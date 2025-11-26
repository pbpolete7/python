def mostrar_majors_que(tupla, x):
    print(f"Valors majors que {x}:")
    for num in tupla:
        if num > x:
            print(num)


# Programa per provar-ho
vals = []

# Introduir valors per construir la tupla
print("Introdueix valors enters (escriu 'fi' per acabar):")
while True:
    entrada = input("Valor: ")
    if entrada.lower() == "fi":
        break
    vals.append(int(entrada))

# Convertim la llista a tupla
tupla_nums = tuple(vals)

# Mostram els majors de 18
mostrar_majors_que(tupla_nums, 18)
