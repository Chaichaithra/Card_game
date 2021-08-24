from Player import Player
from Card import Card
import time
import random
from prettytable import PrettyTable
from colorama import Fore, Back, Style

# chars - name, attackStrength, defense, intelligence, speed, rating)
def createCards():

    superman = Card("Superman", 1)
    batman = Card("Batman", 2)
    flash = Card("Flash", 3)
    hulk = Card("Hulk", 4)
    ironMan = Card("Ironman", 5)
    wonderWoman = Card("Wonderwoman", 6)
    wolverine = Card("Wolverine", 7)
    blackPanther = Card("Black panther", 8)
    captainMarvel = Card("Captain Marvel", 9)
    spiderMan = Card("Spiderman", 10)
    thor = Card("Thor", 11)
    captainAmerica = Card("Captain America", 12)
    starLord = Card("Star Lord", 13)
    aquaMan = Card("Aquaman", 14)
    Magneto = Card("Magneto", 15)
    deadPool = Card("Deadpool", 16)
    phoenix = Card("Phoenix", 17)
    shazam = Card("Shazam", 18)
    loki = Card("Loki", 19)
    greenLantern = Card("Green Lantern", 20)

    return [superman, batman, flash, hulk, ironMan, wonderWoman, wolverine, blackPanther, captainMarvel, spiderMan,
     thor, captainAmerica, starLord, aquaMan, Magneto, deadPool, phoenix, shazam, loki, greenLantern]
        
# Distributes a set of cards to 2 players. Each player gets 7 cards.
def distributeCards(cards, numberOfCardsToEachPlayer = 7):
    randomNumbersList = random.sample(range(0,20),20) # A list of random numbers without replacement
    p1=list() # player 1 cards
    p2=list() # player 2 cards

    for i in range(numberOfCardsToEachPlayer):
        p1.append(cards[randomNumbersList[i]])
        p2.append(cards[randomNumbersList[i + numberOfCardsToEachPlayer]])

    outdated = list() # The rest of the cards are stored in 'outdated' deck
    for i in range(15,20):
        outdated.append(cards[randomNumbersList[i]])

    return p1, p2, outdated

# Simulate throw of a dice. This is a decorator function called when a dice is thrown
def simulateThrow(function):
    def simulate():
        tEnd=time.time() + 1
        while time.time() < tEnd:
            # Print a random number between 1 and 6 in the same place in terminal.
            print(" " + str(random.randrange(1, 7)), end="\b\b")
        res=function() # Get the actual dice throw value
        return res
    return simulate

# Get the dice value which is between 1 and 6
@simulateThrow
def dice():
    return random.randrange(1, 7)
    
# Identifies which player plays first. If the dice value is same,
# the process is repeated.
def identifyFirstPlayer(p1, p2):

    # Get dice value of player 1
    p1DiceValue = dice()
    print(p1.getName() + "'s dice = " + str(p1DiceValue))
    print("\n")

    # Get dice value of player 2
    p2DiceValue = dice()
    print(p2.getName() + "'s dice = " + str(p2DiceValue))

    if p1DiceValue > p2DiceValue: return "Player 1"
    elif p1DiceValue < p2DiceValue: return "Player 2"
    else: 
        # If it's tie, generate random numbers again 
        print("It is a tie. Both should throw dice again.")
        print("\n")
        time.sleep(0.5) # For visual flair
        return identifyFirstPlayer(p1, p2)

# Display card in a table format. Recieves an object of class "Card"
def displayCard(card):
    print("Your card:", end="\n")
    table = PrettyTable([card.getName()])
    table.add_row(['1. Attack = ' + card.getAttackStrength()])
    table.add_row(['2. Defense = ' + card.getDefense()])
    table.add_row(['3. Intelligence = ' + card.getIntelligence()])
    table.add_row(['4. Speed = ' + card.getSpeed()])
    table.add_row(['5. Rating = '+ card.getRating()])
    print(table, end="\n")

# Displays the strength of a characteristic of 2 cards.
# name = Name of the characteristic
# char1 = Strength of player1's "name" characteristic
# char2 = Strength of player2's "name" characteristic
def displayComparison(char1, char2, name):
    print("\n")
    print("Your " + name + " = " + str(char1))
    print("Your opponent's " + name + " = " + str(char2))
    print("\n")
    time.sleep(0.35)

# Function to handle when game ends if any player empties cards or abrupt end
def endGame(player1, player2):
    print("\n")
    # Print scoreboard in tabular format.
    print("Scoreboard: ",end="\n")
    table = PrettyTable([player1.getName(), player2.getName()])
    table.add_row([player1.getPoints(), player2.getPoints()])
    print(table)
    print("\n")

    # Identify winner based on the points of each player
    if player1.getPoints() > player2.getPoints(): winner = player1.getName()
    elif player1.getPoints() < player2.getPoints(): winner = player2.getName()
    else: 
        # If tie, end game.
        print("It's a tie. Try again.")
        return
    time.sleep(0.33)

    # Congratulatory message
    print(Fore.YELLOW+"**************************************************************")
    print(Style.RESET_ALL)
    print(Fore.GREEN+"\t\t" + winner + Style.RESET_ALL+" won the game. "+ Fore.RED+"Congratulations!", end="\n")
    print(Style.RESET_ALL)
    print(Fore.YELLOW+"**************************************************************")
    print(Style.RESET_ALL)

def main():
    # Compare Attack characteristic of 2 cards
    def checkAttackStrength(card1, card2):
        char1 = card1.getAttackStrength()
        char2 = card2.getAttackStrength()
        # Display the comparision
        displayComparison(char1, char2, "attack strength")
        if char1 > char2: return 1
        else: return 0

    # Compare Defense characteristic of 2 cards
    def checkDefense(card1, card2):
        char1 = card1.getDefense()
        char2 = card2.getDefense()
        # Display strength of defense characteristic of these 2 cards
        displayComparison(char1, char2, "defense")
        if char1 > char2: return 1
        else: return 0

    # Compare Intelligence characteristic of 2 cards
    def checkIntelligence(card1, card2):
        char1 = card1.getIntelligence()
        char2 = card2.getIntelligence()
        # Display strength of Intelligence characteristic of these 2 cards
        displayComparison(char1, char2, "intelligence")
        if char1 > char2: return 1
        else: return 0
    
    # Compare speed characteristic of 2 cards
    def checkSpeed(card1, card2):
        char1 = card1.getSpeed()
        char2 = card2.getSpeed()
        # Display strength of speed characteristic of these 2 cards
        displayComparison(char1, char2, "speed")
        if char1 > char2: return 1
        else: return 0

    # Compare rating characteristic of 2 cards
    def checkRating(card1, card2):
        char1 = card1.getRating()
        char2 = card2.getRating()
        # Display strength of rating characteristic of these 2 cards
        displayComparison(char1, char2, "rating")
        if char1 > char2: return 1
        else: return 0

    # Master function to handle comparision of characters
    def compareCharacteristics(card1, card2, characteristicNumber):
        print("\n")
        print("Your opponents card: ")
        displayCard(card2)
        # Dictionary to hold function objects
        characteristics = {1: checkAttackStrength, 2: checkDefense, 3: checkIntelligence, 4: checkSpeed, 5: checkRating}
        
        # Call the appropriate function and pass the 2 cards as parameters
        # Return 1 if card1 has greater strength. 0 if card2 has greater strength
        return characteristics[characteristicNumber](card1, card2)
        
    # Handle resurrect spell
    def resurrectSpell(player, playerCards, outdated):
        # index of the card to be chosen from outdated deck
        number = random.randrange(len(outdated))
        
        # Make player relevant changes by calling the "useResurrect" method for player object
        if player.useResurrect(outdated[number]):
            print(player.getName() + " used resurrect spell.")
        else: 
            print("\n")
            # If the player previously used resurrect spell. Then he can't use it again.
            # Display message and continue execution.
            print(player.getName() + "'s resurrect spell potion empty. The card at the top of your deck is chosen.")
        del(outdated[number])
        return

    # Handle resurrect spell. "godplayer" = Player who used god spell.
    def godSpell(godPlayer, opponent):
        # Recieve index of card to be chosen in the opponent deck
        cardNumber = int(input("Which card number should your opponent play between 1 and " +  str(len(opponent.cards)) + " "))
        
        # Make player relevant changes and recieve the chosen card from opponent's deck
        card=godPlayer.useGod(opponent, cardNumber)
        if card:
            print(godPlayer.getName() + " used god spell.")
        else: 
            # If god spell was used before.
            print(godPlayer.getName() + "'s god spell potion is empty.")
        return card
        
        
    # Create superherocards and store all 20 cards
    cards = createCards()

    # Select number of cards to each Player in the second argument for this function.
    # Default is 7 to each player.
    # p1-> Cards of player 1. p2-> Cards of player 2.
    player1Cards, player2Cards, outdated = distributeCards(cards)

    # Create player objects. Pass their respective cards objects as parameters.
    player1 = Player(input("Enter player 1's name : "), player1Cards)
    player2 = Player(input("Enter player 2's name : "), player2Cards)
    print("\n")

    # Identify who has to play first. Can be p1 or p2
    player = player1 if identifyFirstPlayer(player1, player2) == "Player 1" else player2
    
    # god spell has not been used yet
    godBool = False

    while True:
        # Display current player's details
        print("\nIt is " + Fore.CYAN + player.getName() + Style.RESET_ALL + "'s turn.", end="\n\n")

        # If any player has 0 cards, exit the loop and end game.
        if len(player1.cards) < 1 or len(player2.cards) < 1: break

        # Check if player wants to use any spells.
        spell = input("Type 'god' to use god spell or 'res' for resurrect spell. Press Enter to continue : ")
        
        # if player uses resurrect spell
        if spell.lower() == "res":
            resurrectSpell(player, player.cards, outdated)
        # If player uses god spell
        elif spell.lower() == "god":
            # We will use this when identify opponents card.
            godBool=True

        # display current player's card and compare cards
        if player == player1:
            card1 = player1.cards[0]
            # if player chose to use god spell
            if godBool:
                # select opponent's card by calling this function
                card2 = godSpell(player1, player2)
                # If god spell failed, continue normal execution
                if not card2:
                    card2 = player2.cards[0]
                    player1.cards = player1.cards[1:]
                    player2.cards = player2.cards[1:]
                    
            # Select opponents card when god spell isn't used
            else:
                card2 = player2.cards[0]
                player1.cards = player1.cards[1:]
                player2.cards = player2.cards[1:]
                

        else:
            card1 = player2.cards[0]
            # if player chose to use god spell
            if godBool:
                # select opponent's card by calling this function
                card2 = godSpell(player2, player1)
                # If god spell failed, continue normal execution
                if not card2:
                    card2 = player1.cards[0]
                    player1.cards = player1.cards[1:]
                    player2.cards = player2.cards[1:]

            # Select opponents card when god spell isn't used
            else:
                card2 = player1.cards[0]
                player1.cards = player1.cards[1:]
                player2.cards = player2.cards[1:]
        
        # Display card of previous round winner
        displayCard(card1)
        godBool=False
        
        print("\n")
        chararacteristic = int(input("Enter the characteristic's number: "))

        # If prev round winner's card has less strength than opponent player's card
        if not compareCharacteristics(card1, card2, chararacteristic):
            print(Fore.GREEN + player.getName() + " lost"+ Style.RESET_ALL + " this round.")

            #Switch player
            player = player1 if player == player2 else player2

        else:
            print(Fore.GREEN + player.getName() + " won"+ Style.RESET_ALL + " this round.")

        # Add cards to outdated deck
        outdated.insert(0, card1)
        outdated.insert(1,card2) 
        # print("Outdated = "+ str(len(outdated)))

        # Shuffle outdated deck
        random.shuffle(outdated)

        # Add points to the current round winner
        player.addPoint()

        # Check if user wants to terminate game early
        end = input("Do you want to exit ? ")
        if end.lower() == "yes":
            break

    # Endgame if any exception
    endGame(player1, player2)

    
if __name__ == "__main__":
    main()
    