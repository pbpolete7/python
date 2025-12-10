from functools import reduce

def Passar_a_Numero(llista):
    """
    Retorna el número que corresponen els dígits d'una llista.
    """
    return reduce(lambda x, y: x * 10 + y, llista)

# Exemple d'ús
digits = [3, 4, 1, 5]
numero = Passar_a_Numero(digits)
print(numero)  # Sortida: 3415
