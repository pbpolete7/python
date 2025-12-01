def eliminarcapicua(llista):
    # Comprovar que la llista tingui almenys 2 elements
    if len(llista) < 2:
        return []   # Si no, retornem una llista buida
    
    return llista[1:-1]  # Retorna la llista sense primer i darrer element
# Exemple de prova
original = [10, 20, 30, 40, 50]
nova = eliminarcapicua(original)

print("Llista original:", original)
print("Llista sense primer i darrer element:", nova)
