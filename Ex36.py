def es_de_traspas(any):
    if (any % 4 == 0 and any % 100 != 0) or (any % 400 == 0):
        return True
    else:
        return False
print(es_de_traspas(2020))  # True
print(es_de_traspas(1900))  # False
print(es_de_traspas(2000))  # True
print(es_de_traspas(2023))  # False
