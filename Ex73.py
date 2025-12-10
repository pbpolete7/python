from abc import ABC, abstractmethod

# Classe base abstracta
class Animal(ABC):
    def __init__(self, especie, edat):
        self.especie = especie
        self.edat = edat

    @abstractmethod
    def xerrar(self):
        pass

    @abstractmethod
    def mourem(self):
        pass

    def quisoc(self):
        print(f"{self.especie} fa algo al quiosc.")

# Subclasses concretes
class Cavall(Animal):
    def xerrar(self):
        print("Neigh!")

    def mourem(self):
        print("El cavall galopa.")

class Dofí(Animal):
    def xerrar(self):
        print("Eeee-eee!")

    def mourem(self):
        print("El dofí nedant ràpid.")

class Abella(Animal):
    def xerrar(self):
        print("Bzzz bzzz!")

    def mourem(self):
        print("L'abella vola d'una flor a una altra.")

    def picar(self):
        print("L'abella pica!")

class Humà(Animal):
    def __init__(self, especie, edat, nom):
        super().__init__(especie, edat)
        self.nom = nom

    def xerrar(self):
        print(f"{self.nom} diu hola!")

    def mourem(self):
        print(f"{self.nom} camina.")

class Fiet(Humà):
    def __init__(self, especie, edat, nom, pares):
        super().__init__(especie, edat, nom)
        self.pares = pares

    def nompares(self):
        print(f"Els pares de {self.nom} són: {', '.join(self.pares)}")

class Centaure(Cavall, Humà):
    def __init__(self, especie, edat, nom):
        Cavall.__init__(self, especie, edat)
        self.nom = nom

    def xerrar(self):
        print(f"{self.nom} crida com centaure!")

    def mourem(self):
        print(f"{self.nom} galopa amb les cames de cavall i camina com humà.")

# Classe sense relació amb Animal
class Xou:
    def xerrar(self):
        print("Xou: farem soroll!")

    def mourem(self):
        print("Xou: ens movem d'una manera divertida.")

    def quisoc(self):
        print("Xou: fem coses al quiosc.")

# Crear llista d'elements
elements = [
    Cavall("Cavall", 5),
    Dofí("Dofí", 3),
    Abella("Abella", 1),
    Humà("Humà", 30, "Joan"),
    Fiet("Humà", 5, "Nina", ["Anna", "Marc"]),
    Centaure("Centaure", 10, "Chiron"),
    Xou()
]

# Bucle que crida als mètodes comuns
for e in elements:
    e.xerrar()
    e.mourem()
    e.quisoc()
    # Mètodes específics
    if isinstance(e, Abella):
        e.picar()
    if isinstance(e, Fiet):
        e.nompares()
