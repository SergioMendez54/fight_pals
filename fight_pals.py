#Fight Pals game
class Trainer:
    def __init(self, name, pals, potions, active):
        self.name = name
        self.pals = []
        self.potions = potions
        self.active = active
    
    def attack(self):
        pass

    def use_potion(self):
        pass

    def switch_pal(self):
        pass

class Fightpals(Trainer):
    def __init__(self, name, level, health, max_health, type, is_knocked_out=0):
        self.name = name
        self.level = level
        self.health = health
        self.max_health = max_health
        self.type = type
        self.is_knocked_out = is_knocked_out
        print("{} added and has {}hp. ".format(self.name, self.health))
    
    def lose_health(self):
        self.health -= 10
        print("{} lost 10hp and now has {}hp".format(self.name, self.health))
    
    def gain_health(self):
        self.health +=10
        print("{} gained 10hp and now has {}hp".format(self.name, self.health))
    
    def knocked_out(self):
        if self.health < 1:
            self.is_knocked_out = 1
            print("{} has {}hp and is knocked out. ".format(self.name, self.health))
  
    def revive(self):
        self.is_knocked_out = 0
        self.health = self.max_health
        print("{} is revived and has {}hp. ".format(self.name, self.health))
    
    #def attack(self, name):

    
#Start main game
print("Welcome to Pokepals. \nChoose your starting Pokepal:\n1: Charmander - Fire\n2: Squirtle - Water\n3: Bulbasaur - Grass")

first = input("Enter choice: ") 
while first not in ["1","2","3"]:
  input("Not a valid choice, try again: ")
  
charmander = Fightpals("Charmander", 1, 100, 100, "Fire") 
squirtle = Fightpals("Squirtle",1, 100, 100, "Water")
bulbasaur = Fightpals("Bulbasaur",1,100,100,"Grass")

charmander.lose_health()
charmander.lose_health()
charmander.gain_health()
charmander.knocked_out()




    
