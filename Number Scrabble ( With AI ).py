#Defining
numbers = [1,2,3,4,5,6,7,8,9]
player1=[]
computer=[]
here = 0
over = False
draw = False
import random

# Rules :
print "Number Scrabble"
print "Pick a number only once ( from 1 to 9 ) so the sum of 3 chosen numbers (at least) equal 15"

# Game start
while True :
    for player in range (1,3) :
        
        # Print all available numbers
        for x in numbers :
            print '[ ',x,' ]',
        print ''
        
        # Pick a number
        if player == 1 :
            print "Player 1 : ",
            pick_1 = input()
            
            # Check if number is available 
            while numbers.count(pick_1) == 0 :
                print "Sorry, This number is already picked. Pick another one ! :)"
                print "Player 1 : ",
                pick_1 = input()
                
            player1.append(pick_1)
            players = player1
            
            numbers.remove(pick_1)
            numbers.insert(pick_1 - 1, 0)

        if player == 2 :
            print "Computer : ",
            
            pick_2 = random.choice (numbers)
                
            if len(player1) == 2 and sum(player1) < 15 and sum(player1) >= 6 and numbers.count(15 - sum(player1)) != 0 :
                pick_2 = 15 - sum(player1)

            if len(computer) == 2 and sum(computer) < 15 and sum(computer) >= 6 and numbers.count(15 - sum(player1)) != 0 :
                pick_2 = 15 - sum(computer)
                
            if len(computer) == 3 :
                for i in range(0,3):
                    pickThree = 15 - ( sum(computer) - computer[i] )
                    if numbers.count(pickThree) != 0 :
                        pick_2 = pickThree
                
            while pick_2 == 0 or numbers.count(pick_2) == 0 :
                pick_2 = random.choice (numbers)
                     
            computer.append(pick_2)
            players = computer

        
            numbers.remove(pick_2)
            numbers.insert(pick_2 - 1, 0)
                    
            print pick_2
            
        threeIt = sum(players) - 15
        
        # If player has 3 inputs (Minimum)
        if len(players) == 3 :
            if sum(players) == 15:
                over = True
        
        # If player has 4 inputs
        if len(players) == 4 :
            if players.count(threeIt) != 0 :
                over = True

        # If player has 5 inputs (Maximum)
        if len(players) == 5 :
            for i in range (0,5) :
                fourIt = threeIt - players[i]
                if players.count(fourIt) != 0 and fourIt != players[i] :
                    over = True
                    break
                
        # who's exactly won !
        if over and player == 1 :
            print 'Player 1 Wins :) !'
            break
        elif over and player == 2 :
            print 'You Lose :( !'
            break

        # Draw
        if here == 4:
            draw = True
            break
        
    # Counter
    here = here + 1
    
    if over or draw :
        break
    
if draw :
    print "Draw !"
