import random
from citazioni import citazioni


# frasi rare (appaiono molto raramente)
frasi_speciali = [
    "Anche oggi basta 1 mm.",
    "Un passo piccolo è ancora un passo.",
    "A volte continuare è già abbastanza.",
    "Anche restare qui è un modo di andare avanti.",
    "Oggi basta non fermarsi.",
    "Respira. Anche questo è un passo."
]


# concetti interiori
concetti = [

    "la pazienza",
    "la calma",
    "la costanza",
    "la determinazione",
    "il coraggio",
    "la resilienza",
    "la quiete",
    "la fiducia",

    "la presenza",
    "la lucidità",
    "la perseveranza",
    "la volontà",
    "la disciplina",
    "la serenità",
    "la speranza",
    "la stabilità",

    "la forza silenziosa",
    "la presenza interiore",
    "la continuità",
    "la dedizione",
    "la chiarezza",
    "la cura"
]


# azioni che producono cambiamento
azioni = [

    "trasforma i giorni difficili",
    "costruisce ciò che sembra impossibile",
    "apre strade dove prima non c'erano",
    "fa crescere anche ciò che non si vede",
    "vince quando tutto sembra fermo",
    "tiene acceso qualcosa dentro",

    "cambia lentamente le cose",
    "porta avanti anche nei momenti incerti",
    "regge il peso delle giornate lunghe",
    "illumina i passi più piccoli",
    "muove ciò che sembra immobile",

    "mantiene viva la direzione",
    "rafforza anche i passi fragili",
    "costruisce nel silenzio",
    "fa spazio alla luce",
    "mantiene il cammino",

    "sostiene nei momenti duri",
    "apre spiragli inattesi",
    "aiuta a respirare meglio",
    "rende più leggero il viaggio",
    "ricorda che è possibile continuare",

    "accende nuovi inizi",
    "porta avanti anche oggi",
    "tiene viva la speranza"
]


# memoria runtime per evitare ripetizioni
frasi_usate = []
MAX_MEMORIA = 1000


def frase_valida(frase):

    parole = frase.split()

    if len(parole) > 18:
        return False

    if len(parole) < 3:
        return False

    return True


def frase_non_ripetuta(frase):

    if frase in frasi_usate:
        return False

    frasi_usate.append(frase)

    if len(frasi_usate) > MAX_MEMORIA:
        frasi_usate.pop(0)

    return True


def genera_frase_dinamica():

    concetto = random.choice(concetti)
    azione = random.choice(azioni)

    strutture = [

        f"{concetto.capitalize()} {azione}.",

        f"A volte {concetto} {azione}.",

        f"Spesso {concetto} {azione}.",

        f"Quando tutto sembra fermo, {concetto} {azione}.",

        f"Certe volte {concetto} {azione}.",

        f"Forse {concetto} {azione}.",

        f"Nel tempo, {concetto} {azione}.",

        f"A piccoli passi, {concetto} {azione}.",

        f"Con il tempo, {concetto} {azione}.",

        f"In silenzio, {concetto} {azione}.",

        f"Giorno dopo giorno, {concetto} {azione}.",

        f"Anche lentamente, {concetto} {azione}.",

        f"Con pazienza, {concetto} {azione}.",

        f"Passo dopo passo, {concetto} {azione}.",

    ]

    return random.choice(strutture)


def genera_frase():

    # probabilità frase speciale
    if random.randint(1, 25) == 1:
        return random.choice(frasi_speciali)

    while True:

        r = random.random()

        if r < 0.45:
            frase = random.choice(citazioni)
        else:
            frase = genera_frase_dinamica()

        if frase_valida(frase) and frase_non_ripetuta(frase):
            return frase