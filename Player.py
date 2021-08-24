class Player:
    def __init__(self, name, cards, points = 0, godSpell=1, resurrectSpell=1):
        self.name = name
        self.points = points
        self.godSpell=godSpell
        self.resurrectSpell=resurrectSpell
        self.cards=cards

    def getName(self):
        return self.name

    def getPoints(self):
        return str(self.points)
    
    def addPoint(self):
        self.points += 1


    def useGod(self, opponent, number):
        if self.godSpell < 1:
            return 0
        card2 = opponent.cards[number-1]
        del(opponent.cards[number-1])
        self.godSpell -= 1
        return card2

    def useResurrect(self, card):
        if self.resurrectSpell < 1:
            return 0
        
        self.resurrectSpell-=1
        self.cards.insert(0, card)
        return 1

