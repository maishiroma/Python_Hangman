# using this site: http://www.practicepython.org

# Selects a random word from the given text file
def get_random_word(file_name):
    import random
    with open(file_name, "r") as open_file:
        # takes out all of the file and stuffs it into a list.
        words = open_file.readlines()
        rand_numb = random.randint(0,len(words)-1)
        return words[rand_numb].strip()

def hangman_game():
    print("Welcome to Hangman: Python Edition!")
    while True:
        key = get_random_word("sowpods.txt")
        key_list = list(key)
        game_board = ["_"] * len(key)
        incorrect_guess_set = set()
        correct_guess_set = set()
        # We are using a set to make sure we only get unique elements in it.
        # However, the items in the set should be immutable, meaning lists are not allowed to be in a set
        while True:
            # If the player either guessed incorrectly 6 times or completes the board, the game ends
            if len(incorrect_guess_set) == 6:
                print("Oh no! You lost! The word was " + key + ".")
                break
            elif print_hangman(game_board) == True:
                print("Congrats! The word was " + key + ".")
                break
            else:
                guess = raw_input("Enter a character: ").upper()
                # This if statement is unique in that sets are specialized in finding elements in it of it can.
                if guess in incorrect_guess_set or guess in correct_guess_set:
                    print("You already guessed that!")
                else:
                    # Checks if the player guessed right and add them to the respective sets
                    if check_hangman(game_board, key_list, guess) == False:
                        print("Incorrect...")
                        incorrect_guess_set.add(guess)
                    else:
                        print("Nice job!")
                        correct_guess_set.add(guess)

                # Prints out the player's wrong guesses if it's not empty
                print_hangman_wrong_guess(incorrect_guess_set)
                graphic_hangman(len(incorrect_guess_set))
                print("\n")

        user = raw_input("Would you like to play again? yes or no: ")
        if user != "yes":
            print("Take care.")
            break

# checks the selected guess and compared it to the key_list and returns true if the guess was found in the list
# This method also appends to the original game_board, since the list was not REASSIGNED completely
# the game board and key_list should be the same length
def check_hangman(game_board, key_list, guess):
    correct = False
    for index in range(len(key_list)):
        if key_list[index] == guess:
            game_board[index] = guess
            correct = True

    return correct

# Prints the entire board to the screen.  Returns true if there no more empty spots in the board
def print_hangman(game_board):
    result = ""
    if "_" in game_board:
        for char in game_board:
            result = result + char + " "

        print result[0:len(result)-1]
        return False
    return True

# Prints out the player's guesses in a nice format
def print_hangman_wrong_guess(guesses):
    if len(guesses) > 0:
        result = "Wrong Letters: "
        for guess in guesses:
            result = result + guess + ", "

        print result[0:len(result)-2]

# prints a graphic representation of the wrong guesses.
# This works by building up the man dynamically
def graphic_hangman(numb_wrong):
    # If the player has at least one wrong guess
    if numb_wrong > 0:
        print("  O")

    # If the player has wrong guesses in the range from 2 to 4, the body and arms are drawn
    if numb_wrong == 2:
        print("  |")
    elif numb_wrong == 3:
        print(" -|")
    elif numb_wrong == 4:
        print(" -|-")
    elif numb_wrong > 4:
        # If the player has more than 4 wrong, the entire torso is drawn and the legs are then drawn.
        print(" -|-")

        if numb_wrong == 5:
            print(" /")
        else:
            print(" / \\")

# main execution
# By using the build in __name__, we can allow for a way to tell Python to go into this and act it as a main method...
if __name__ == "__main__":
    hangman_game()
