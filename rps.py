import random

def check(comp, user):
   
    if user == 0:  
        if comp == 3:  
            return 1
        elif comp == 8:  
            return -1
        elif comp == 9:  
            return 0
    elif user == 1:  
        if comp == 4:  
            return 1
        elif comp == 5:  
            return -1
        elif comp == 9:  
            return 0
    elif user == 2:  
        if comp == 6: 
            return 1
        elif comp == 7:  
            return -1
        elif comp == 9: 
            return 0
    
    if comp == user:
        return 0
    if (comp == 0 and user == 1) or (comp == 1 and user == 2) or (comp == 2 and user == 0):
        return -1
    return 1

def tournament():
    print("Welcome to the Rock-Paper-Scissors Tournament!")
    print("In this tournament, you will play a series of rounds against the computer.")
    print("You score 1 point for each win.")
    print("At the end of the tournament, the player with the most points wins!")
    
    
    special_moves = {3: 'Rockslide', 4: 'Paper Plane', 5: 'Tornado', 6: 'Scissor Storm', 7: 'Fireball', 8: 'Lightning Strike', 9: 'Dynamite'}

    while True:
        num_rounds = int(input("Enter the number of rounds you want to play: "))
        if num_rounds <= 0:
            print("Please enter a valid number of rounds (greater than 0).")
        else:
            break

    player_score = 0
    moves = ['rock', 'paper', 'scissors']

    for round_num in range(num_rounds):
        comp = random.randint(0, 2)
        user = int(input("Enter 0 for rock, 1 for paper, 2 for scissors, or 3-9 for special moves: "))
        
        if user >= 3 and user <= 9:
            print("You used a special move:", special_moves[user])
        else:
            print("You chose:", moves[user])

        print("Computer chose:", moves[comp])

        score = check(comp, user)
        print("\nRound", round_num + 1)

        if score == 0:
            print("It's a draw")
        elif score == -1:
            print("You lose")
        else:
            print("You won!")
            player_score += 1

    print("\nTournament Over!")
    print("Your score:", player_score, "out of", num_rounds)
    if player_score > num_rounds // 2:
        print("Congratulations! You won the tournament!")
    elif player_score == num_rounds // 2:
        print("It's a tie!")
    else:
         print("You lost the tournament")

tournament()
