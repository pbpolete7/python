import os

# 1. Crear el directori /home/cicles/AO/Prova si no existeix
directori = "/home/cicles/AO/Prova"
os.makedirs(directori, exist_ok=True)

# 2. Canviar-nos a aquest directori
os.chdir(directori)

# 3. Crear el fitxer Ex12.txt i escriure els noms dels companys de classe
companys = ["izan", "moha", "assama", "pol", "joan", "lucas", "ian", "rafael", "aitor", "luca"]
with open("Ex12.txt", "w", encoding="utf-8") as fitxer:
    for nom in companys:
        fitxer.write(nom + "\n")

# 4. Obrir-lo per afegir els noms dels professors
professors = ["joan", "pep", "david", "jesus"]
with open("Ex12.txt", "a", encoding="utf-8") as fitxer:
    for nom in professors:
        fitxer.write(nom + "\n")

# 5. Obrir el fitxer i posar tot el seu contingut dins d'una llista
with open("Ex12.txt", "r", encoding="utf-8") as fitxer:
    noms_totals = [linia.strip() for linia in fitxer]

# Mostrar la llista final
print(noms_totals)
