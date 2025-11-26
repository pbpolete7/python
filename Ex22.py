def superposicio(llista1, llista2):
    for element in llista1:
        if element in llista2:
            return True
    return False
print(superposicio([1, 2, 3], [3, 4, 5]))   # True
print(superposicio(["a", "b"], ["c", "d"])) # False
print(superposicio([], [1, 2]))             # False
