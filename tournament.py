import random

class Equipe:
    
    v = 0
    d =  0
    scr = 0

    def __init__(self, nome: str, membros: list):
        self.nome = nome
        self.membros = membros

    def presentation(self):
        print(f'Nome da equipe: {self.nome}\nIntegranntes da equipe:') 
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

class Torneio:
    
    def __init__(self, equipes: list):
        self.equipes = equipes

    def presentation(self):
        for equipe in self.equipes[:2]:
            print(equipe.presentation())

Bananos = Equipe("Bananos", ["A", "B", "C"])

Bananos.placar()

Bananos.score(int(2))

Bananos.placar()

