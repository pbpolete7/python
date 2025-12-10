# Nombre inicial
max_num = 5

# Bucle per a cada línia
for i in range(max_num, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()  # Nova línia després de cada fila
