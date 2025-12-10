def dividir(a, b):
    """
    Retorna la divisió de a entre b.
    Si b és 0, avisa que no es pot dividir per zero.
    """
    if b == 0:
        print("Error: No es pot dividir per zero!")
        return None
    return a / b

# Exemple d'ús
print(dividir(10, 2))  # Sortida: 5.0
print(dividir(5, 0))   # Sortida: Error: No es pot dividir per zero! / None
