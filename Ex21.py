import unicodedata

def es_palindrom(paraula: str) -> bool:
    # Passar a minúscules
    p = paraula.lower()

    # Eliminar accents
    p = ''.join(
        c for c in unicodedata.normalize('NFD', p)
        if unicodedata.category(c) != 'Mn'
    )

    # Eliminar espais i signes de puntuació
    p = ''.join(c for c in p if c.isalnum())

    # Comprovar palíndrom
    return p == p[::-1]
print(es_palindrom("radar"))       # True
print(es_palindrom("Ara"))         # True
print(es_palindrom("réfer"))       # True (funciona amb accents)
print(es_palindrom("A mamá Roma le aviva el amor a mamá"))  # True
print(es_palindrom("Python"))      # False
