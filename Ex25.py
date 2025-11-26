def crear_punts(llista):
    for num in llista:
        print("." * num)

def dibuixar_piramide(alcada):
    # Genera una llista de 1 fins a l'alçada
    punts_per_linia = list(range(1, alcada + 1))
    crear_punts(punts_per_linia)

# Exemple:
dibuixar_piramide(5)
