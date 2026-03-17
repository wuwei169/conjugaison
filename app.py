from flask import Flask, render_template, jsonify, request, make_response, send_file
import random
from io import BytesIO
from gtts import gTTS
from verbs import VERBS, PRONOUNS, TENSES, get_verb_translation

app = Flask(__name__)


def normalize_answer(answer):
    """Normalize answer for comparison, handling accent variations."""
    return answer.strip().lower()


def check_answer(user_answer, correct_answer):
    """
    Check if user's answer matches the correct answer.
    For passé composé with être verbs, accepts any gender/number variant.
    """
    user = normalize_answer(user_answer)
    correct = normalize_answer(correct_answer)

    # Direct match
    if user == correct:
        return True

    # For passé composé être verbs, accept without parenthetical gender markers
    # e.g., "suis allé" should match "suis allé(e)"
    if "(" in correct:
        # Remove parenthetical parts for comparison
        simplified = correct.replace("(e)", "").replace("(s)", "").replace("(e)s", "s")
        if user == simplified:
            return True
        # Also accept with explicit endings
        variants = [
            correct.replace("(e)", "").replace("(s)", ""),  # masculine singular
            correct.replace("(e)", "e").replace("(s)", ""),  # feminine singular
            correct.replace("(e)", "").replace("(s)", "s"),  # masculine plural
            correct.replace("(e)", "e").replace("(s)", "s"),  # feminine plural
            correct.replace("(e)(s)", "s"),  # masculine plural alt
            correct.replace("(e)(s)", "es"),  # feminine plural
        ]
        if user in [normalize_answer(v) for v in variants]:
            return True

    return False


@app.route("/")
def index():
    """Serve the main quiz page."""
    # Sort verbs by rank for the verb list
    verb_list = sorted(
        [(v, data.get("irregular", False)) for v, data in VERBS.items()],
        key=lambda x: VERBS[x[0]]["rank"]
    )
    return render_template("index.html", tenses=TENSES, verb_list=verb_list)


@app.route("/api/question", methods=["POST"])
def get_question():
    """Generate a random conjugation question with verb filtering."""
    data = request.get_json() or {}
    selected_tenses = data.get("tenses") or list(TENSES.keys())
    max_rank = data.get("maxRank", 10)  # Default to top 10
    irregular_only = data.get("irregularOnly", True)  # Default to irregular only
    selected_pronouns = data.get("pronouns") or list(range(7))  # Default to all 7 pronouns
    mastered_keys = set(data.get("masteredKeys") or [])  # Fully mastered (exclude)
    reduced_weight_keys = set(data.get("reducedWeightKeys") or [])  # 1 correct (1/4 weight)

    # Filter verbs based on settings
    filtered_verbs = []
    for verb, verb_data in VERBS.items():
        rank = verb_data.get("rank", 999)
        is_irregular = verb_data.get("irregular", False)

        if rank > max_rank:
            continue
        if irregular_only and not is_irregular:
            continue
        filtered_verbs.append(verb)

    if not filtered_verbs:
        filtered_verbs = list(VERBS.keys())[:10]  # Fallback

    # Build list of all possible questions with weights
    questions = []

    for verb in filtered_verbs:
        for tense in selected_tenses:
            if tense not in VERBS[verb]:
                continue
            for pronoun_idx in selected_pronouns:
                # Skip impersonal verbs for non-il/elle pronouns
                if VERBS[verb][tense][pronoun_idx] == "-":
                    continue
                key = f"{verb}|{tense}|{pronoun_idx}"

                # Skip mastered questions
                if key in mastered_keys:
                    continue

                # Reduced weight for questions answered correctly once
                weight = 1 if key not in reduced_weight_keys else 0.25
                questions.append((verb, tense, pronoun_idx, key, weight))

    # Check if session is complete
    if not questions:
        return jsonify({"sessionComplete": True})

    # Weighted random selection
    total_weight = sum(q[4] for q in questions)
    r = random.random() * total_weight
    cumulative = 0
    for verb, tense, pronoun_idx, key, weight in questions:
        cumulative += weight
        if r <= cumulative:
            break
    pronoun = PRONOUNS[pronoun_idx]
    correct = VERBS[verb][tense][pronoun_idx]

    return jsonify({
        "verb": verb,
        "translation": get_verb_translation(verb),
        "tense": tense,
        "tense_display": TENSES[tense],
        "pronoun": pronoun,
        "pronoun_idx": pronoun_idx,
        "correct": correct,
        "key": key
    })


@app.route("/api/check", methods=["POST"])
def check():
    """Check the user's answer."""
    data = request.get_json()
    user_answer = data.get("answer", "")
    correct_answer = data.get("correct", "")

    is_correct = check_answer(user_answer, correct_answer)

    return jsonify({
        "correct": is_correct,
        "expected": correct_answer
    })


@app.route("/api/tts", methods=["POST", "OPTIONS"])
def tts():
    if request.method == "OPTIONS":
        res = make_response()
        res.headers["Access-Control-Allow-Origin"] = "*"
        res.headers["Access-Control-Allow-Headers"] = "Content-Type"
        res.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        return res

    data = request.get_json()
    text = (data or {}).get("text", "")
    if not text:
        return jsonify({"error": "no text"}), 400

    mp3 = BytesIO()
    gTTS(text=text, lang="fr", tld="fr").write_to_fp(mp3)
    mp3.seek(0)

    res = make_response(send_file(mp3, mimetype="audio/mpeg"))
    res.headers["Access-Control-Allow-Origin"] = "*"
    return res


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
