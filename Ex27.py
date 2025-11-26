def paraula_mes_llarga(llista):
    mes_llarga = llista[0]
    for paraula in llista:
        if len(paraula) > len(mes_llarga):
            mes_llarga = paraula
    return mes_llarga
print(paraula_mes_llarga(["Hola", "Ramis", "IES", "Paraula"]))  
# Retorna: Paraula
