import random

def user_input():
    choice = 'Y'
    score = 0
    while(choice == 'Y' or choice == 'y'):
        print("Enter your choice: ")
        print("Enter R for Rock, S for scissors, P for paper.")
        string = input()
        result = main_game(string)                      #This function calls the main_game function to perform necessary oprations after user has given the input.
        if result == 'W':
            score += 1
        elif result == 'L':
            score -= 1
        else:
            score += 0
        print("Your score is:",score)
        choice = input("Do you want to continue?")

def main_game(string):
    lst  = ['R', 'S', 'P']
    opp_choice = random.choice(lst)                          #Picks a random choice for the computer.And the following lines decide who wins.
    if(string == str(opp_choice)):
        print("The match is drawn as both of you have chosen:", string)
        return 'D'
    elif(string == 'R' and str(opp_choice) == 'S'):
        print("You win because you chose Rock while your opponent chose scissors.")
        return 'W'
    elif(string == 'R' and str(opp_choice) == 'P'):
        print("You lost because you chose Rock while your opponent chose Paper.")
        return 'L'
    elif(string == 'S' and str(opp_choice) == 'P'):
        print("You won because you chose Scissors and your opponent went with Paper.")
        return 'W'
    elif(string == 'S' and str(opp_choice) == 'R'):
        print("You lost because you chose Scissors and your opponent went with Rock.")
        return 'L'
    elif(string == 'P' and str(opp_choice) == 'R'):
        print("You won because you chose Paper and your opponent took with Rock.")
        return 'W'
    else:
        print("You lost because you chose Paper while your opponent chose Scissors.")
        return 'L'

if __name__ == "__main__":                                      #This starts the program.
    user_input()