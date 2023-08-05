class Player:
    def __init__(self, name, health = 100, energy = 100): #contruvtor
        self.name = name
        self.health = health
        self.energy = energy

    def attack(self, target, damage = 10):
        target.health -= damage
        self.energy -= damage
        print(f"{self.name} attacking {damage} damage to {target.name}!")
        if target.is_attacked(player_name = self.name):
            self.health -= target.damage
        
    def show_info(self):
        print(f"Status {self.name}")
        print(f"Health : {self.health} hp")
        print(f"Energy : {self.energy} mp")
        print("")
        
        
class Monster:
    def __init__(self, name, health = 100):
        self.name = name
        self.health = health
        self.health_init = self.health
        self.damage = 10
        
    def is_attacked(self, player_name):
        print(f"{self.name} attack {self.damage} damage to {player_name}")
        print("")
        return self.health < self.health_init
    
    def show_info(self):
        print(f"Status {self.name}")
        print(f"Health : {self.health} hp")
        print("")
        

knight = Player(name = "Knight")
mage = Player(name = "Mage")
dragon = Monster(name = "Dragon", health = 500)
ldragon = Monster(name = "Little Dragon")

knight.attack(target = dragon, damage = 80)
mage.attack(target = ldragon, damage = 20)

knight.show_info()
mage.show_info()
dragon.show_info()
ldragon.show_info()
