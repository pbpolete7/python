def gran_llista(llista):
    mes_gran = llista[0]
    for num in llista:
        if num > mes_gran:
            mes_gran = num
    return mes_gran
print(gran_llista([3, 4, 2, 3, 10]))   # 10
