import random

def generar_codi():
    # Codi de 4 xifres aleatòries (0–9)
    return [random.randint(0, 9) for _ in range(4)]

def comparar_codis(codi, proposta):
    # Compta xifres correctes (posició encertada)
    correctes = sum(codi[i] == proposta[i] for i in range(4))
    
    # Compta coincidències fora de lloc
    # Fem llistes de xifres no encertades
    codi_restants = []
    proposta_restants = []
    
    for i in range(4):
        if codi[i] != proposta[i]:
            codi_restants.append(codi[i])
            proposta_restants.append(proposta[i])
    
    # Nombre de coincidències = suma del mínim de vegades que surt cada dígit
    coincidencies = 0
    for x in set(proposta_restants):
        coincidencies += min(proposta_restants.count(x), codi_restants.count(x))
    
    return correctes, coincidencies

def llegir_proposta():
    while True:
        entrada = input("Introdueix un codi de 4 xifres: ")
        if entrada.isdigit() and len(entrada) == 4:
            return [int(x) for x in entrada]
        print("Entrada incorrecta. Escriu exactament 4 xifres.")

def mastermind():
    print("Benvingut al MasterMind!")
    codi = generar_codi()
    intents = 0

    while True:
        proposta = llegir_proposta()
        intents += 1
        
        correctes, coincidencies = comparar_codis(codi, proposta)
        
        print(f"Xifres correctes en posició correcta: {correctes}")
        print(f"Xifres correctes en posició incorrecta: {coincidencies}")
        
        if correctes == 4:
            print(f"Felicitats! Has encertat el codi en {intents} intents!")
            break

# Executar el joc
mastermind()
