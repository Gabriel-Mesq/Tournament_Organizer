import random

class Member:

    def __init__(self, nome: str, peso: float):
        self.nome = nome
        self.peso = peso
        
class Equipe:
    
    v = 0
    d =  0
    scr = 0

    def __init__(self, nome: str, membros: list):
        self.nome = nome
        self.membros = membros

    def presentation(self):
        print(f'Nome da equipe: {self.nome}\nIntegrantes da equipe:') 
        for membro in self.membros:
            print(membro)

    def score(self, n: int):
        
        self.scr += n
        
        if n > 0:
            self.v += n
        else: 
            self.d += n
    
    def placar(self):
        print(f"Score: {self.scr}\nV: {self.v}\nD: {self.d}")

class Tournament:
    
    def __init__(self, equipes: list):
        self.equipes = equipes

    def presentation(self):
        for equipe in self.equipes:
            print(equipe.presentation())

    def brackets(self):
        
        random.shuffle(self.equipes)

        i = 0

        try:
            
            while i < len(self.equipes):
                print(self.equipes[i].nome, "x", self.equipes[i + 1].nome, "\n") 
                i += 2
        
        except IndexError:
            print(self.equipes[len(self.equipes) - 1].nome)

A = Equipe("Ada", ["a1", "a2", "a3"])
B = Equipe("Bananos", ["A", "B", "C"])
C = Equipe("Cada", ["D", "F", "G"])
D = Equipe("Dada", ["D", "F", "G"])
E = Equipe("Eada", ["D", "F", "G"])

T = Tournament([A, B, C, D, E])

T.brackets()