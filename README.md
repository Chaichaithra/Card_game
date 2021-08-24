# Card_game

Exercise : Card Game in Python
Game Mechanics: The game is a card game between two entities. The game can be played between two humans or a human and a machine. Choose a set of characters(fictional or real) and their characteristics. Characteristics are represented by a specific numeric value indicating the strength of the characteristic (strength may be indicated by negative or positive numeric value). Each card contains only one character and its characteristics. 
Characteristics must be same across all characters but can vary in strength. No characteristic across characters can share the same value. 
The two entities will be called Player 1 and Player 2 hence. 
Distribute the cards equally among player 1 and player 2 face down such that the players cannot see the characters they have been given. Simulate a dice throw by both player 1 and player 2 where the highest number starts first 
Constraints : Each player gets two special spells (God and Resurrect) . These spells are not associated to the characters but is assoicated to the player itself 
Each round is played as below: 
Player 1 : chooses the first card from the deck and can : play a charactertistic he wishes to challenge player 2 with . Player 2 chooses the first card in his deck and compares the charactertistic. The round is won by the Player whose characteristic weighs more and gets 1 point. The 2 cards are then kept faced down on a different deck called 'outdated'(the cards in the outdated deck are schuflled in a random order after each card placed). In round 2 , The player who won the previous round begins by choosing the next card in his deck and the round proceeds as above. 
Spells: 
In each round a player can decide to play the God spell or the Resurrect spell along with challenging with a characteristic. 
God Spell: The player who starts the round must choose the next card and characteristic on his deck. After choosing he can play the God spell, forcing the opponenet player to play any card that he chooses. The game proceeds with the comparision of the the charactestic on the choosen card. 
Resurrect Spell: Before choosing the next card and characteristic, the player who starts the round can choose Resurrect spell. Choosing Resurrect will create a random number and the card at the that random number position from the 'outdated' deck will be choosen. The card present at the random number at the 'outdated' deck will be added back to the top of the player deck. The player must then play this card. 
When Player 1 plays the God spell , Player 2 cannot play the God spell as he is forced to choose the card, however player 2 can play the Resurrect spell and add a new card to the top of his deck. Player 1 can then force the resurrected card to be choosen or can go with his earlier choice. 
God and Resurrect spell can only be played once by each Player. 
The Game ends when all cards of one / both players have been played. 
The game is won by the player with maximum points. 
Please note : the game mechanics is not perfect and can imbalence the game , but for the purpose of this exercise that can be overlooked. 


Algorithm 

Step 1   :   Start
Step 2   :   create cards(6)
Step 3   :   declare empty list outdated, and round_count, scores,special_spells, prev_round_winner
Step 4   :   Shuffle the cards
             shuffle(deck)
Step 5   :  Roll a dice using 
            random.randint(1,6)
Step 5.1 :  Display the results 
Step 6   :  Append the outdated deck and reshuffle 
            self.outdated.append(char)
            shuffle(self.outdated)
        
Step 7   : randomly pick a card and update outdated_deck

Step 8   : randomly select an integer r and 
           if r is 1 then "god spell"
           if r is 2 then "resurrect spell"
           else return None 

Step 9   : if spell is resurrect then pick one random card from outdated cards and players card 
           if spell is god then pick a random card from players cardsAlgorithm 

Step 1   :   Start
Step 2   :   create cards(6)
Step 3   :   declare empty list outdated, and round_count, scores,special_spells, prev_round_winner
Step 4   :   Shuffle the cards
             shuffle(deck)
Step 5   :  Roll a dice using 
            random.randint(1,6)
Step 5.1 :  Display the results 
Step 6   :  Append the outdated deck and reshuffle 
            self.outdated.append(char)
            shuffle(self.outdated)
        
Step 7   : randomly pick a card and update outdated_deck

Step 8   : randomly select an integer r and 
           if r is 1 then "god spell"
           if r is 2 then "resurrect spell"
           else return None 

Step 9   : if spell is resurrect then pick one random card from outdated cards and players card 
           if spell is god then pick a random card from players cards

Step 10  : compare the characteristics and decide the winner update round_count 
           
Step 11  :  Display the Winner(player1 / player 2/ tie)    


Step 10  : compare the characteristics and decide the winner update round_count 
           
Step 11  :  Display the Winner(player1 / player 2/ tie)    
