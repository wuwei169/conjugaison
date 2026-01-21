# French Verb Conjugations
# Structure: verbs[infinitive] = {translation, rank, irregular, tenses...}
# rank: frequency rank (1 = most common)
# irregular: True if verb has irregular conjugations

PRONOUNS = ["je", "tu", "il/elle", "on", "nous", "vous", "ils/elles"]

TENSES = {
    "présent": "Présent",
    "passé_composé": "Passé Composé",
    "imparfait": "Imparfait",
    "futur_simple": "Futur Simple",
    "conditionnel": "Conditionnel Présent",
    "subjonctif": "Subjonctif Présent"
}

VERBS = {
    # Top 10 most common French verbs (all irregular)
    "être": {
        "translation": "to be",
        "rank": 1,
        "irregular": True,
        "présent": ["suis", "es", "est", "est", "sommes", "êtes", "sont"],
        "passé_composé": ["ai été", "as été", "a été", "a été", "avons été", "avez été", "ont été"],
        "imparfait": ["étais", "étais", "était", "était", "étions", "étiez", "étaient"],
        "futur_simple": ["serai", "seras", "sera", "sera", "serons", "serez", "seront"],
        "conditionnel": ["serais", "serais", "serait", "serait", "serions", "seriez", "seraient"],
        "subjonctif": ["sois", "sois", "soit", "soit", "soyons", "soyez", "soient"]
    },
    "avoir": {
        "translation": "to have",
        "rank": 2,
        "irregular": True,
        "présent": ["ai", "as", "a", "a", "avons", "avez", "ont"],
        "passé_composé": ["ai eu", "as eu", "a eu", "a eu", "avons eu", "avez eu", "ont eu"],
        "imparfait": ["avais", "avais", "avait", "avait", "avions", "aviez", "avaient"],
        "futur_simple": ["aurai", "auras", "aura", "aura", "aurons", "aurez", "auront"],
        "conditionnel": ["aurais", "aurais", "aurait", "aurait", "aurions", "auriez", "auraient"],
        "subjonctif": ["aie", "aies", "ait", "ait", "ayons", "ayez", "aient"]
    },
    "faire": {
        "translation": "to do/make",
        "rank": 3,
        "irregular": True,
        "présent": ["fais", "fais", "fait", "fait", "faisons", "faites", "font"],
        "passé_composé": ["ai fait", "as fait", "a fait", "a fait", "avons fait", "avez fait", "ont fait"],
        "imparfait": ["faisais", "faisais", "faisait", "faisait", "faisions", "faisiez", "faisaient"],
        "futur_simple": ["ferai", "feras", "fera", "fera", "ferons", "ferez", "feront"],
        "conditionnel": ["ferais", "ferais", "ferait", "ferait", "ferions", "feriez", "feraient"],
        "subjonctif": ["fasse", "fasses", "fasse", "fasse", "fassions", "fassiez", "fassent"]
    },
    "dire": {
        "translation": "to say/tell",
        "rank": 4,
        "irregular": True,
        "présent": ["dis", "dis", "dit", "dit", "disons", "dites", "disent"],
        "passé_composé": ["ai dit", "as dit", "a dit", "a dit", "avons dit", "avez dit", "ont dit"],
        "imparfait": ["disais", "disais", "disait", "disait", "disions", "disiez", "disaient"],
        "futur_simple": ["dirai", "diras", "dira", "dira", "dirons", "direz", "diront"],
        "conditionnel": ["dirais", "dirais", "dirait", "dirait", "dirions", "diriez", "diraient"],
        "subjonctif": ["dise", "dises", "dise", "dise", "disions", "disiez", "disent"]
    },
    "pouvoir": {
        "translation": "to be able to/can",
        "rank": 5,
        "irregular": True,
        "présent": ["peux", "peux", "peut", "peut", "pouvons", "pouvez", "peuvent"],
        "passé_composé": ["ai pu", "as pu", "a pu", "a pu", "avons pu", "avez pu", "ont pu"],
        "imparfait": ["pouvais", "pouvais", "pouvait", "pouvait", "pouvions", "pouviez", "pouvaient"],
        "futur_simple": ["pourrai", "pourras", "pourra", "pourra", "pourrons", "pourrez", "pourront"],
        "conditionnel": ["pourrais", "pourrais", "pourrait", "pourrait", "pourrions", "pourriez", "pourraient"],
        "subjonctif": ["puisse", "puisses", "puisse", "puisse", "puissions", "puissiez", "puissent"]
    },
    "aller": {
        "translation": "to go",
        "rank": 6,
        "irregular": True,
        "présent": ["vais", "vas", "va", "va", "allons", "allez", "vont"],
        "passé_composé": ["suis allé(e)", "es allé(e)", "est allé(e)", "est allé(e)", "sommes allé(e)s", "êtes allé(e)(s)", "sont allé(e)s"],
        "imparfait": ["allais", "allais", "allait", "allait", "allions", "alliez", "allaient"],
        "futur_simple": ["irai", "iras", "ira", "ira", "irons", "irez", "iront"],
        "conditionnel": ["irais", "irais", "irait", "irait", "irions", "iriez", "iraient"],
        "subjonctif": ["aille", "ailles", "aille", "aille", "allions", "alliez", "aillent"]
    },
    "voir": {
        "translation": "to see",
        "rank": 7,
        "irregular": True,
        "présent": ["vois", "vois", "voit", "voit", "voyons", "voyez", "voient"],
        "passé_composé": ["ai vu", "as vu", "a vu", "a vu", "avons vu", "avez vu", "ont vu"],
        "imparfait": ["voyais", "voyais", "voyait", "voyait", "voyions", "voyiez", "voyaient"],
        "futur_simple": ["verrai", "verras", "verra", "verra", "verrons", "verrez", "verront"],
        "conditionnel": ["verrais", "verrais", "verrait", "verrait", "verrions", "verriez", "verraient"],
        "subjonctif": ["voie", "voies", "voie", "voie", "voyions", "voyiez", "voient"]
    },
    "vouloir": {
        "translation": "to want",
        "rank": 8,
        "irregular": True,
        "présent": ["veux", "veux", "veut", "veut", "voulons", "voulez", "veulent"],
        "passé_composé": ["ai voulu", "as voulu", "a voulu", "a voulu", "avons voulu", "avez voulu", "ont voulu"],
        "imparfait": ["voulais", "voulais", "voulait", "voulait", "voulions", "vouliez", "voulaient"],
        "futur_simple": ["voudrai", "voudras", "voudra", "voudra", "voudrons", "voudrez", "voudront"],
        "conditionnel": ["voudrais", "voudrais", "voudrait", "voudrait", "voudrions", "voudriez", "voudraient"],
        "subjonctif": ["veuille", "veuilles", "veuille", "veuille", "voulions", "vouliez", "veuillent"]
    },
    "venir": {
        "translation": "to come",
        "rank": 9,
        "irregular": True,
        "présent": ["viens", "viens", "vient", "vient", "venons", "venez", "viennent"],
        "passé_composé": ["suis venu(e)", "es venu(e)", "est venu(e)", "est venu(e)", "sommes venu(e)s", "êtes venu(e)(s)", "sont venu(e)s"],
        "imparfait": ["venais", "venais", "venait", "venait", "venions", "veniez", "venaient"],
        "futur_simple": ["viendrai", "viendras", "viendra", "viendra", "viendrons", "viendrez", "viendront"],
        "conditionnel": ["viendrais", "viendrais", "viendrait", "viendrait", "viendrions", "viendriez", "viendraient"],
        "subjonctif": ["vienne", "viennes", "vienne", "vienne", "venions", "veniez", "viennent"]
    },
    "devoir": {
        "translation": "to have to/must",
        "rank": 10,
        "irregular": True,
        "présent": ["dois", "dois", "doit", "doit", "devons", "devez", "doivent"],
        "passé_composé": ["ai dû", "as dû", "a dû", "a dû", "avons dû", "avez dû", "ont dû"],
        "imparfait": ["devais", "devais", "devait", "devait", "devions", "deviez", "devaient"],
        "futur_simple": ["devrai", "devras", "devra", "devra", "devrons", "devrez", "devront"],
        "conditionnel": ["devrais", "devrais", "devrait", "devrait", "devrions", "devriez", "devraient"],
        "subjonctif": ["doive", "doives", "doive", "doive", "devions", "deviez", "doivent"]
    },

    # Top 11-20
    "prendre": {
        "translation": "to take",
        "rank": 11,
        "irregular": True,
        "présent": ["prends", "prends", "prend", "prend", "prenons", "prenez", "prennent"],
        "passé_composé": ["ai pris", "as pris", "a pris", "a pris", "avons pris", "avez pris", "ont pris"],
        "imparfait": ["prenais", "prenais", "prenait", "prenait", "prenions", "preniez", "prenaient"],
        "futur_simple": ["prendrai", "prendras", "prendra", "prendra", "prendrons", "prendrez", "prendront"],
        "conditionnel": ["prendrais", "prendrais", "prendrait", "prendrait", "prendrions", "prendriez", "prendraient"],
        "subjonctif": ["prenne", "prennes", "prenne", "prenne", "prenions", "preniez", "prennent"]
    },
    "savoir": {
        "translation": "to know (facts)",
        "rank": 12,
        "irregular": True,
        "présent": ["sais", "sais", "sait", "sait", "savons", "savez", "savent"],
        "passé_composé": ["ai su", "as su", "a su", "a su", "avons su", "avez su", "ont su"],
        "imparfait": ["savais", "savais", "savait", "savait", "savions", "saviez", "savaient"],
        "futur_simple": ["saurai", "sauras", "saura", "saura", "saurons", "saurez", "sauront"],
        "conditionnel": ["saurais", "saurais", "saurait", "saurait", "saurions", "sauriez", "sauraient"],
        "subjonctif": ["sache", "saches", "sache", "sache", "sachions", "sachiez", "sachent"]
    },
    "falloir": {
        "translation": "to be necessary",
        "rank": 13,
        "irregular": True,
        "présent": ["-", "-", "faut", "faut", "-", "-", "-"],
        "passé_composé": ["-", "-", "a fallu", "a fallu", "-", "-", "-"],
        "imparfait": ["-", "-", "fallait", "fallait", "-", "-", "-"],
        "futur_simple": ["-", "-", "faudra", "faudra", "-", "-", "-"],
        "conditionnel": ["-", "-", "faudrait", "faudrait", "-", "-", "-"],
        "subjonctif": ["-", "-", "faille", "faille", "-", "-", "-"]
    },
    "croire": {
        "translation": "to believe",
        "rank": 14,
        "irregular": True,
        "présent": ["crois", "crois", "croit", "croit", "croyons", "croyez", "croient"],
        "passé_composé": ["ai cru", "as cru", "a cru", "a cru", "avons cru", "avez cru", "ont cru"],
        "imparfait": ["croyais", "croyais", "croyait", "croyait", "croyions", "croyiez", "croyaient"],
        "futur_simple": ["croirai", "croiras", "croira", "croira", "croirons", "croirez", "croiront"],
        "conditionnel": ["croirais", "croirais", "croirait", "croirait", "croirions", "croiriez", "croiraient"],
        "subjonctif": ["croie", "croies", "croie", "croie", "croyions", "croyiez", "croient"]
    },
    "mettre": {
        "translation": "to put",
        "rank": 15,
        "irregular": True,
        "présent": ["mets", "mets", "met", "met", "mettons", "mettez", "mettent"],
        "passé_composé": ["ai mis", "as mis", "a mis", "a mis", "avons mis", "avez mis", "ont mis"],
        "imparfait": ["mettais", "mettais", "mettait", "mettait", "mettions", "mettiez", "mettaient"],
        "futur_simple": ["mettrai", "mettras", "mettra", "mettra", "mettrons", "mettrez", "mettront"],
        "conditionnel": ["mettrais", "mettrais", "mettrait", "mettrait", "mettrions", "mettriez", "mettraient"],
        "subjonctif": ["mette", "mettes", "mette", "mette", "mettions", "mettiez", "mettent"]
    },
    "parler": {
        "translation": "to speak",
        "rank": 16,
        "irregular": False,
        "présent": ["parle", "parles", "parle", "parle", "parlons", "parlez", "parlent"],
        "passé_composé": ["ai parlé", "as parlé", "a parlé", "a parlé", "avons parlé", "avez parlé", "ont parlé"],
        "imparfait": ["parlais", "parlais", "parlait", "parlait", "parlions", "parliez", "parlaient"],
        "futur_simple": ["parlerai", "parleras", "parlera", "parlera", "parlerons", "parlerez", "parleront"],
        "conditionnel": ["parlerais", "parlerais", "parlerait", "parlerait", "parlerions", "parleriez", "parleraient"],
        "subjonctif": ["parle", "parles", "parle", "parle", "parlions", "parliez", "parlent"]
    },
    "demander": {
        "translation": "to ask",
        "rank": 17,
        "irregular": False,
        "présent": ["demande", "demandes", "demande", "demande", "demandons", "demandez", "demandent"],
        "passé_composé": ["ai demandé", "as demandé", "a demandé", "a demandé", "avons demandé", "avez demandé", "ont demandé"],
        "imparfait": ["demandais", "demandais", "demandait", "demandait", "demandions", "demandiez", "demandaient"],
        "futur_simple": ["demanderai", "demanderas", "demandera", "demandera", "demanderons", "demanderez", "demanderont"],
        "conditionnel": ["demanderais", "demanderais", "demanderait", "demanderait", "demanderions", "demanderiez", "demanderaient"],
        "subjonctif": ["demande", "demandes", "demande", "demande", "demandions", "demandiez", "demandent"]
    },
    "tenir": {
        "translation": "to hold",
        "rank": 18,
        "irregular": True,
        "présent": ["tiens", "tiens", "tient", "tient", "tenons", "tenez", "tiennent"],
        "passé_composé": ["ai tenu", "as tenu", "a tenu", "a tenu", "avons tenu", "avez tenu", "ont tenu"],
        "imparfait": ["tenais", "tenais", "tenait", "tenait", "tenions", "teniez", "tenaient"],
        "futur_simple": ["tiendrai", "tiendras", "tiendra", "tiendra", "tiendrons", "tiendrez", "tiendront"],
        "conditionnel": ["tiendrais", "tiendrais", "tiendrait", "tiendrait", "tiendrions", "tiendriez", "tiendraient"],
        "subjonctif": ["tienne", "tiennes", "tienne", "tienne", "tenions", "teniez", "tiennent"]
    },
    "donner": {
        "translation": "to give",
        "rank": 19,
        "irregular": False,
        "présent": ["donne", "donnes", "donne", "donne", "donnons", "donnez", "donnent"],
        "passé_composé": ["ai donné", "as donné", "a donné", "a donné", "avons donné", "avez donné", "ont donné"],
        "imparfait": ["donnais", "donnais", "donnait", "donnait", "donnions", "donniez", "donnaient"],
        "futur_simple": ["donnerai", "donneras", "donnera", "donnera", "donnerons", "donnerez", "donneront"],
        "conditionnel": ["donnerais", "donnerais", "donnerait", "donnerait", "donnerions", "donneriez", "donneraient"],
        "subjonctif": ["donne", "donnes", "donne", "donne", "donnions", "donniez", "donnent"]
    },
    "penser": {
        "translation": "to think",
        "rank": 20,
        "irregular": False,
        "présent": ["pense", "penses", "pense", "pense", "pensons", "pensez", "pensent"],
        "passé_composé": ["ai pensé", "as pensé", "a pensé", "a pensé", "avons pensé", "avez pensé", "ont pensé"],
        "imparfait": ["pensais", "pensais", "pensait", "pensait", "pensions", "pensiez", "pensaient"],
        "futur_simple": ["penserai", "penseras", "pensera", "pensera", "penserons", "penserez", "penseront"],
        "conditionnel": ["penserais", "penserais", "penserait", "penserait", "penserions", "penseriez", "penseraient"],
        "subjonctif": ["pense", "penses", "pense", "pense", "pensions", "pensiez", "pensent"]
    },

    # Top 21-50
    "partir": {
        "translation": "to leave",
        "rank": 21,
        "irregular": True,
        "présent": ["pars", "pars", "part", "part", "partons", "partez", "partent"],
        "passé_composé": ["suis parti(e)", "es parti(e)", "est parti(e)", "est parti(e)", "sommes parti(e)s", "êtes parti(e)(s)", "sont parti(e)s"],
        "imparfait": ["partais", "partais", "partait", "partait", "partions", "partiez", "partaient"],
        "futur_simple": ["partirai", "partiras", "partira", "partira", "partirons", "partirez", "partiront"],
        "conditionnel": ["partirais", "partirais", "partirait", "partirait", "partirions", "partiriez", "partiraient"],
        "subjonctif": ["parte", "partes", "parte", "parte", "partions", "partiez", "partent"]
    },
    "connaître": {
        "translation": "to know (people/places)",
        "rank": 22,
        "irregular": True,
        "présent": ["connais", "connais", "connaît", "connaît", "connaissons", "connaissez", "connaissent"],
        "passé_composé": ["ai connu", "as connu", "a connu", "a connu", "avons connu", "avez connu", "ont connu"],
        "imparfait": ["connaissais", "connaissais", "connaissait", "connaissait", "connaissions", "connaissiez", "connaissaient"],
        "futur_simple": ["connaîtrai", "connaîtras", "connaîtra", "connaîtra", "connaîtrons", "connaîtrez", "connaîtront"],
        "conditionnel": ["connaîtrais", "connaîtrais", "connaîtrait", "connaîtrait", "connaîtrions", "connaîtriez", "connaîtraient"],
        "subjonctif": ["connaisse", "connaisses", "connaisse", "connaisse", "connaissions", "connaissiez", "connaissent"]
    },
    "trouver": {
        "translation": "to find",
        "rank": 23,
        "irregular": False,
        "présent": ["trouve", "trouves", "trouve", "trouve", "trouvons", "trouvez", "trouvent"],
        "passé_composé": ["ai trouvé", "as trouvé", "a trouvé", "a trouvé", "avons trouvé", "avez trouvé", "ont trouvé"],
        "imparfait": ["trouvais", "trouvais", "trouvait", "trouvait", "trouvions", "trouviez", "trouvaient"],
        "futur_simple": ["trouverai", "trouveras", "trouvera", "trouvera", "trouverons", "trouverez", "trouveront"],
        "conditionnel": ["trouverais", "trouverais", "trouverait", "trouverait", "trouverions", "trouveriez", "trouveraient"],
        "subjonctif": ["trouve", "trouves", "trouve", "trouve", "trouvions", "trouviez", "trouvent"]
    },
    "rendre": {
        "translation": "to return/give back",
        "rank": 24,
        "irregular": False,
        "présent": ["rends", "rends", "rend", "rend", "rendons", "rendez", "rendent"],
        "passé_composé": ["ai rendu", "as rendu", "a rendu", "a rendu", "avons rendu", "avez rendu", "ont rendu"],
        "imparfait": ["rendais", "rendais", "rendait", "rendait", "rendions", "rendiez", "rendaient"],
        "futur_simple": ["rendrai", "rendras", "rendra", "rendra", "rendrons", "rendrez", "rendront"],
        "conditionnel": ["rendrais", "rendrais", "rendrait", "rendrait", "rendrions", "rendriez", "rendraient"],
        "subjonctif": ["rende", "rendes", "rende", "rende", "rendions", "rendiez", "rendent"]
    },
    "entendre": {
        "translation": "to hear",
        "rank": 25,
        "irregular": False,
        "présent": ["entends", "entends", "entend", "entend", "entendons", "entendez", "entendent"],
        "passé_composé": ["ai entendu", "as entendu", "a entendu", "a entendu", "avons entendu", "avez entendu", "ont entendu"],
        "imparfait": ["entendais", "entendais", "entendait", "entendait", "entendions", "entendiez", "entendaient"],
        "futur_simple": ["entendrai", "entendras", "entendra", "entendra", "entendrons", "entendrez", "entendront"],
        "conditionnel": ["entendrais", "entendrais", "entendrait", "entendrait", "entendrions", "entendriez", "entendraient"],
        "subjonctif": ["entende", "entendes", "entende", "entende", "entendions", "entendiez", "entendent"]
    },
    "attendre": {
        "translation": "to wait",
        "rank": 26,
        "irregular": False,
        "présent": ["attends", "attends", "attend", "attend", "attendons", "attendez", "attendent"],
        "passé_composé": ["ai attendu", "as attendu", "a attendu", "a attendu", "avons attendu", "avez attendu", "ont attendu"],
        "imparfait": ["attendais", "attendais", "attendait", "attendait", "attendions", "attendiez", "attendaient"],
        "futur_simple": ["attendrai", "attendras", "attendra", "attendra", "attendrons", "attendrez", "attendront"],
        "conditionnel": ["attendrais", "attendrais", "attendrait", "attendrait", "attendrions", "attendriez", "attendraient"],
        "subjonctif": ["attende", "attendes", "attende", "attende", "attendions", "attendiez", "attendent"]
    },
    "sortir": {
        "translation": "to go out",
        "rank": 27,
        "irregular": True,
        "présent": ["sors", "sors", "sort", "sort", "sortons", "sortez", "sortent"],
        "passé_composé": ["suis sorti(e)", "es sorti(e)", "est sorti(e)", "est sorti(e)", "sommes sorti(e)s", "êtes sorti(e)(s)", "sont sorti(e)s"],
        "imparfait": ["sortais", "sortais", "sortait", "sortait", "sortions", "sortiez", "sortaient"],
        "futur_simple": ["sortirai", "sortiras", "sortira", "sortira", "sortirons", "sortirez", "sortiront"],
        "conditionnel": ["sortirais", "sortirais", "sortirait", "sortirait", "sortirions", "sortiriez", "sortiraient"],
        "subjonctif": ["sorte", "sortes", "sorte", "sorte", "sortions", "sortiez", "sortent"]
    },
    "rester": {
        "translation": "to stay",
        "rank": 28,
        "irregular": False,
        "présent": ["reste", "restes", "reste", "reste", "restons", "restez", "restent"],
        "passé_composé": ["suis resté(e)", "es resté(e)", "est resté(e)", "est resté(e)", "sommes resté(e)s", "êtes resté(e)(s)", "sont resté(e)s"],
        "imparfait": ["restais", "restais", "restait", "restait", "restions", "restiez", "restaient"],
        "futur_simple": ["resterai", "resteras", "restera", "restera", "resterons", "resterez", "resteront"],
        "conditionnel": ["resterais", "resterais", "resterait", "resterait", "resterions", "resteriez", "resteraient"],
        "subjonctif": ["reste", "restes", "reste", "reste", "restions", "restiez", "restent"]
    },
    "sentir": {
        "translation": "to feel/smell",
        "rank": 29,
        "irregular": True,
        "présent": ["sens", "sens", "sent", "sent", "sentons", "sentez", "sentent"],
        "passé_composé": ["ai senti", "as senti", "a senti", "a senti", "avons senti", "avez senti", "ont senti"],
        "imparfait": ["sentais", "sentais", "sentait", "sentait", "sentions", "sentiez", "sentaient"],
        "futur_simple": ["sentirai", "sentiras", "sentira", "sentira", "sentirons", "sentirez", "sentiront"],
        "conditionnel": ["sentirais", "sentirais", "sentirait", "sentirait", "sentirions", "sentiriez", "sentiraient"],
        "subjonctif": ["sente", "sentes", "sente", "sente", "sentions", "sentiez", "sentent"]
    },
    "aimer": {
        "translation": "to love/like",
        "rank": 30,
        "irregular": False,
        "présent": ["aime", "aimes", "aime", "aime", "aimons", "aimez", "aiment"],
        "passé_composé": ["ai aimé", "as aimé", "a aimé", "a aimé", "avons aimé", "avez aimé", "ont aimé"],
        "imparfait": ["aimais", "aimais", "aimait", "aimait", "aimions", "aimiez", "aimaient"],
        "futur_simple": ["aimerai", "aimeras", "aimera", "aimera", "aimerons", "aimerez", "aimeront"],
        "conditionnel": ["aimerais", "aimerais", "aimerait", "aimerait", "aimerions", "aimeriez", "aimeraient"],
        "subjonctif": ["aime", "aimes", "aime", "aime", "aimions", "aimiez", "aiment"]
    },
    "passer": {
        "translation": "to pass/spend time",
        "rank": 31,
        "irregular": False,
        "présent": ["passe", "passes", "passe", "passe", "passons", "passez", "passent"],
        "passé_composé": ["ai passé", "as passé", "a passé", "a passé", "avons passé", "avez passé", "ont passé"],
        "imparfait": ["passais", "passais", "passait", "passait", "passions", "passiez", "passaient"],
        "futur_simple": ["passerai", "passeras", "passera", "passera", "passerons", "passerez", "passeront"],
        "conditionnel": ["passerais", "passerais", "passerait", "passerait", "passerions", "passeriez", "passeraient"],
        "subjonctif": ["passe", "passes", "passe", "passe", "passions", "passiez", "passent"]
    },
    "porter": {
        "translation": "to carry/wear",
        "rank": 32,
        "irregular": False,
        "présent": ["porte", "portes", "porte", "porte", "portons", "portez", "portent"],
        "passé_composé": ["ai porté", "as porté", "a porté", "a porté", "avons porté", "avez porté", "ont porté"],
        "imparfait": ["portais", "portais", "portait", "portait", "portions", "portiez", "portaient"],
        "futur_simple": ["porterai", "porteras", "portera", "portera", "porterons", "porterez", "porteront"],
        "conditionnel": ["porterais", "porterais", "porterait", "porterait", "porterions", "porteriez", "porteraient"],
        "subjonctif": ["porte", "portes", "porte", "porte", "portions", "portiez", "portent"]
    },
    "comprendre": {
        "translation": "to understand",
        "rank": 33,
        "irregular": True,
        "présent": ["comprends", "comprends", "comprend", "comprend", "comprenons", "comprenez", "comprennent"],
        "passé_composé": ["ai compris", "as compris", "a compris", "a compris", "avons compris", "avez compris", "ont compris"],
        "imparfait": ["comprenais", "comprenais", "comprenait", "comprenait", "comprenions", "compreniez", "comprenaient"],
        "futur_simple": ["comprendrai", "comprendras", "comprendra", "comprendra", "comprendrons", "comprendrez", "comprendront"],
        "conditionnel": ["comprendrais", "comprendrais", "comprendrait", "comprendrait", "comprendrions", "comprendriez", "comprendraient"],
        "subjonctif": ["comprenne", "comprennes", "comprenne", "comprenne", "comprenions", "compreniez", "comprennent"]
    },
    "écrire": {
        "translation": "to write",
        "rank": 34,
        "irregular": True,
        "présent": ["écris", "écris", "écrit", "écrit", "écrivons", "écrivez", "écrivent"],
        "passé_composé": ["ai écrit", "as écrit", "a écrit", "a écrit", "avons écrit", "avez écrit", "ont écrit"],
        "imparfait": ["écrivais", "écrivais", "écrivait", "écrivait", "écrivions", "écriviez", "écrivaient"],
        "futur_simple": ["écrirai", "écriras", "écrira", "écrira", "écrirons", "écrirez", "écriront"],
        "conditionnel": ["écrirais", "écrirais", "écrirait", "écrirait", "écririons", "écririez", "écriraient"],
        "subjonctif": ["écrive", "écrives", "écrive", "écrive", "écrivions", "écriviez", "écrivent"]
    },
    "lire": {
        "translation": "to read",
        "rank": 35,
        "irregular": True,
        "présent": ["lis", "lis", "lit", "lit", "lisons", "lisez", "lisent"],
        "passé_composé": ["ai lu", "as lu", "a lu", "a lu", "avons lu", "avez lu", "ont lu"],
        "imparfait": ["lisais", "lisais", "lisait", "lisait", "lisions", "lisiez", "lisaient"],
        "futur_simple": ["lirai", "liras", "lira", "lira", "lirons", "lirez", "liront"],
        "conditionnel": ["lirais", "lirais", "lirait", "lirait", "lirions", "liriez", "liraient"],
        "subjonctif": ["lise", "lises", "lise", "lise", "lisions", "lisiez", "lisent"]
    },
    "perdre": {
        "translation": "to lose",
        "rank": 36,
        "irregular": False,
        "présent": ["perds", "perds", "perd", "perd", "perdons", "perdez", "perdent"],
        "passé_composé": ["ai perdu", "as perdu", "a perdu", "a perdu", "avons perdu", "avez perdu", "ont perdu"],
        "imparfait": ["perdais", "perdais", "perdait", "perdait", "perdions", "perdiez", "perdaient"],
        "futur_simple": ["perdrai", "perdras", "perdra", "perdra", "perdrons", "perdrez", "perdront"],
        "conditionnel": ["perdrais", "perdrais", "perdrait", "perdrait", "perdrions", "perdriez", "perdraient"],
        "subjonctif": ["perde", "perdes", "perde", "perde", "perdions", "perdiez", "perdent"]
    },
    "commencer": {
        "translation": "to begin",
        "rank": 37,
        "irregular": False,
        "présent": ["commence", "commences", "commence", "commence", "commençons", "commencez", "commencent"],
        "passé_composé": ["ai commencé", "as commencé", "a commencé", "a commencé", "avons commencé", "avez commencé", "ont commencé"],
        "imparfait": ["commençais", "commençais", "commençait", "commençait", "commencions", "commenciez", "commençaient"],
        "futur_simple": ["commencerai", "commenceras", "commencera", "commencera", "commencerons", "commencerez", "commenceront"],
        "conditionnel": ["commencerais", "commencerais", "commencerait", "commencerait", "commencerions", "commenceriez", "commenceraient"],
        "subjonctif": ["commence", "commences", "commence", "commence", "commencions", "commenciez", "commencent"]
    },
    "appeler": {
        "translation": "to call",
        "rank": 38,
        "irregular": False,
        "présent": ["appelle", "appelles", "appelle", "appelle", "appelons", "appelez", "appellent"],
        "passé_composé": ["ai appelé", "as appelé", "a appelé", "a appelé", "avons appelé", "avez appelé", "ont appelé"],
        "imparfait": ["appelais", "appelais", "appelait", "appelait", "appelions", "appeliez", "appelaient"],
        "futur_simple": ["appellerai", "appelleras", "appellera", "appellera", "appellerons", "appellerez", "appelleront"],
        "conditionnel": ["appellerais", "appellerais", "appellerait", "appellerait", "appellerions", "appelleriez", "appelleraient"],
        "subjonctif": ["appelle", "appelles", "appelle", "appelle", "appelions", "appeliez", "appellent"]
    },
    "suivre": {
        "translation": "to follow",
        "rank": 39,
        "irregular": True,
        "présent": ["suis", "suis", "suit", "suit", "suivons", "suivez", "suivent"],
        "passé_composé": ["ai suivi", "as suivi", "a suivi", "a suivi", "avons suivi", "avez suivi", "ont suivi"],
        "imparfait": ["suivais", "suivais", "suivait", "suivait", "suivions", "suiviez", "suivaient"],
        "futur_simple": ["suivrai", "suivras", "suivra", "suivra", "suivrons", "suivrez", "suivront"],
        "conditionnel": ["suivrais", "suivrais", "suivrait", "suivrait", "suivrions", "suivriez", "suivraient"],
        "subjonctif": ["suive", "suives", "suive", "suive", "suivions", "suiviez", "suivent"]
    },
    "mourir": {
        "translation": "to die",
        "rank": 40,
        "irregular": True,
        "présent": ["meurs", "meurs", "meurt", "meurt", "mourons", "mourez", "meurent"],
        "passé_composé": ["suis mort(e)", "es mort(e)", "est mort(e)", "est mort(e)", "sommes mort(e)s", "êtes mort(e)(s)", "sont mort(e)s"],
        "imparfait": ["mourais", "mourais", "mourait", "mourait", "mourions", "mouriez", "mouraient"],
        "futur_simple": ["mourrai", "mourras", "mourra", "mourra", "mourrons", "mourrez", "mourront"],
        "conditionnel": ["mourrais", "mourrais", "mourrait", "mourrait", "mourrions", "mourriez", "mourraient"],
        "subjonctif": ["meure", "meures", "meure", "meure", "mourions", "mouriez", "meurent"]
    },
    "vivre": {
        "translation": "to live",
        "rank": 41,
        "irregular": True,
        "présent": ["vis", "vis", "vit", "vit", "vivons", "vivez", "vivent"],
        "passé_composé": ["ai vécu", "as vécu", "a vécu", "a vécu", "avons vécu", "avez vécu", "ont vécu"],
        "imparfait": ["vivais", "vivais", "vivait", "vivait", "vivions", "viviez", "vivaient"],
        "futur_simple": ["vivrai", "vivras", "vivra", "vivra", "vivrons", "vivrez", "vivront"],
        "conditionnel": ["vivrais", "vivrais", "vivrait", "vivrait", "vivrions", "vivriez", "vivraient"],
        "subjonctif": ["vive", "vives", "vive", "vive", "vivions", "viviez", "vivent"]
    },
    "boire": {
        "translation": "to drink",
        "rank": 42,
        "irregular": True,
        "présent": ["bois", "bois", "boit", "boit", "buvons", "buvez", "boivent"],
        "passé_composé": ["ai bu", "as bu", "a bu", "a bu", "avons bu", "avez bu", "ont bu"],
        "imparfait": ["buvais", "buvais", "buvait", "buvait", "buvions", "buviez", "buvaient"],
        "futur_simple": ["boirai", "boiras", "boira", "boira", "boirons", "boirez", "boiront"],
        "conditionnel": ["boirais", "boirais", "boirait", "boirait", "boirions", "boiriez", "boiraient"],
        "subjonctif": ["boive", "boives", "boive", "boive", "buvions", "buviez", "boivent"]
    },
    "dormir": {
        "translation": "to sleep",
        "rank": 43,
        "irregular": True,
        "présent": ["dors", "dors", "dort", "dort", "dormons", "dormez", "dorment"],
        "passé_composé": ["ai dormi", "as dormi", "a dormi", "a dormi", "avons dormi", "avez dormi", "ont dormi"],
        "imparfait": ["dormais", "dormais", "dormait", "dormait", "dormions", "dormiez", "dormaient"],
        "futur_simple": ["dormirai", "dormiras", "dormira", "dormira", "dormirons", "dormirez", "dormiront"],
        "conditionnel": ["dormirais", "dormirais", "dormirait", "dormirait", "dormirions", "dormiriez", "dormiraient"],
        "subjonctif": ["dorme", "dormes", "dorme", "dorme", "dormions", "dormiez", "dorment"]
    },
    "courir": {
        "translation": "to run",
        "rank": 44,
        "irregular": True,
        "présent": ["cours", "cours", "court", "court", "courons", "courez", "courent"],
        "passé_composé": ["ai couru", "as couru", "a couru", "a couru", "avons couru", "avez couru", "ont couru"],
        "imparfait": ["courais", "courais", "courait", "courait", "courions", "couriez", "couraient"],
        "futur_simple": ["courrai", "courras", "courra", "courra", "courrons", "courrez", "courront"],
        "conditionnel": ["courrais", "courrais", "courrait", "courrait", "courrions", "courriez", "courraient"],
        "subjonctif": ["coure", "coures", "coure", "coure", "courions", "couriez", "courent"]
    },
    "servir": {
        "translation": "to serve",
        "rank": 45,
        "irregular": True,
        "présent": ["sers", "sers", "sert", "sert", "servons", "servez", "servent"],
        "passé_composé": ["ai servi", "as servi", "a servi", "a servi", "avons servi", "avez servi", "ont servi"],
        "imparfait": ["servais", "servais", "servait", "servait", "servions", "serviez", "servaient"],
        "futur_simple": ["servirai", "serviras", "servira", "servira", "servirons", "servirez", "serviront"],
        "conditionnel": ["servirais", "servirais", "servirait", "servirait", "servirions", "serviriez", "serviraient"],
        "subjonctif": ["serve", "serves", "serve", "serve", "servions", "serviez", "servent"]
    },
    "ouvrir": {
        "translation": "to open",
        "rank": 46,
        "irregular": True,
        "présent": ["ouvre", "ouvres", "ouvre", "ouvre", "ouvrons", "ouvrez", "ouvrent"],
        "passé_composé": ["ai ouvert", "as ouvert", "a ouvert", "a ouvert", "avons ouvert", "avez ouvert", "ont ouvert"],
        "imparfait": ["ouvrais", "ouvrais", "ouvrait", "ouvrait", "ouvrions", "ouvriez", "ouvraient"],
        "futur_simple": ["ouvrirai", "ouvriras", "ouvrira", "ouvrira", "ouvrirons", "ouvrirez", "ouvriront"],
        "conditionnel": ["ouvrirais", "ouvrirais", "ouvrirait", "ouvrirait", "ouvririons", "ouvririez", "ouvriraient"],
        "subjonctif": ["ouvre", "ouvres", "ouvre", "ouvre", "ouvrions", "ouvriez", "ouvrent"]
    },
    "recevoir": {
        "translation": "to receive",
        "rank": 47,
        "irregular": True,
        "présent": ["reçois", "reçois", "reçoit", "reçoit", "recevons", "recevez", "reçoivent"],
        "passé_composé": ["ai reçu", "as reçu", "a reçu", "a reçu", "avons reçu", "avez reçu", "ont reçu"],
        "imparfait": ["recevais", "recevais", "recevait", "recevait", "recevions", "receviez", "recevaient"],
        "futur_simple": ["recevrai", "recevras", "recevra", "recevra", "recevrons", "recevrez", "recevront"],
        "conditionnel": ["recevrais", "recevrais", "recevrait", "recevrait", "recevrions", "recevriez", "recevraient"],
        "subjonctif": ["reçoive", "reçoives", "reçoive", "reçoive", "recevions", "receviez", "reçoivent"]
    },
    "répondre": {
        "translation": "to answer",
        "rank": 48,
        "irregular": False,
        "présent": ["réponds", "réponds", "répond", "répond", "répondons", "répondez", "répondent"],
        "passé_composé": ["ai répondu", "as répondu", "a répondu", "a répondu", "avons répondu", "avez répondu", "ont répondu"],
        "imparfait": ["répondais", "répondais", "répondait", "répondait", "répondions", "répondiez", "répondaient"],
        "futur_simple": ["répondrai", "répondras", "répondra", "répondra", "répondrons", "répondrez", "répondront"],
        "conditionnel": ["répondrais", "répondrais", "répondrait", "répondrait", "répondrions", "répondriez", "répondraient"],
        "subjonctif": ["réponde", "répondes", "réponde", "réponde", "répondions", "répondiez", "répondent"]
    },
    "naître": {
        "translation": "to be born",
        "rank": 49,
        "irregular": True,
        "présent": ["nais", "nais", "naît", "naît", "naissons", "naissez", "naissent"],
        "passé_composé": ["suis né(e)", "es né(e)", "est né(e)", "est né(e)", "sommes né(e)s", "êtes né(e)(s)", "sont né(e)s"],
        "imparfait": ["naissais", "naissais", "naissait", "naissait", "naissions", "naissiez", "naissaient"],
        "futur_simple": ["naîtrai", "naîtras", "naîtra", "naîtra", "naîtrons", "naîtrez", "naîtront"],
        "conditionnel": ["naîtrais", "naîtrais", "naîtrait", "naîtrait", "naîtrions", "naîtriez", "naîtraient"],
        "subjonctif": ["naisse", "naisses", "naisse", "naisse", "naissions", "naissiez", "naissent"]
    },
    "entrer": {
        "translation": "to enter",
        "rank": 50,
        "irregular": False,
        "présent": ["entre", "entres", "entre", "entre", "entrons", "entrez", "entrent"],
        "passé_composé": ["suis entré(e)", "es entré(e)", "est entré(e)", "est entré(e)", "sommes entré(e)s", "êtes entré(e)(s)", "sont entré(e)s"],
        "imparfait": ["entrais", "entrais", "entrait", "entrait", "entrions", "entriez", "entraient"],
        "futur_simple": ["entrerai", "entreras", "entrera", "entrera", "entrerons", "entrerez", "entreront"],
        "conditionnel": ["entrerais", "entrerais", "entrerait", "entrerait", "entrerions", "entreriez", "entreraient"],
        "subjonctif": ["entre", "entres", "entre", "entre", "entrions", "entriez", "entrent"]
    },

    # Top 51-100
    "monter": {
        "translation": "to go up/climb",
        "rank": 51,
        "irregular": False,
        "présent": ["monte", "montes", "monte", "monte", "montons", "montez", "montent"],
        "passé_composé": ["suis monté(e)", "es monté(e)", "est monté(e)", "est monté(e)", "sommes monté(e)s", "êtes monté(e)(s)", "sont monté(e)s"],
        "imparfait": ["montais", "montais", "montait", "montait", "montions", "montiez", "montaient"],
        "futur_simple": ["monterai", "monteras", "montera", "montera", "monterons", "monterez", "monteront"],
        "conditionnel": ["monterais", "monterais", "monterait", "monterait", "monterions", "monteriez", "monteraient"],
        "subjonctif": ["monte", "montes", "monte", "monte", "montions", "montiez", "montent"]
    },
    "descendre": {
        "translation": "to go down",
        "rank": 52,
        "irregular": False,
        "présent": ["descends", "descends", "descend", "descend", "descendons", "descendez", "descendent"],
        "passé_composé": ["suis descendu(e)", "es descendu(e)", "est descendu(e)", "est descendu(e)", "sommes descendu(e)s", "êtes descendu(e)(s)", "sont descendu(e)s"],
        "imparfait": ["descendais", "descendais", "descendait", "descendait", "descendions", "descendiez", "descendaient"],
        "futur_simple": ["descendrai", "descendras", "descendra", "descendra", "descendrons", "descendrez", "descendront"],
        "conditionnel": ["descendrais", "descendrais", "descendrait", "descendrait", "descendrions", "descendriez", "descendraient"],
        "subjonctif": ["descende", "descendes", "descende", "descende", "descendions", "descendiez", "descendent"]
    },
    "tomber": {
        "translation": "to fall",
        "rank": 53,
        "irregular": False,
        "présent": ["tombe", "tombes", "tombe", "tombe", "tombons", "tombez", "tombent"],
        "passé_composé": ["suis tombé(e)", "es tombé(e)", "est tombé(e)", "est tombé(e)", "sommes tombé(e)s", "êtes tombé(e)(s)", "sont tombé(e)s"],
        "imparfait": ["tombais", "tombais", "tombait", "tombait", "tombions", "tombiez", "tombaient"],
        "futur_simple": ["tomberai", "tomberas", "tombera", "tombera", "tomberons", "tomberez", "tomberont"],
        "conditionnel": ["tomberais", "tomberais", "tomberait", "tomberait", "tomberions", "tomberiez", "tomberaient"],
        "subjonctif": ["tombe", "tombes", "tombe", "tombe", "tombions", "tombiez", "tombent"]
    },
    "arriver": {
        "translation": "to arrive",
        "rank": 54,
        "irregular": False,
        "présent": ["arrive", "arrives", "arrive", "arrive", "arrivons", "arrivez", "arrivent"],
        "passé_composé": ["suis arrivé(e)", "es arrivé(e)", "est arrivé(e)", "est arrivé(e)", "sommes arrivé(e)s", "êtes arrivé(e)(s)", "sont arrivé(e)s"],
        "imparfait": ["arrivais", "arrivais", "arrivait", "arrivait", "arrivions", "arriviez", "arrivaient"],
        "futur_simple": ["arriverai", "arriveras", "arrivera", "arrivera", "arriverons", "arriverez", "arriveront"],
        "conditionnel": ["arriverais", "arriverais", "arriverait", "arriverait", "arriverions", "arriveriez", "arriveraient"],
        "subjonctif": ["arrive", "arrives", "arrive", "arrive", "arrivions", "arriviez", "arrivent"]
    },
    "retourner": {
        "translation": "to return",
        "rank": 55,
        "irregular": False,
        "présent": ["retourne", "retournes", "retourne", "retourne", "retournons", "retournez", "retournent"],
        "passé_composé": ["suis retourné(e)", "es retourné(e)", "est retourné(e)", "est retourné(e)", "sommes retourné(e)s", "êtes retourné(e)(s)", "sont retourné(e)s"],
        "imparfait": ["retournais", "retournais", "retournait", "retournait", "retournions", "retourniez", "retournaient"],
        "futur_simple": ["retournerai", "retourneras", "retournera", "retournera", "retournerons", "retournerez", "retourneront"],
        "conditionnel": ["retournerais", "retournerais", "retournerait", "retournerait", "retournerions", "retourneriez", "retourneraient"],
        "subjonctif": ["retourne", "retournes", "retourne", "retourne", "retournions", "retourniez", "retournent"]
    },
    "manger": {
        "translation": "to eat",
        "rank": 56,
        "irregular": False,
        "présent": ["mange", "manges", "mange", "mange", "mangeons", "mangez", "mangent"],
        "passé_composé": ["ai mangé", "as mangé", "a mangé", "a mangé", "avons mangé", "avez mangé", "ont mangé"],
        "imparfait": ["mangeais", "mangeais", "mangeait", "mangeait", "mangions", "mangiez", "mangeaient"],
        "futur_simple": ["mangerai", "mangeras", "mangera", "mangera", "mangerons", "mangerez", "mangeront"],
        "conditionnel": ["mangerais", "mangerais", "mangerait", "mangerait", "mangerions", "mangeriez", "mangeraient"],
        "subjonctif": ["mange", "manges", "mange", "mange", "mangions", "mangiez", "mangent"]
    },
    "jouer": {
        "translation": "to play",
        "rank": 57,
        "irregular": False,
        "présent": ["joue", "joues", "joue", "joue", "jouons", "jouez", "jouent"],
        "passé_composé": ["ai joué", "as joué", "a joué", "a joué", "avons joué", "avez joué", "ont joué"],
        "imparfait": ["jouais", "jouais", "jouait", "jouait", "jouions", "jouiez", "jouaient"],
        "futur_simple": ["jouerai", "joueras", "jouera", "jouera", "jouerons", "jouerez", "joueront"],
        "conditionnel": ["jouerais", "jouerais", "jouerait", "jouerait", "jouerions", "joueriez", "joueraient"],
        "subjonctif": ["joue", "joues", "joue", "joue", "jouions", "jouiez", "jouent"]
    },
    "travailler": {
        "translation": "to work",
        "rank": 58,
        "irregular": False,
        "présent": ["travaille", "travailles", "travaille", "travaille", "travaillons", "travaillez", "travaillent"],
        "passé_composé": ["ai travaillé", "as travaillé", "a travaillé", "a travaillé", "avons travaillé", "avez travaillé", "ont travaillé"],
        "imparfait": ["travaillais", "travaillais", "travaillait", "travaillait", "travaillions", "travailliez", "travaillaient"],
        "futur_simple": ["travaillerai", "travailleras", "travaillera", "travaillera", "travaillerons", "travaillerez", "travailleront"],
        "conditionnel": ["travaillerais", "travaillerais", "travaillerait", "travaillerait", "travaillerions", "travailleriez", "travailleraient"],
        "subjonctif": ["travaille", "travailles", "travaille", "travaille", "travaillions", "travailliez", "travaillent"]
    },
    "acheter": {
        "translation": "to buy",
        "rank": 59,
        "irregular": False,
        "présent": ["achète", "achètes", "achète", "achète", "achetons", "achetez", "achètent"],
        "passé_composé": ["ai acheté", "as acheté", "a acheté", "a acheté", "avons acheté", "avez acheté", "ont acheté"],
        "imparfait": ["achetais", "achetais", "achetait", "achetait", "achetions", "achetiez", "achetaient"],
        "futur_simple": ["achèterai", "achèteras", "achètera", "achètera", "achèterons", "achèterez", "achèteront"],
        "conditionnel": ["achèterais", "achèterais", "achèterait", "achèterait", "achèterions", "achèteriez", "achèteraient"],
        "subjonctif": ["achète", "achètes", "achète", "achète", "achetions", "achetiez", "achètent"]
    },
    "vendre": {
        "translation": "to sell",
        "rank": 60,
        "irregular": False,
        "présent": ["vends", "vends", "vend", "vend", "vendons", "vendez", "vendent"],
        "passé_composé": ["ai vendu", "as vendu", "a vendu", "a vendu", "avons vendu", "avez vendu", "ont vendu"],
        "imparfait": ["vendais", "vendais", "vendait", "vendait", "vendions", "vendiez", "vendaient"],
        "futur_simple": ["vendrai", "vendras", "vendra", "vendra", "vendrons", "vendrez", "vendront"],
        "conditionnel": ["vendrais", "vendrais", "vendrait", "vendrait", "vendrions", "vendriez", "vendraient"],
        "subjonctif": ["vende", "vendes", "vende", "vende", "vendions", "vendiez", "vendent"]
    },
    "finir": {
        "translation": "to finish",
        "rank": 61,
        "irregular": False,
        "présent": ["finis", "finis", "finit", "finit", "finissons", "finissez", "finissent"],
        "passé_composé": ["ai fini", "as fini", "a fini", "a fini", "avons fini", "avez fini", "ont fini"],
        "imparfait": ["finissais", "finissais", "finissait", "finissait", "finissions", "finissiez", "finissaient"],
        "futur_simple": ["finirai", "finiras", "finira", "finira", "finirons", "finirez", "finiront"],
        "conditionnel": ["finirais", "finirais", "finirait", "finirait", "finirions", "finiriez", "finiraient"],
        "subjonctif": ["finisse", "finisses", "finisse", "finisse", "finissions", "finissiez", "finissent"]
    },
    "choisir": {
        "translation": "to choose",
        "rank": 62,
        "irregular": False,
        "présent": ["choisis", "choisis", "choisit", "choisit", "choisissons", "choisissez", "choisissent"],
        "passé_composé": ["ai choisi", "as choisi", "a choisi", "a choisi", "avons choisi", "avez choisi", "ont choisi"],
        "imparfait": ["choisissais", "choisissais", "choisissait", "choisissait", "choisissions", "choisissiez", "choisissaient"],
        "futur_simple": ["choisirai", "choisiras", "choisira", "choisira", "choisirons", "choisirez", "choisiront"],
        "conditionnel": ["choisirais", "choisirais", "choisirait", "choisirait", "choisirions", "choisiriez", "choisiraient"],
        "subjonctif": ["choisisse", "choisisses", "choisisse", "choisisse", "choisissions", "choisissiez", "choisissent"]
    },
    "réussir": {
        "translation": "to succeed",
        "rank": 63,
        "irregular": False,
        "présent": ["réussis", "réussis", "réussit", "réussit", "réussissons", "réussissez", "réussissent"],
        "passé_composé": ["ai réussi", "as réussi", "a réussi", "a réussi", "avons réussi", "avez réussi", "ont réussi"],
        "imparfait": ["réussissais", "réussissais", "réussissait", "réussissait", "réussissions", "réussissiez", "réussissaient"],
        "futur_simple": ["réussirai", "réussiras", "réussira", "réussira", "réussirons", "réussirez", "réussiront"],
        "conditionnel": ["réussirais", "réussirais", "réussirait", "réussirait", "réussirions", "réussiriez", "réussiraient"],
        "subjonctif": ["réussisse", "réussisses", "réussisse", "réussisse", "réussissions", "réussissiez", "réussissent"]
    },
    "remplir": {
        "translation": "to fill",
        "rank": 64,
        "irregular": False,
        "présent": ["remplis", "remplis", "remplit", "remplit", "remplissons", "remplissez", "remplissent"],
        "passé_composé": ["ai rempli", "as rempli", "a rempli", "a rempli", "avons rempli", "avez rempli", "ont rempli"],
        "imparfait": ["remplissais", "remplissais", "remplissait", "remplissait", "remplissions", "remplissiez", "remplissaient"],
        "futur_simple": ["remplirai", "rempliras", "remplira", "remplira", "remplirons", "remplirez", "rempliront"],
        "conditionnel": ["remplirais", "remplirais", "remplirait", "remplirait", "remplirions", "rempliriez", "rempliraient"],
        "subjonctif": ["remplisse", "remplisses", "remplisse", "remplisse", "remplissions", "remplissiez", "remplissent"]
    },
    "offrir": {
        "translation": "to offer/give",
        "rank": 65,
        "irregular": True,
        "présent": ["offre", "offres", "offre", "offre", "offrons", "offrez", "offrent"],
        "passé_composé": ["ai offert", "as offert", "a offert", "a offert", "avons offert", "avez offert", "ont offert"],
        "imparfait": ["offrais", "offrais", "offrait", "offrait", "offrions", "offriez", "offraient"],
        "futur_simple": ["offrirai", "offriras", "offrira", "offrira", "offrirons", "offrirez", "offriront"],
        "conditionnel": ["offrirais", "offrirais", "offrirait", "offrirait", "offririons", "offririez", "offriraient"],
        "subjonctif": ["offre", "offres", "offre", "offre", "offrions", "offriez", "offrent"]
    },
    "couvrir": {
        "translation": "to cover",
        "rank": 66,
        "irregular": True,
        "présent": ["couvre", "couvres", "couvre", "couvre", "couvrons", "couvrez", "couvrent"],
        "passé_composé": ["ai couvert", "as couvert", "a couvert", "a couvert", "avons couvert", "avez couvert", "ont couvert"],
        "imparfait": ["couvrais", "couvrais", "couvrait", "couvrait", "couvrions", "couvriez", "couvraient"],
        "futur_simple": ["couvrirai", "couvriras", "couvrira", "couvrira", "couvrirons", "couvrirez", "couvriront"],
        "conditionnel": ["couvrirais", "couvrirais", "couvrirait", "couvrirait", "couvririons", "couvririez", "couvriraient"],
        "subjonctif": ["couvre", "couvres", "couvre", "couvre", "couvrions", "couvriez", "couvrent"]
    },
    "apprendre": {
        "translation": "to learn",
        "rank": 67,
        "irregular": True,
        "présent": ["apprends", "apprends", "apprend", "apprend", "apprenons", "apprenez", "apprennent"],
        "passé_composé": ["ai appris", "as appris", "a appris", "a appris", "avons appris", "avez appris", "ont appris"],
        "imparfait": ["apprenais", "apprenais", "apprenait", "apprenait", "apprenions", "appreniez", "apprenaient"],
        "futur_simple": ["apprendrai", "apprendras", "apprendra", "apprendra", "apprendrons", "apprendrez", "apprendront"],
        "conditionnel": ["apprendrais", "apprendrais", "apprendrait", "apprendrait", "apprendrions", "apprendriez", "apprendraient"],
        "subjonctif": ["apprenne", "apprennes", "apprenne", "apprenne", "apprenions", "appreniez", "apprennent"]
    },
    "permettre": {
        "translation": "to allow",
        "rank": 68,
        "irregular": True,
        "présent": ["permets", "permets", "permet", "permet", "permettons", "permettez", "permettent"],
        "passé_composé": ["ai permis", "as permis", "a permis", "a permis", "avons permis", "avez permis", "ont permis"],
        "imparfait": ["permettais", "permettais", "permettait", "permettait", "permettions", "permettiez", "permettaient"],
        "futur_simple": ["permettrai", "permettras", "permettra", "permettra", "permettrons", "permettrez", "permettront"],
        "conditionnel": ["permettrais", "permettrais", "permettrait", "permettrait", "permettrions", "permettriez", "permettraient"],
        "subjonctif": ["permette", "permettes", "permette", "permette", "permettions", "permettiez", "permettent"]
    },
    "promettre": {
        "translation": "to promise",
        "rank": 69,
        "irregular": True,
        "présent": ["promets", "promets", "promet", "promet", "promettons", "promettez", "promettent"],
        "passé_composé": ["ai promis", "as promis", "a promis", "a promis", "avons promis", "avez promis", "ont promis"],
        "imparfait": ["promettais", "promettais", "promettait", "promettait", "promettions", "promettiez", "promettaient"],
        "futur_simple": ["promettrai", "promettras", "promettra", "promettra", "promettrons", "promettrez", "promettront"],
        "conditionnel": ["promettrais", "promettrais", "promettrait", "promettrait", "promettrions", "promettriez", "promettraient"],
        "subjonctif": ["promette", "promettes", "promette", "promette", "promettions", "promettiez", "promettent"]
    },
    "battre": {
        "translation": "to beat",
        "rank": 70,
        "irregular": True,
        "présent": ["bats", "bats", "bat", "bat", "battons", "battez", "battent"],
        "passé_composé": ["ai battu", "as battu", "a battu", "a battu", "avons battu", "avez battu", "ont battu"],
        "imparfait": ["battais", "battais", "battait", "battait", "battions", "battiez", "battaient"],
        "futur_simple": ["battrai", "battras", "battra", "battra", "battrons", "battrez", "battront"],
        "conditionnel": ["battrais", "battrais", "battrait", "battrait", "battrions", "battriez", "battraient"],
        "subjonctif": ["batte", "battes", "batte", "batte", "battions", "battiez", "battent"]
    },
    "conduire": {
        "translation": "to drive",
        "rank": 71,
        "irregular": True,
        "présent": ["conduis", "conduis", "conduit", "conduit", "conduisons", "conduisez", "conduisent"],
        "passé_composé": ["ai conduit", "as conduit", "a conduit", "a conduit", "avons conduit", "avez conduit", "ont conduit"],
        "imparfait": ["conduisais", "conduisais", "conduisait", "conduisait", "conduisions", "conduisiez", "conduisaient"],
        "futur_simple": ["conduirai", "conduiras", "conduira", "conduira", "conduirons", "conduirez", "conduiront"],
        "conditionnel": ["conduirais", "conduirais", "conduirait", "conduirait", "conduirions", "conduiriez", "conduiraient"],
        "subjonctif": ["conduise", "conduises", "conduise", "conduise", "conduisions", "conduisiez", "conduisent"]
    },
    "produire": {
        "translation": "to produce",
        "rank": 72,
        "irregular": True,
        "présent": ["produis", "produis", "produit", "produit", "produisons", "produisez", "produisent"],
        "passé_composé": ["ai produit", "as produit", "a produit", "a produit", "avons produit", "avez produit", "ont produit"],
        "imparfait": ["produisais", "produisais", "produisait", "produisait", "produisions", "produisiez", "produisaient"],
        "futur_simple": ["produirai", "produiras", "produira", "produira", "produirons", "produirez", "produiront"],
        "conditionnel": ["produirais", "produirais", "produirait", "produirait", "produirions", "produiriez", "produiraient"],
        "subjonctif": ["produise", "produises", "produise", "produise", "produisions", "produisiez", "produisent"]
    },
    "construire": {
        "translation": "to build",
        "rank": 73,
        "irregular": True,
        "présent": ["construis", "construis", "construit", "construit", "construisons", "construisez", "construisent"],
        "passé_composé": ["ai construit", "as construit", "a construit", "a construit", "avons construit", "avez construit", "ont construit"],
        "imparfait": ["construisais", "construisais", "construisait", "construisait", "construisions", "construisiez", "construisaient"],
        "futur_simple": ["construirai", "construiras", "construira", "construira", "construirons", "construirez", "construiront"],
        "conditionnel": ["construirais", "construirais", "construirait", "construirait", "construirions", "construiriez", "construiraient"],
        "subjonctif": ["construise", "construises", "construise", "construise", "construisions", "construisiez", "construisent"]
    },
    "détruire": {
        "translation": "to destroy",
        "rank": 74,
        "irregular": True,
        "présent": ["détruis", "détruis", "détruit", "détruit", "détruisons", "détruisez", "détruisent"],
        "passé_composé": ["ai détruit", "as détruit", "a détruit", "a détruit", "avons détruit", "avez détruit", "ont détruit"],
        "imparfait": ["détruisais", "détruisais", "détruisait", "détruisait", "détruisions", "détruisiez", "détruisaient"],
        "futur_simple": ["détruirai", "détruiras", "détruira", "détruira", "détruirons", "détruirez", "détruiront"],
        "conditionnel": ["détruirais", "détruirais", "détruirait", "détruirait", "détruirions", "détruiriez", "détruiraient"],
        "subjonctif": ["détruise", "détruises", "détruise", "détruise", "détruisions", "détruisiez", "détruisent"]
    },
    "traduire": {
        "translation": "to translate",
        "rank": 75,
        "irregular": True,
        "présent": ["traduis", "traduis", "traduit", "traduit", "traduisons", "traduisez", "traduisent"],
        "passé_composé": ["ai traduit", "as traduit", "a traduit", "a traduit", "avons traduit", "avez traduit", "ont traduit"],
        "imparfait": ["traduisais", "traduisais", "traduisait", "traduisait", "traduisions", "traduisiez", "traduisaient"],
        "futur_simple": ["traduirai", "traduiras", "traduira", "traduira", "traduirons", "traduirez", "traduiront"],
        "conditionnel": ["traduirais", "traduirais", "traduirait", "traduirait", "traduirions", "traduiriez", "traduiraient"],
        "subjonctif": ["traduise", "traduises", "traduise", "traduise", "traduisions", "traduisiez", "traduisent"]
    },
    "rire": {
        "translation": "to laugh",
        "rank": 76,
        "irregular": True,
        "présent": ["ris", "ris", "rit", "rit", "rions", "riez", "rient"],
        "passé_composé": ["ai ri", "as ri", "a ri", "a ri", "avons ri", "avez ri", "ont ri"],
        "imparfait": ["riais", "riais", "riait", "riait", "riions", "riiez", "riaient"],
        "futur_simple": ["rirai", "riras", "rira", "rira", "rirons", "rirez", "riront"],
        "conditionnel": ["rirais", "rirais", "rirait", "rirait", "ririons", "ririez", "riraient"],
        "subjonctif": ["rie", "ries", "rie", "rie", "riions", "riiez", "rient"]
    },
    "sourire": {
        "translation": "to smile",
        "rank": 77,
        "irregular": True,
        "présent": ["souris", "souris", "sourit", "sourit", "sourions", "souriez", "sourient"],
        "passé_composé": ["ai souri", "as souri", "a souri", "a souri", "avons souri", "avez souri", "ont souri"],
        "imparfait": ["souriais", "souriais", "souriait", "souriait", "souriions", "souriiez", "souriaient"],
        "futur_simple": ["sourirai", "souriras", "sourira", "sourira", "sourirons", "sourirez", "souriront"],
        "conditionnel": ["sourirais", "sourirais", "sourirait", "sourirait", "souririons", "souririez", "souriraient"],
        "subjonctif": ["sourie", "souries", "sourie", "sourie", "souriions", "souriiez", "sourient"]
    },
    "plaire": {
        "translation": "to please",
        "rank": 78,
        "irregular": True,
        "présent": ["plais", "plais", "plaît", "plaît", "plaisons", "plaisez", "plaisent"],
        "passé_composé": ["ai plu", "as plu", "a plu", "a plu", "avons plu", "avez plu", "ont plu"],
        "imparfait": ["plaisais", "plaisais", "plaisait", "plaisait", "plaisions", "plaisiez", "plaisaient"],
        "futur_simple": ["plairai", "plairas", "plaira", "plaira", "plairons", "plairez", "plairont"],
        "conditionnel": ["plairais", "plairais", "plairait", "plairait", "plairions", "plairiez", "plairaient"],
        "subjonctif": ["plaise", "plaises", "plaise", "plaise", "plaisions", "plaisiez", "plaisent"]
    },
    "craindre": {
        "translation": "to fear",
        "rank": 79,
        "irregular": True,
        "présent": ["crains", "crains", "craint", "craint", "craignons", "craignez", "craignent"],
        "passé_composé": ["ai craint", "as craint", "a craint", "a craint", "avons craint", "avez craint", "ont craint"],
        "imparfait": ["craignais", "craignais", "craignait", "craignait", "craignions", "craigniez", "craignaient"],
        "futur_simple": ["craindrai", "craindras", "craindra", "craindra", "craindrons", "craindrez", "craindront"],
        "conditionnel": ["craindrais", "craindrais", "craindrait", "craindrait", "craindrions", "craindriez", "craindraient"],
        "subjonctif": ["craigne", "craignes", "craigne", "craigne", "craignions", "craigniez", "craignent"]
    },
    "peindre": {
        "translation": "to paint",
        "rank": 80,
        "irregular": True,
        "présent": ["peins", "peins", "peint", "peint", "peignons", "peignez", "peignent"],
        "passé_composé": ["ai peint", "as peint", "a peint", "a peint", "avons peint", "avez peint", "ont peint"],
        "imparfait": ["peignais", "peignais", "peignait", "peignait", "peignions", "peigniez", "peignaient"],
        "futur_simple": ["peindrai", "peindras", "peindra", "peindra", "peindrons", "peindrez", "peindront"],
        "conditionnel": ["peindrais", "peindrais", "peindrait", "peindrait", "peindrions", "peindriez", "peindraient"],
        "subjonctif": ["peigne", "peignes", "peigne", "peigne", "peignions", "peigniez", "peignent"]
    },
    "rejoindre": {
        "translation": "to join/meet",
        "rank": 81,
        "irregular": True,
        "présent": ["rejoins", "rejoins", "rejoint", "rejoint", "rejoignons", "rejoignez", "rejoignent"],
        "passé_composé": ["ai rejoint", "as rejoint", "a rejoint", "a rejoint", "avons rejoint", "avez rejoint", "ont rejoint"],
        "imparfait": ["rejoignais", "rejoignais", "rejoignait", "rejoignait", "rejoignions", "rejoigniez", "rejoignaient"],
        "futur_simple": ["rejoindrai", "rejoindras", "rejoindra", "rejoindra", "rejoindrons", "rejoindrez", "rejoindront"],
        "conditionnel": ["rejoindrais", "rejoindrais", "rejoindrait", "rejoindrait", "rejoindrions", "rejoindriez", "rejoindraient"],
        "subjonctif": ["rejoigne", "rejoignes", "rejoigne", "rejoigne", "rejoignions", "rejoigniez", "rejoignent"]
    },
    "atteindre": {
        "translation": "to reach",
        "rank": 82,
        "irregular": True,
        "présent": ["atteins", "atteins", "atteint", "atteint", "atteignons", "atteignez", "atteignent"],
        "passé_composé": ["ai atteint", "as atteint", "a atteint", "a atteint", "avons atteint", "avez atteint", "ont atteint"],
        "imparfait": ["atteignais", "atteignais", "atteignait", "atteignait", "atteignions", "atteigniez", "atteignaient"],
        "futur_simple": ["atteindrai", "atteindras", "atteindra", "atteindra", "atteindrons", "atteindrez", "atteindront"],
        "conditionnel": ["atteindrais", "atteindrais", "atteindrait", "atteindrait", "atteindrions", "atteindriez", "atteindraient"],
        "subjonctif": ["atteigne", "atteignes", "atteigne", "atteigne", "atteignions", "atteigniez", "atteignent"]
    },
    "éteindre": {
        "translation": "to turn off/extinguish",
        "rank": 83,
        "irregular": True,
        "présent": ["éteins", "éteins", "éteint", "éteint", "éteignons", "éteignez", "éteignent"],
        "passé_composé": ["ai éteint", "as éteint", "a éteint", "a éteint", "avons éteint", "avez éteint", "ont éteint"],
        "imparfait": ["éteignais", "éteignais", "éteignait", "éteignait", "éteignions", "éteigniez", "éteignaient"],
        "futur_simple": ["éteindrai", "éteindras", "éteindra", "éteindra", "éteindrons", "éteindrez", "éteindront"],
        "conditionnel": ["éteindrais", "éteindrais", "éteindrait", "éteindrait", "éteindrions", "éteindriez", "éteindraient"],
        "subjonctif": ["éteigne", "éteignes", "éteigne", "éteigne", "éteignions", "éteigniez", "éteignent"]
    },
    "résoudre": {
        "translation": "to solve",
        "rank": 84,
        "irregular": True,
        "présent": ["résous", "résous", "résout", "résout", "résolvons", "résolvez", "résolvent"],
        "passé_composé": ["ai résolu", "as résolu", "a résolu", "a résolu", "avons résolu", "avez résolu", "ont résolu"],
        "imparfait": ["résolvais", "résolvais", "résolvait", "résolvait", "résolvions", "résolviez", "résolvaient"],
        "futur_simple": ["résoudrai", "résoudras", "résoudra", "résoudra", "résoudrons", "résoudrez", "résoudront"],
        "conditionnel": ["résoudrais", "résoudrais", "résoudrait", "résoudrait", "résoudrions", "résoudriez", "résoudraient"],
        "subjonctif": ["résolve", "résolves", "résolve", "résolve", "résolvions", "résolviez", "résolvent"]
    },
    "coudre": {
        "translation": "to sew",
        "rank": 85,
        "irregular": True,
        "présent": ["couds", "couds", "coud", "coud", "cousons", "cousez", "cousent"],
        "passé_composé": ["ai cousu", "as cousu", "a cousu", "a cousu", "avons cousu", "avez cousu", "ont cousu"],
        "imparfait": ["cousais", "cousais", "cousait", "cousait", "cousions", "cousiez", "cousaient"],
        "futur_simple": ["coudrai", "coudras", "coudra", "coudra", "coudrons", "coudrez", "coudront"],
        "conditionnel": ["coudrais", "coudrais", "coudrait", "coudrait", "coudrions", "coudriez", "coudraient"],
        "subjonctif": ["couse", "couses", "couse", "couse", "cousions", "cousiez", "cousent"]
    },
    "moudre": {
        "translation": "to grind",
        "rank": 86,
        "irregular": True,
        "présent": ["mouds", "mouds", "moud", "moud", "moulons", "moulez", "moulent"],
        "passé_composé": ["ai moulu", "as moulu", "a moulu", "a moulu", "avons moulu", "avez moulu", "ont moulu"],
        "imparfait": ["moulais", "moulais", "moulait", "moulait", "moulions", "mouliez", "moulaient"],
        "futur_simple": ["moudrai", "moudras", "moudra", "moudra", "moudrons", "moudrez", "moudront"],
        "conditionnel": ["moudrais", "moudrais", "moudrait", "moudrait", "moudrions", "moudriez", "moudraient"],
        "subjonctif": ["moule", "moules", "moule", "moule", "moulions", "mouliez", "moulent"]
    },
    "valoir": {
        "translation": "to be worth",
        "rank": 87,
        "irregular": True,
        "présent": ["vaux", "vaux", "vaut", "vaut", "valons", "valez", "valent"],
        "passé_composé": ["ai valu", "as valu", "a valu", "a valu", "avons valu", "avez valu", "ont valu"],
        "imparfait": ["valais", "valais", "valait", "valait", "valions", "valiez", "valaient"],
        "futur_simple": ["vaudrai", "vaudras", "vaudra", "vaudra", "vaudrons", "vaudrez", "vaudront"],
        "conditionnel": ["vaudrais", "vaudrais", "vaudrait", "vaudrait", "vaudrions", "vaudriez", "vaudraient"],
        "subjonctif": ["vaille", "vailles", "vaille", "vaille", "valions", "valiez", "vaillent"]
    },
    "asseoir": {
        "translation": "to sit",
        "rank": 88,
        "irregular": True,
        "présent": ["assieds", "assieds", "assied", "assied", "asseyons", "asseyez", "asseyent"],
        "passé_composé": ["ai assis", "as assis", "a assis", "a assis", "avons assis", "avez assis", "ont assis"],
        "imparfait": ["asseyais", "asseyais", "asseyait", "asseyait", "asseyions", "asseyiez", "asseyaient"],
        "futur_simple": ["assiérai", "assiéras", "assiéra", "assiéra", "assiérons", "assiérez", "assiéront"],
        "conditionnel": ["assiérais", "assiérais", "assiérait", "assiérait", "assiérions", "assiériez", "assiéraient"],
        "subjonctif": ["asseye", "asseyes", "asseye", "asseye", "asseyions", "asseyiez", "asseyent"]
    },
    "pleuvoir": {
        "translation": "to rain",
        "rank": 89,
        "irregular": True,
        "présent": ["-", "-", "pleut", "pleut", "-", "-", "-"],
        "passé_composé": ["-", "-", "a plu", "a plu", "-", "-", "-"],
        "imparfait": ["-", "-", "pleuvait", "pleuvait", "-", "-", "-"],
        "futur_simple": ["-", "-", "pleuvra", "pleuvra", "-", "-", "-"],
        "conditionnel": ["-", "-", "pleuvrait", "pleuvrait", "-", "-", "-"],
        "subjonctif": ["-", "-", "pleuve", "pleuve", "-", "-", "-"]
    },
    "apparaître": {
        "translation": "to appear",
        "rank": 90,
        "irregular": True,
        "présent": ["apparais", "apparais", "apparaît", "apparaît", "apparaissons", "apparaissez", "apparaissent"],
        "passé_composé": ["ai apparu", "as apparu", "a apparu", "a apparu", "avons apparu", "avez apparu", "ont apparu"],
        "imparfait": ["apparaissais", "apparaissais", "apparaissait", "apparaissait", "apparaissions", "apparaissiez", "apparaissaient"],
        "futur_simple": ["apparaîtrai", "apparaîtras", "apparaîtra", "apparaîtra", "apparaîtrons", "apparaîtrez", "apparaîtront"],
        "conditionnel": ["apparaîtrais", "apparaîtrais", "apparaîtrait", "apparaîtrait", "apparaîtrions", "apparaîtriez", "apparaîtraient"],
        "subjonctif": ["apparaisse", "apparaisses", "apparaisse", "apparaisse", "apparaissions", "apparaissiez", "apparaissent"]
    },
    "disparaître": {
        "translation": "to disappear",
        "rank": 91,
        "irregular": True,
        "présent": ["disparais", "disparais", "disparaît", "disparaît", "disparaissons", "disparaissez", "disparaissent"],
        "passé_composé": ["ai disparu", "as disparu", "a disparu", "a disparu", "avons disparu", "avez disparu", "ont disparu"],
        "imparfait": ["disparaissais", "disparaissais", "disparaissait", "disparaissait", "disparaissions", "disparaissiez", "disparaissaient"],
        "futur_simple": ["disparaîtrai", "disparaîtras", "disparaîtra", "disparaîtra", "disparaîtrons", "disparaîtrez", "disparaîtront"],
        "conditionnel": ["disparaîtrais", "disparaîtrais", "disparaîtrait", "disparaîtrait", "disparaîtrions", "disparaîtriez", "disparaîtraient"],
        "subjonctif": ["disparaisse", "disparaisses", "disparaisse", "disparaisse", "disparaissions", "disparaissiez", "disparaissent"]
    },
    "paraître": {
        "translation": "to seem/appear",
        "rank": 92,
        "irregular": True,
        "présent": ["parais", "parais", "paraît", "paraît", "paraissons", "paraissez", "paraissent"],
        "passé_composé": ["ai paru", "as paru", "a paru", "a paru", "avons paru", "avez paru", "ont paru"],
        "imparfait": ["paraissais", "paraissais", "paraissait", "paraissait", "paraissions", "paraissiez", "paraissaient"],
        "futur_simple": ["paraîtrai", "paraîtras", "paraîtra", "paraîtra", "paraîtrons", "paraîtrez", "paraîtront"],
        "conditionnel": ["paraîtrais", "paraîtrais", "paraîtrait", "paraîtrait", "paraîtrions", "paraîtriez", "paraîtraient"],
        "subjonctif": ["paraisse", "paraisses", "paraisse", "paraisse", "paraissions", "paraissiez", "paraissent"]
    },
    "croître": {
        "translation": "to grow",
        "rank": 93,
        "irregular": True,
        "présent": ["croîs", "croîs", "croît", "croît", "croissons", "croissez", "croissent"],
        "passé_composé": ["ai crû", "as crû", "a crû", "a crû", "avons crû", "avez crû", "ont crû"],
        "imparfait": ["croissais", "croissais", "croissait", "croissait", "croissions", "croissiez", "croissaient"],
        "futur_simple": ["croîtrai", "croîtras", "croîtra", "croîtra", "croîtrons", "croîtrez", "croîtront"],
        "conditionnel": ["croîtrais", "croîtrais", "croîtrait", "croîtrait", "croîtrions", "croîtriez", "croîtraient"],
        "subjonctif": ["croisse", "croisses", "croisse", "croisse", "croissions", "croissiez", "croissent"]
    },
    "vaincre": {
        "translation": "to defeat",
        "rank": 94,
        "irregular": True,
        "présent": ["vaincs", "vaincs", "vainc", "vainc", "vainquons", "vainquez", "vainquent"],
        "passé_composé": ["ai vaincu", "as vaincu", "a vaincu", "a vaincu", "avons vaincu", "avez vaincu", "ont vaincu"],
        "imparfait": ["vainquais", "vainquais", "vainquait", "vainquait", "vainquions", "vainquiez", "vainquaient"],
        "futur_simple": ["vaincrai", "vaincras", "vaincra", "vaincra", "vaincrons", "vaincrez", "vaincront"],
        "conditionnel": ["vaincrais", "vaincrais", "vaincrait", "vaincrait", "vaincrions", "vaincriez", "vaincraient"],
        "subjonctif": ["vainque", "vainques", "vainque", "vainque", "vainquions", "vainquiez", "vainquent"]
    },
    "convaincre": {
        "translation": "to convince",
        "rank": 95,
        "irregular": True,
        "présent": ["convaincs", "convaincs", "convainc", "convainc", "convainquons", "convainquez", "convainquent"],
        "passé_composé": ["ai convaincu", "as convaincu", "a convaincu", "a convaincu", "avons convaincu", "avez convaincu", "ont convaincu"],
        "imparfait": ["convainquais", "convainquais", "convainquait", "convainquait", "convainquions", "convainquiez", "convainquaient"],
        "futur_simple": ["convaincrai", "convaincras", "convaincra", "convaincra", "convaincrons", "convaincrez", "convaincront"],
        "conditionnel": ["convaincrais", "convaincrais", "convaincrait", "convaincrait", "convaincrions", "convaincriez", "convaincraient"],
        "subjonctif": ["convainque", "convainques", "convainque", "convainque", "convainquions", "convainquiez", "convainquent"]
    },
    "haïr": {
        "translation": "to hate",
        "rank": 96,
        "irregular": True,
        "présent": ["hais", "hais", "hait", "hait", "haïssons", "haïssez", "haïssent"],
        "passé_composé": ["ai haï", "as haï", "a haï", "a haï", "avons haï", "avez haï", "ont haï"],
        "imparfait": ["haïssais", "haïssais", "haïssait", "haïssait", "haïssions", "haïssiez", "haïssaient"],
        "futur_simple": ["haïrai", "haïras", "haïra", "haïra", "haïrons", "haïrez", "haïront"],
        "conditionnel": ["haïrais", "haïrais", "haïrait", "haïrait", "haïrions", "haïriez", "haïraient"],
        "subjonctif": ["haïsse", "haïsses", "haïsse", "haïsse", "haïssions", "haïssiez", "haïssent"]
    },
    "fuir": {
        "translation": "to flee",
        "rank": 97,
        "irregular": True,
        "présent": ["fuis", "fuis", "fuit", "fuit", "fuyons", "fuyez", "fuient"],
        "passé_composé": ["ai fui", "as fui", "a fui", "a fui", "avons fui", "avez fui", "ont fui"],
        "imparfait": ["fuyais", "fuyais", "fuyait", "fuyait", "fuyions", "fuyiez", "fuyaient"],
        "futur_simple": ["fuirai", "fuiras", "fuira", "fuira", "fuirons", "fuirez", "fuiront"],
        "conditionnel": ["fuirais", "fuirais", "fuirait", "fuirait", "fuirions", "fuiriez", "fuiraient"],
        "subjonctif": ["fuie", "fuies", "fuie", "fuie", "fuyions", "fuyiez", "fuient"]
    },
    "acquérir": {
        "translation": "to acquire",
        "rank": 98,
        "irregular": True,
        "présent": ["acquiers", "acquiers", "acquiert", "acquiert", "acquérons", "acquérez", "acquièrent"],
        "passé_composé": ["ai acquis", "as acquis", "a acquis", "a acquis", "avons acquis", "avez acquis", "ont acquis"],
        "imparfait": ["acquérais", "acquérais", "acquérait", "acquérait", "acquérions", "acquériez", "acquéraient"],
        "futur_simple": ["acquerrai", "acquerras", "acquerra", "acquerra", "acquerrons", "acquerrez", "acquerront"],
        "conditionnel": ["acquerrais", "acquerrais", "acquerrait", "acquerrait", "acquerrions", "acquerriez", "acquerraient"],
        "subjonctif": ["acquière", "acquières", "acquière", "acquière", "acquérions", "acquériez", "acquièrent"]
    },
    "cueillir": {
        "translation": "to pick/gather",
        "rank": 99,
        "irregular": True,
        "présent": ["cueille", "cueilles", "cueille", "cueille", "cueillons", "cueillez", "cueillent"],
        "passé_composé": ["ai cueilli", "as cueilli", "a cueilli", "a cueilli", "avons cueilli", "avez cueilli", "ont cueilli"],
        "imparfait": ["cueillais", "cueillais", "cueillait", "cueillait", "cueillions", "cueilliez", "cueillaient"],
        "futur_simple": ["cueillerai", "cueilleras", "cueillera", "cueillera", "cueillerons", "cueillerez", "cueilleront"],
        "conditionnel": ["cueillerais", "cueillerais", "cueillerait", "cueillerait", "cueillerions", "cueilleriez", "cueilleraient"],
        "subjonctif": ["cueille", "cueilles", "cueille", "cueille", "cueillions", "cueilliez", "cueillent"]
    },
    "bouillir": {
        "translation": "to boil",
        "rank": 100,
        "irregular": True,
        "présent": ["bous", "bous", "bout", "bout", "bouillons", "bouillez", "bouillent"],
        "passé_composé": ["ai bouilli", "as bouilli", "a bouilli", "a bouilli", "avons bouilli", "avez bouilli", "ont bouilli"],
        "imparfait": ["bouillais", "bouillais", "bouillait", "bouillait", "bouillions", "bouilliez", "bouillaient"],
        "futur_simple": ["bouillirai", "bouilliras", "bouillira", "bouillira", "bouillirons", "bouillirez", "bouilliront"],
        "conditionnel": ["bouillirais", "bouillirais", "bouillirait", "bouillirait", "bouillirions", "bouilliriez", "bouilliraient"],
        "subjonctif": ["bouille", "bouilles", "bouille", "bouille", "bouillions", "bouilliez", "bouillent"]
    }
}


def get_conjugation(verb, tense, pronoun_index):
    """Get a specific conjugation."""
    if verb in VERBS and tense in VERBS[verb]:
        return VERBS[verb][tense][pronoun_index]
    return None


def get_all_verbs():
    """Return list of all verb infinitives."""
    return list(VERBS.keys())


def get_verb_translation(verb):
    """Get English translation of a verb."""
    return VERBS.get(verb, {}).get("translation", "")


def get_verbs_by_rank(max_rank):
    """Get verbs up to a certain rank."""
    return [v for v, data in VERBS.items() if data.get("rank", 999) <= max_rank]


def get_irregular_verbs(max_rank=None):
    """Get irregular verbs, optionally filtered by rank."""
    verbs = [v for v, data in VERBS.items() if data.get("irregular", False)]
    if max_rank:
        verbs = [v for v in verbs if VERBS[v].get("rank", 999) <= max_rank]
    return verbs
