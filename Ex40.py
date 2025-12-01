# Programa per calcular el capital final amb interès compost

# Llegir dades amb validació
while True:
    capital = float(input("Introdueix el capital inicial (50.000€ - 800.000€): "))
    if 50000 <= capital <= 800000:
        break
    print("❌ Error: el capital ha d'estar entre 50.000 i 800.000 euros.")

while True:
    interes = float(input("Introdueix l'interès (0.5% - 13%): "))
    if 0.5 <= interes <= 13:
        break
    print("❌ Error: l'interès ha d'estar entre 0.5% i 13%.")

while True:
    anys = int(input("Introdueix els anys (3 - 40): "))
    if 3 <= anys <= 40:
        break
    print("❌ Error: els anys han d'estar entre 3 i 40.")

# Càlcul del capital final
capital_final = capital * (1 + interes / 100) ** anys

# Resultat
print(f"\nEl capital final serà de: {capital_final:.2f} €")
