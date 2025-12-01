def hi_ha_duplicats(llista):
    # Si la longitud del conjunt és menor que la de la llista, hi ha duplicats
    return len(set(llista)) != len(llista)
print(hi_ha_duplicats([1, 2, 3, 4]))        # False
print(hi_ha_duplicats([1, 2, 3, 2]))        # True
print(hi_ha_duplicats(['a', 'b', 'c']))     # False
print(hi_ha_duplicats(['a', 'b', 'a']))     # True
print(hi_ha_duplicats([]))                  # False (cap duplicat)
