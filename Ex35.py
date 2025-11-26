def comptar_vocals(paraula):
    paraula = paraula.lower()  # per evitar problemes amb majúscules

    vocals = {
        "a": 0,
        "e": 0,
        "i": 0,
        "o": 0,
        "u": 0
    }

    for lletra in paraula:
        if lletra in vocals:
            vocals[lletra] += 1

    return vocals
resultat = comptar_vocals("Ratapinyada")
print(f"Hi ha {resultat['a']} a’s, {resultat['e']} e’s, {resultat['i']} i’s, {resultat['o']} o’s i {resultat['u']} u’s.")
