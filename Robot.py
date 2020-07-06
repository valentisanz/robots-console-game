import random
class Robot():
    name=''
    power=0
    magic=0
    health=0
    
    def createRobot(self,name,power,magic,health):
        self.name=name
        self.power=power
        self.magic=magic
        self.health=health

    def getInfo(self):
        print(self.name,'-',self.health,'hp')
    def attack(self,enemy):
        rnd=random.randint(5, 10)
        if(rnd==5 or rnd==8 or rnd==10 ):
            enemy.health=enemy.health-self.power-rnd+2
            print(f'Critical hit! {enemy.name} -{self.power+rnd-2}hp')
        else:
            enemy.health=enemy.health-self.power
            print(f'{enemy.name} -{self.power}hp')
    def heal(self):
        self.health=self.health+self.magic
        print(f'+{self.magic}hp')
