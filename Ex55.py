# Números parells fins a 100
print("Números parells:")
for i in range(2, 101, 2):  # Comença a 2, fins a 100, increment de 2
    print(i, end=", " if i < 100 else "\n")

# Números senars fins a 100
print("Números senars:")
for i in range(1, 101, 2):  # Comença a 1, fins a 99, increment de 2
    print(i, end=", " if i < 100 else "\n")
