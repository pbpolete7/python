def filtrar_paraules(llista, x):
    resultat = []
    for paraula in llista:
        if len(paraula) > x:
            resultat.append(paraula)
    return resultat
print(filtrar_paraules(["Hola", "Ramis", "IES", "Paraula"], 4))
# Retorna: ['Hola', 'Ramis', 'Paraula']
