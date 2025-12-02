def elimina_duplicats(llista):
    nova_llista = []
    vistos = set()
    for element in llista:
        if element not in vistos:
            nova_llista.append(element)
            vistos.add(element)
    return nova_llista
nums = [1, 2, 2, 3, 1, 4, 3]
print(elimina_duplicats(nums))
# Sortida: [1, 2, 3, 4]
