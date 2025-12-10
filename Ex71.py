def llegir_fitxer(nom_fitxer):
    """
    Llegeix i retorna el contingut d'un fitxer.
    Controla errors si el fitxer no existeix o no es pot obrir.
    """
    try:
        with open(nom_fitxer, 'r', encoding='utf-8') as f:
            contingut = f.read()
        return contingut
    except FileNotFoundError:
        print(f"Error: El fitxer '{nom_fitxer}' no existeix.")
    except IOError:
        print(f"Error: No s'ha pogut obrir el fitxer '{nom_fitxer}'.")

# Exemple d'ús
fitxer = "exemple.txt"
dades = llegir_fitxer(fitxer)
if dades is not None:
    print("Contingut del fitxer:")
    print(dades)
