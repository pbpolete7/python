# Programa que comprova si dues paraules rimen

# Demanar paraules
p1 = input("Introdueix la primera paraula: ").strip().lower()
p2 = input("Introdueix la segona paraula: ").strip().lower()

# Comprovació de rima
if len(p1) >= 3 and len(p2) >= 3 and p1[-3:] == p2[-3:]:
    print("Rimen!")
elif len(p1) >= 2 and len(p2) >= 2 and p1[-2:] == p2[-2:]:
    print("Rimen un poc.")
else:
    print("No rimen.")
