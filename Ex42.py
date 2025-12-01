# Programa que indica quants dígits té un número

while True:
    n = input("Introdueix un número entre 1 i 900000: ")

    # Comprovació que sigui un número enter positiu
    if n.isdigit():
        n_int = int(n)
        if 1 <= n_int <= 900000:
            break

    print("❌ Error: has d'introduir un número enter entre 1 i 900000.")

# Comptar els dígits (convertint-lo a string)
num_digits = len(n)

print(f"El número {n_int} té {num_digits} dígits.")
