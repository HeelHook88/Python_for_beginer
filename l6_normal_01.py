import sys

class Person:
    def __init__(self, health, damage, armor):
        self.health = 100
        self.damage = 100
        self.armor = 20

class Player(Person):

    def att(self, armourEnemy ):
        return armourEnemy - self.damage

    def deff(self,damage):
        return self.armor - self.damage

    def _calcMyDamge(self, damage):
        self.health = self.health - self.damage

class Enemy(Person):

    def att(self, armourPlayer ):
        return armourPlayer - self.damage

    def deff(self,damage):
        return self.armor - self.damage

    def _calcMyDamge(self, damage):
        self.health = self.health - self.damage

class StartGame:
    player = Player("health","damage","armor")
    enemy = Enemy("health","damage","armor")

    last_attacker = enemy
    while player.health > 0 and enemy.health > 0:
            if last_attacker == player:
                player._calcMyDamge("damage")
                last_attacker = enemy
            else:
                enemy._calcMyDamge("damage")
                last_attacker = player

            if player.health > 0:
                print('Игрок победил!')
                sys.exit()
            else:
                print('Враг победил!')
                sys.exit()
StartGame()