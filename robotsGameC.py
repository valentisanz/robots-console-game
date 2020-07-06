import random
from Robot import *


player = Robot()
npc = Robot()

name = input('>Enter your name: ')
print('Choose a robot type:')
robotType = input('>Fighter(1), Healer(2), Tank(3): ')
if(robotType == '1'):
    player.createRobot(name, 15, 10, 100)
elif(robotType == '2'):
    player.createRobot(name, 10, 15, 100)
elif(robotType == '3'):
    player.createRobot(name, 10, 10, 130)
else:
    player.createRobot(name, 15, 10, 100)
    print('Invalid value, Fighter selected')

enemyType = random.randint(1, 3)
if(enemyType == 1):
    npc.createRobot('RX-Fighter', 15, 10, 100)
elif(enemyType == 2):
    npc.createRobot('RX-Healer', 10, 15, 100)
elif(enemyType == 3):
    npc.createRobot('RX-Tank', 10, 10, 130)

play = True
turn = 0
while play:
    turn = turn+1
    print(f'****************************TURN:{turn}****************************')
    action = input('>Attack(1) or Heal(2): ')
    if(action == '1'):
        player.attack(npc)
    elif(action == '2'):
        player.heal()
    else:
        print('Invalid action, you lost your turn.')
    if(npc.health <= 50 and player.health > 30):
        npcAction = random.randint(1, 4)
        if(npcAction == 2 or npcAction == 4):
            npc.attack(player)
        else:
            npc.heal()
    else:
        npcAction = random.randint(1, 3)
        if(npcAction == 1 or npcAction == 3):
            npc.attack(player)
        else:
            npc.heal()
    print()
    player.getInfo()
    npc.getInfo()
    if(player.health <= 0 or npc.health <= 0):
        play = False

if(player.health > 0):
    print(f'{player.name} WINS!')
else:
    print(f'{npc.name} WINS!.')
