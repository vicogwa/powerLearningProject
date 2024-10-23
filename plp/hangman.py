word = str(input("Enter a secret word: ")).lower() 
guesses=[]
wrong_guess =[]
 # Initialize the secret word with underscores
secret_word = "_" * len(word) 

def guess():
    guesses_letter = input("Guess a letter: ").lower()
    while len(guesses_letter) != 1:
        guesses_letter = input("Please guess one letter: ").lower()
    return guesses_letter   

def check_guess(guess):
    global word
    global secret_word
    # Convert secret_word to a list for easier manipulation
    my_word = list(secret_word)  
    for i in range(len(word)):
        if word[i] == guess:
            # Replace the underscore with the guessed letter
            my_word[i] = guess 
            # Convert list back to a string 
    return ''.join(my_word)  

while word != secret_word:
    print("The secret word is: " + secret_word)
    new_guess = guess()
    if new_guess not in guesses:
        guesses.append(new_guess) 
    secret_word = check_guess(new_guess)
    if new_guess not in word and new_guess not in wrong_guess:
        wrong_guess.append(new_guess)
        print("you have guess " + str(guesses))
        print("these has been a wrong guesses " + str(wrong_guess))

    else:
        

        print(f"Guesses so far: {guesses} Try more letter")

print("\nCongratulations! You've guessed the word: " + word)