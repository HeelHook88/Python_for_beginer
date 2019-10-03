import random
import os
import sys

class Card ():


    def create_list(self):

        rand_list = [random.randint(1, 91) for i in range(1, 91)]
        rand_card = []

        while len(rand_card) <5:
            rand = random.SystemRandom()
            rand_card.append(rand.choice(rand_list))

        for i in range(4):
            rand_card.insert(random.randint(1,9),' ')
        return (rand_card)


class Player(Card):

    def pl_card_create(self):
        pl_card = []
        for i in range(3):
            pl_card.append(Player.create_list('self'))

        return  pl_card

class NPC(Card):

    def npc_card_create(self):
        npc_card = []
        for i in range(3):
            npc_card.append(NPC.create_list('self'))

        return npc_card


class Start():

    pl_card = Player
    npc_card = NPC

    def start(self):

        while True:
            rand = random.SystemRandom()

        #print('Новый бочонок: ', {} ,'Остальось {}'.format((random.randint(1,91)),len(Card.create_list('self'))))
        print('Карточка игрока', '__________________________________________''\n', npc_card.npc_card_create('self'),
              '\n''__________________________________________')
        print('Карточка компьютера', '__________________________________________''\n', pl_card.pl_card_create('self'),
              '\n''__________________________________________')

        choise = input(str())
        print('Зачеркнуть цифру Y/N')
        if choise == 'Y':
            pass
        else:
            pass

#start = Start
#start.start('self')
rand = random.SystemRandom()
npc_card = NPC
pl_card = Player
card = Card

rand_list = random.randint(1, 91)


print('Карточка игрока''\n', '________________________________________''\n', npc_card.npc_card_create('self'),
    '\n''_________________________________________')
print('Карточка компьютера''\n', '________________________________________''\n', pl_card.pl_card_create('self'),
    '\n''_________________________________________')

#print('Новый бочонок: ', {} ,'Остальось {}'.format(rand.choice(rand_list)))
