import random

class Card:
    char1 = random.sample(range(65,101),20)
    char2 = random.sample(range(65,101),20)
    char3 = random.sample(range(65,101),20)
    char4 = random.sample(range(65,101),20)
    char5 = random.sample(range(65,101),20)
    #characteristics = {1: getAttackStrength, 2: getDefense, 3: getIntelligence, 4: getSpeed, 5: getRating}
        
    def __init__(self, name, cardNumber):
        self.name = name
        self.attackStrength = Card.char1[cardNumber-1]
        self.defense = Card.char2[cardNumber-1]
        self.intelligence = Card.char3[cardNumber-1]
        self.speed = Card.char4[cardNumber-1]
        self.rating = Card.char5[cardNumber-1]
        # self.characteristics = {1: Card.getAttackStrength, 2: Card.getDefense, 3: Card.getIntelligence, 4: Card.getSpeed, 5: Card.getRating}
    
    def getName(self):
        return str(self.name)

    def getAttackStrength(self):
        return str(self.attackStrength)

    def getDefense(self):
        return str(self.defense)

    def getIntelligence(self):
        return str(self.intelligence)
    
    def getSpeed(self):
        return str(self.speed)
    
    def getRating(self):
        return str(self.rating)

    





        