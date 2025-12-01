def esta_ordenada(llista):
    # Comprovar si està ordenada en ordre ascendent
    if llista == sorted(llista):
        return "Està ordenada de forma ascendent"
    
    # Comprovar si està ordenada en ordre descendent
    if llista == sorted(llista, reverse=True):
        return "Està ordenada de forma descendent"
    
    # Qualsevol altre cas
    return "No està ordenada"
print(esta_ordenada([3, 2, 1]))   # descendent
print(esta_ordenada([4, 5, 6]))   # ascendent
print(esta_ordenada([3, 5, 1]))   # no ordenada
print(esta_ordenada([10]))        # un sol element → ascendent
print(esta_ordenada([]))          # llista buida → ascendent
