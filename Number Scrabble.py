#Defining
numbers = [1,2,3,4,5,6,7,8,9]
player1=[]
player2=[]
here = 0
over = False
draw = False

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
        print "Player ",player," : ",
        pick = input()
        print ""
        
        # Check if number is available 
        while numbers.count(pick) == 0 :
            print "Sorry, This number is already picked. Pick another one ! :)"
            print "Player ",player," : ",
            pick = input()
            print ""

        # Input separation
        if player == 1 :
            player1.append(pick)
            players = player1
        else :
            player2.append(pick)
            players = player2

        # If player has 3 inputs (Minimum)
        if len(players) == 3 :
            if sum(players) == 15:
                over = True
                
        threeIt = sum(players) - 15
        
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
            print 'Player 1 wins :) !'
            break
        elif over and player == 2 :
            print 'Player 2 wins :) !'
            break
        
        # None won so complete the game ..
        else :
            numbers.remove(pick)
            numbers.insert(pick-1,"-")

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
