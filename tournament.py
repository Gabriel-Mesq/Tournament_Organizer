import random

class Member:

    members_list = []
    teams_list = []

    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight  

    def addMember(self):
        self.members_list.append(self)

    def divideTeams(self, qt):
        
        #Sort the members in ascending order of weight
        
        i = 0

        while len(self.members_list) > qt:
            self.teams_list[i].append(self.members_list[0])
            self.teams_list[i].append(self.members_list[-1])
            self.members_list.pop[0]
            self.members_list.pop[-1]
            i += 1

        for i in range(qt):
            self.teams_list[i].append(self.members_list[i])

        for i in self.teams_list:
            print(i)

    def presentation(self):

        for i in self.members_list:
            print(i.name)

class Equipe:
    
    v = 0
    d =  0
    scr = 0

    def __init__(self, name: str, membros: list):
        self.name = name
        self.membros = membros

    def presentation(self):
        print(f'Nome da equipe: {self.name}\nIntegrantes da equipe:') 
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
                print(self.equipes[i].name, "x", self.equipes[i + 1].name, "\n") 
                i += 2
        
        except IndexError:
            print(self.equipes[len(self.equipes) - 1].name)

qt = int(input("How many teams are going to compete? "))

for i in range(qt*5):
    Member.addMember(Member(input("Nickname: "), int(input("Tier: "))))

Member.presentation(Member)



"""
Ideias:

Soma da pontuação do time deve dar times com a menor descrepancia possivel

Forma de somar 5 pesos


"""