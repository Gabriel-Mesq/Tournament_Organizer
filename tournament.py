import random

class Equipe:
    
    def __init__(self, nome: str, membros: list):
        self.nome = nome
        self.membros = membros

    def presentation(self):
        print(f'Nome da equipe: {self.nome}\nIntegranntes da equipe:') 
        for membro in self.membros:
            print(membro)

class Torneio:
    
    def __init__(self, equipes: list):
        self.equipes = equipes

    def presentation(self):
        for equipe in self.equipes:
            print(equipe.presentation())

Bananos = Equipe("Bananos", ["A", "B", "C"])
Moe = Equipe("Moe", ["D", "F", "G"])

T = Torneio([Bananos, Moe])

T.presentation()