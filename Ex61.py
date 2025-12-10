def lenp(frase):
    """
    Retorna una llista amb la longitud de cada paraula d'una cadena.
    """
    # Separar la frase en paraules
    paraules = frase.split()
    # Aplicar map per obtenir la longitud de cada paraula
    longituds = list(map(len, paraules))
    return longituds

# Exemple d'ús
frase = "Hola món com estàs"
print(lenp(frase))  # Sortida: [4, 3, 3, 5]
