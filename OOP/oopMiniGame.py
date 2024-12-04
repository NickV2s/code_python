from random import randrange
class Character():
    def __init__(self,userName,baseStats = [50,5,5]):
        self.name = userName
        self.baseStats = baseStats
        self.hp = baseStats[0]
        self.dmg = baseStats[1]
        self.speed = baseStats[2]
        self.lvl = 1
        self.investment = [0,0,0]
        self.dead = False
    def __str__(self):
        return f"{self.name}( HP:{self.hp}, DMG:{self.dmg}, Speed:{self.speed}"
    def levelUp(self):
        upgrade = input(f"Choose a stat to level up: HP(+{self.investment[0]}), DMG(+{self.investment[1]}), Speed(+{self.investment[2]})")
        if upgrade=="HP":
            self.hp+=10
            self.investment[0]+=1
        elif upgrade=="DMG":
            self.dmg+=2
            self.investment[1]+=1
        else:
            self.speed+=2
            self.investment[2]+=1
    def attack(self,other):
            if other.speed>randrange(1,80):
               print("Dodged")
            else:
                other.hp = other.hp-self.dmg
                if other.hp<=0:
                    self.lvl+=1
                    self.levelUp()
                    other.dead = True

user = Character("Test",[100,10,10])
mob1 = Character("Zombie")
enemy=mob1
while user.lvl<10:
    if enemy.dead==True:
        enemy = Character("Zombie")
        user.hp+=15
    while user.dead==False and enemy.dead==False:
        user.attack(enemy)
        enemy.attack(user)
        print(user)
        print(enemy)
