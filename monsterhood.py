import random
from observable import Observable
from observer import Observer
import sys

class Monster(Observable):
    """
    Base class for all the monsters in the game. Inhereits and initiates
    observable so the monsters can use the observable methods
    """
    def __init__(self):
        """
        Constructor for monster base class. Initiates observable 
        args:
        param(self)
        """
        Observable.__init__(self)
    def makeSound():
        print("blank")

class Zombie(Monster):
    """
    Class for zombie monster
    """

    def __init__(self):
        """
        Constructor for zombie class
        initiates name and HP
        args:
        param(self)
        """
    
        Monster.__init__(self)
        self.name = "zombie"
        self.hp = random.randint(50, 100)
    
    def getName(self):
        """
        method to return zombie's name in string form
        Returns:
            "zombie" as a string
        """

        return self.name
    
    def attack(self, player):
        """
        Method to attack player
        args:
            self, self explanitory
            player, player object gets attacked
        """
        
        x = random.randint(0, 10)
        print("zombie bites you for", x, " damage")
        player.takeDamage(x)
    
    def takeDamage(self,  damage, weapon):
        """
        zombie loses hp when attack
        notifies observer when health reaches zero or below
        args:
            self
            damage, amount of damage
            weapon, damage is doubled if attacked with a sour straw
        """
        
        
        if (weapon == "sourstraw"):
            print("sour straw did bonus damage to zombie!")
            damage = damage * 2
        self.hp = self.hp - damage
        print("zombie took", damage, "damage and is now at ", self.hp, "hp")
        if (self.hp <= 0):
            self.update()
    
    def getHP(self):
        """
        returns HP
        args:
            self
        returns:
            HP, amount of hitpoints zombie has remaining
        """
        
        return self.hp
        
class Vampire(Monster):
    """
    Class for vampire monster
    """
    

    def __init__(self):
        """
        Constructor for vampire class
        initiates name and HP
        args:
        param(self)
        """
            
        
        Monster.__init__(self)
        self.name = "vampire"
        self.hp = random.randint(100, 200)
    
    def getName(self):
        """
        method to return vampire's name in string form
        Returns:
            "vampire" as a string
        """        
        
        
        return self.name
    
    def attack(self, player):
        """
        Method to attack player
        args:
            self, self explanitory
            player, player object gets attacked
        """
        
        x = random.randint(10, 20)
        print("vampire swoops at you, doing", x, "damage")
        player.takeDamage(x)
    
    def takeDamage(self,  damage, weapon):
        """
        vampire loses hp when attack
        notifies observer when health reaches zero or below
        args:
            self
            damage, amount of damage
            weapon, vampire is immune to chocolate bar
        """
        

        if (weapon == "chocolatebar"):
            damage = 0
            print("Vampire was immune to chocolate bar!")
        self.hp = self.hp - damage
        print("vampire took", damage, "damage and is now at ", self.hp, "hp")
        if (self.hp <= 0):
            self.update()
    
    def getHP(self):
        """
        returns HP
        args:
            self
        returns:
            HP, amount of hitpoints vampire has remaining
        """
        
    
        return self.hp
        
class Ghoul(Monster):
    """
    Class for Ghoul monster
    """
    
    
    def __init__(self):
        """
        Constructor for ghoul class
        initiates name and HP
        args:
        param(self)
        """
        
        
        
        Monster.__init__(self)
        self.name = "ghoul"
        self.hp = random.randint(40, 80)
    
    def getName(self):
        """
        method to return ghoul's name in string form
        Returns:
            "ghoul" as a string
        """    
        
        
        return self.name
    
    def attack(self, player):
        """
        Method to attack player
        args:
            self, self explanitory
            player, player object gets attacked
        """
        
        x = random.randint(15, 30)
        print("ghoul vomits on you for", x, "damage")
        player.takeDamage(x)
    def takeDamage(self,  damage, weapon):
        """
        ghoul loses hp when attacked
        notifies observer when health reaches zero or below
        args:
            self
            damage, amount of damage
            weapon, not really needed since the bonus is calculated in player 
            attack, but it makes things easier if all monsters follow the same
            pattern
        """
        

        self.hp = self.hp - damage
        print("ghoul took", damage, "damage and is now at ", self.hp, "hp")
        if (self.hp <= 0):
            self.update()
            
    def getHP(self):
        """
        returns HP
        args:
            self
        returns:
            HP, amount of hitpoints ghoul has remaining
        """
        
        return self.hp
        

class Werewolf(Monster):
    """
    Class for werewolf monster
    """

    def __init__(self):
        """
        Constructor for werewelf class
        initiates name and HP
        args:
        param(self)
        """
        
        Monster.__init__(self)
        self.name = "werewolf"
        self.hp = 200
    def getName(self):
        """
        method to return werewolf's name in string form
        Returns:
            "werewolf" as a string
        """    
        return self.name
    
    def attack(self, player):
        """
        Method to attack player
        args:
            self, self explanitory
            player, player object gets attacked
        """
        
        x = random.randint(0, 40)
        print("werewolf claws you for", x, "damage")
        player.takeDamage(x)
    
    def takeDamage(self,  damage, weapon):
        """
        werewolf loses hp when attacked
        notifies observer when health reaches zero or below
        args:
            self
            damage, amount of damage
            weapon, werewolf is immune to sour straws and chocolate bars
        """
        
        
        if (weapon == "sourstraw" or weapon == "chocolatebar"):
            print("werewolf is immune to weapon!")
            damage = 0
        self.hp = self.hp - damage
        print("werewolf took", damage, "damage and is now at ", self.hp, "hp")
        if (self.hp <= 0):
            self.update()

    def getHP(self):
        """
        returns hp
        return:
            hp, remaining monster health
        """
        return self.hp
        
        
class Person(Monster):
    """
    person class, friendly NPC that heals the player
    """
    def __init__(self):
        """
        constructor for person
        initiates health and name
        args:
            self
        """
        
        Monster.__init__(self)
        self.name = "person"
        self.hp = 100
    
    def getName(self):
        """
        returns:
            name, monster name in string form
        """
        return self.name
    
    def attack(self, player):
        """
        heals player, deals negative damage
        I changed the number to be between 1 and 7 because the game was too
        hard otherwise
        args:
            self
            player, the player object to be healed
        """
        

        x = random.randint(1, 7)
        print("Its dangerous to go alone, take this with you!")
        print("Person threw you a piece of candy for", x, "damage healed")
        x = x * -1
        player.takeDamage(x)
    def takeDamage(self,  damage, weapon):
        """
        person does not take damage
        args:
            self
            daamage
            weapon
        """
        pass
    
    def getHP(self):
        """
        returns hp
        args:
            self
        returns:
            hp, always 100 since person doesn't take damage
        """
        return self.hp
    
class House(Observable, Observer):
    """
    constructor for house object
    initiates constructor for observable so it can use its methods
    and calls method to generate monsters
    """
    def __init__(self):
        Observable.__init__(self)
        self.generateMonsters()
    
    def generateMonsters(self):
        """
        uses random numbers to generate monsters
        and inserts into a list
        I made the vampires and werewolves more rare to make the game easier
        args:
            self
        """
        
        self.monsterList = []
        self.monsterNum = random.randint(0, 10)
        for x in range(0, self.monsterNum):
           self.typeNum = random.randint(0, 100)
           if (self.typeNum < 50):
               newZombie = Zombie()
               newZombie.add_observer(self)
               self.monsterList.append(newZombie)
           elif(self.typeNum >= 50 and self.typeNum <65):
               newVampire = Vampire()
               newVampire.add_observer(self)
               self.monsterList.append(newVampire)
           elif(self.typeNum >= 65 and self.typeNum < 95):
               newGhoul = Ghoul()
               newGhoul.add_observer(self)
               self.monsterList.append(newGhoul)
           else:
               newWerewolf = Werewolf()
               newWerewolf.add_observer(self)
               self.monsterList.append(newWerewolf)
           
               
            

    def getMonsterList(self):
        """
        returns list of monsters
        """
        
        return self.monsterList
    
    def update(self, object):
        """
        activated from a monster class when that monster is defeated
        replaces monster with a human 
        if all monsters in the house have been defeated and turned into humans
        it updates neighborhood
        args:
            object, monster object to be turned into person
        """
        
        ourMonster = object
        position = self.monsterList.index(ourMonster)
        self.monsterList.pop(position)
        print(ourMonster.getName(), "was defeated and turned back into a human!")
        newPerson = Person()
        self.monsterList.insert(position, newPerson)
        
        personCount = 0
        for item in self.monsterList:
            if (isinstance(item,Person)):
                personCount = personCount + 1
        if(personCount == len(self.monsterList)):
                self.house_update()
        
        
  


class Player():
    """
    player class, the hero
    """
    
    def __init__(self):
        """
        constructor for player
        initates hp, player attack strength
        and ammo for weapons
        """
        
        self.hp = random.randint(100, 125)
        self.attack = random.randint(10, 20)
        self.hersheyAmmo = 0
        self.sourStrawAmmo = 0
        self.chocolateBarAmmo = 0
        self.nerdBombAmmo = 0
        self.generate_weapons()
    
    def generate_weapons(self):
        """
        generates ammo for player
        player always gets a hershey kiss with unlimited ammo 
        the other 9 weapons are randomly chosen from the 
        remaining 3 weapon types
        """
        
        self.hersheyAmmo = self.hersheyAmmo + 1
        for x in range (9):
            weaponInt = random.randint(1, 3)
            if (weaponInt == 1):
                self.sourStrawAmmo = self.sourStrawAmmo + 2
            elif (weaponInt == 2):
                self.chocolateBarAmmo = self.chocolateBarAmmo + 4
            elif(weaponInt == 3):
                self.nerdBombAmmo = self.nerdBombAmmo + 1
                
                
                
                

    def attackEnemy(self, monsterList):
        """
        takes player input for weapon
        iterates through monster list attacking each one with chosen weapon
        calculates damage
        args:
            monsterList, list of monsters to attack
        """
        
        
        monsterList = monsterList
        print ("Weapon choices: type exactly as displayed below")
        attacked = False  
        if (self.hersheyAmmo > 0):               
            print("hersheykiss, unlimited uses left")
        print("sourstraw", self.sourStrawAmmo, "uses left")
        print("chocolatebar", self.chocolateBarAmmo, "uses left")
        print("nerdbomb", self.nerdBombAmmo, "uses left")
        while (attacked == False):
           

            weaponChoice = input("which weapon do you use?:")
            if (weaponChoice == "hersheykiss" or 
                weaponChoice == "sourstraw" or
                weaponChoice == "chocolatebar" or 
                weaponChoice == "nerdbomb"):
                if (weaponChoice == "hersheykiss" and self.hersheyAmmo > 0 ):
                    print("you threw a handful of Hershey Kisses at the house")
                    for target in monsterList:
                        target.takeDamage(self.attack, weaponChoice)
                    return
                if (weaponChoice == "sourstraw" and self.sourStrawAmmo > 0):
                    print("you threw a handful of Sour Straws at the house")
                    multiplier = random.uniform(1, 1.75)
                    for target in monsterList:
                        target.takeDamage(int(self.attack*multiplier),weaponChoice)
                    self.sourStrawAmmo = self.sourStrawAmmo-1
                    return
                if (weaponChoice == "chocolatebar" and self.chocolateBarAmmo > 0):
                    print("you threw a chocolate Bar at the house")
                    multiplier = random.uniform(2, 2.4)
                    for target in monsterList:
                        target.takeDamage(int(self.attack*multiplier),weaponChoice)
                    self.chocolateBarAmmo = self.chocolateBarAmmo -1
                    return
                if (weaponChoice == "nerdbomb" and self.nerdBombAmmo > 0):
                    print("you threw a Nerd Bomb at the house")
                    multiplier = random.uniform(3.5, 5)
                    for target in monsterList:
                        if (target.getName() == "ghoul"):
                            print("did bonus damage to ghoul!")
                            target.takeDamage(int(self.attack*5),weaponChoice)
                        else:
                            target.takeDamage(int(self.attack*multiplier),weaponChoice)
                    self.nerdBombAmmo = self.nerdBombAmmo -1
                    return
                else:
                    print("not enough ammo")
            else:
                print("weapon not found")

    def takeDamage(self, damage):
        """
        player recieves damage from monster and subtstracts it from total health
        if given negative damage, player is healed
        max health limit of 125 to prevent cheating
        args:
            damage, amount of damage player has taken
        """
        
        self.hp = self.hp - damage
        #caps hp on healing 
        if (self.hp > 125):
            self.hp = 125
    
    def displayStats(self):
        """
        displays health and ammo
        """
        
        if (self.hersheyAmmo > 0):
            print("Hersheys Kiss ammo: unlimited")
        print("Health:", self.hp)
        print("Sour Straw ammo:", self.sourStrawAmmo)
        print("Chocolate Bar Ammo:", self.chocolateBarAmmo)
        print("Nerd Bomb Ammo:", self.nerdBombAmmo)
        
    def getHP(self):
        """
        returns player hitpoints
        returns:
            self.hp, remaining player hitpoints
        """
        return self.hp
        



class Neighborhood(Observer):
    """
    creates and stores 3x3 grid of houses
    is updates when a house is clear
    ends game with all occupied houses are clear
    """
    
    def __init__(self):
        """
        constructor for neighborhood
        inititates observer and calls house grid generation method
        """
        Observer.__init__(self)
        self.makeHouseGrid()
    
    def makeHouseGrid(self):
        """
        generates 3x3 grid of houses
        also initiates winNum, the number of houses that need to be cleared
        to win, and clearCount, the number of houses cleared
        """
        
        self.clearCount = 0
        self.winNum = 0
        self.newList = []
        for x in range (0,3):
            xList = []
            for i in range (0,3):
                newHouse = House()
                newHouse.add_observer(self)
                pop = len(newHouse.getMonsterList())
                if(pop > 0):
                    self.winNum = self.winNum + 1
                xList.append(newHouse)
            self.newList.append(xList)
    
    def getHouseGrid(self):
        """
        returns:
            self.newList, list containing 3x3 grid of houses
        """
        return self.newList
    
    
    def update(self, object):
        """
        called whenever a house is cleared
        announces a house has been cleared,
        adds 1 to the number of cleared houses
        and ends the game if all houses are cleared
        args:
            object:
                cleared house
        """
        
        
        print("house cleared!")
        self.clearCount = self.clearCount + 1
        if (self.clearCount == self.winNum):
            print("All houses cleared, congratulations!")
            print("The last remaining monsters turn back into humans,")
            print("as the rays of the morning sun vanquish the terrible night")
            print("The neighborhood has been saved, thanks your efforts")
            print("As you get ready for your well deserved rest,")
            print("you think that all is at peace")
            print("...until the next halloween")
            print("THE END")
            sys.exit()
        else:
            x = self.winNum - self.clearCount
            print("good job,", x, "houses to go!")
            
    
    
 
    

    

class Game():
    """
    starts game when game is called
    prints into message and runs game
    creates neighborhood, player, and stores player location
    """
    
    def __init__(self):
        player = Player()
        neighborhood = Neighborhood()
        lat = 0
        lon = 0
        ourGrid = neighborhood.getHouseGrid()
        ourHouse = ourGrid[lat][lon]
        print("Bad candy has turned everyone in your neighborhood into freaky monsters!")
        print("You must go from house to house, defeating the monsters,")
        print("and turn everyone back to normal")
        print("Your neighborhood is a 3x3 row of houses")
        print("You start in the north west house")
        print("Clear each monster infested house to win")
        print("Empty houses don't have to be cleared")
        print("Good luck!")
        print("What a horrible night to go trick or treating")
        while (True):
            ourMonsterList = ourHouse.getMonsterList()
            command = input("enter your command:")
    

            if (command == "go north"):
                if (lat > 0):
                    lat = lat - 1
                    ourHouse = ourGrid[lat][lon]
                    print("you went north")
                else:
                    print("you've already reached the north end of the map")
    
            elif (command == "go south"):
                if (lat < 2):
                    lat = lat + 1
                    ourHouse = ourGrid[lat][lon]
                    print("You went south")
                else:
                    print("You've already reached the south end of the map")
                

            elif (command == "go west"):
                if (lon > 0):
                    lon = lon - 1
                    ourHouse = ourGrid[lat][lon]
                    print("you went west")
                else:
                    print("You've already reached the west end of the map")
    
            elif (command == "go east"):
                if (lon < 2):
                    lon = lon + 1
                    ourHouse = ourGrid[lat][lon]
                    print("You went east")
                else:
                    print("You've already reached the east end of the map")
    
            elif (command == "attack"):
                player.attackEnemy(ourMonsterList)
                print("")
                print("monster's turn!")
                for item in ourMonsterList:
                    item.attack(player)
                    self.loseCheck(player)
                print("player now at", player.getHP(), "health!")
        
            elif (command == "show monsters"):
                for item in ourMonsterList:
                    print(item.getName())
                    print(item.getHP())
                x = len(ourMonsterList)
                if(x == 0):
                    print("House is empty!")
    
            elif (command == "show stats"):
                player.displayStats()
        
            elif (command == "quit"):
                print("quitting game")
                sys.exit(0)
   
            elif (command == "help"):
                print("to move in a directiontype:go north,  go south, go east, or go west")
                print("to attack the monsters in the house, type:attack")
                print("to show monsters and monster health, type:show monsters")
                print("to show player health and ammo, type:show stats")
                print("to quit, type:quit")

            else:
                print("Command not recognized, type help for list of valid commands")
                
                
    def loseCheck(self, player):
        """
        method to check if player has lost the game by checking player hp
        args:
            player, player object to be checked
        """
        x = player.getHP()
        if (x <= 0):
            print("Player was defeated!")
            print("Game Over!")
            sys.exit(0)
        
        
ourgame = Game()
