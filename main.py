import random
attempts_list = []
def show_():
    if len(attempts_list) <= 0:
        print("There is currently no high score, its yours for the taking!")
    else:
            print("The current high score is {} attempts".format(min(attempts_list)))
def start_game():
    random number = int(random.randint(1,10))
    print("Hey there! Welcome to the game of guesses!")
    player_name = input("Enter your name!")
    wanna_play = input("Hi, {}, would you like to play the guessing game? (Enter Yes/No)".format(player_name))
    ##Where the show_score function USED to be
    attempts = 0 
    show_score()
    while wanna_play.lower() == "yes":
        try:
             guess = input("Pick a number between 1 and 10 ")
             if int(guess) < 1 or int(guess) > 10: 
                  raise ValueError("Please guess a number within the given range")
             if int(guess) == random_number:
                  print("Congrats! You guessed it right!")
                  attempts