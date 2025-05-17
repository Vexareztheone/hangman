#Step 1
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
#Step 2
#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
#Step 3
#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
#Step 4
#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
#TODO-2: - If guess is not a letter in the chosen_word,
#Then reduce 'lives' by 1. 
#If lives goes down to 0 then the game should stop and it should print "You lose."
#TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
#Step 5
#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
#TODO-2: - Import the stages from hangman_art.py and make this error go away.
#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
#TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
#TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
# print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}\n ")

import random
from hangman_words import word_list
from hangman_art import logo, stages


display = []
guessed_word = ''
lives = 6
chosen_word = random.choice(word_list)
end_of_game = False
guessed_letters = []
#Create blanks
for character in chosen_word:
    display.append("_")
print(logo)
while not end_of_game:
    guess = input("Guess a letter: \n").lower()
    #Check guessed letter
    if guess in guessed_letters:
        print(f"The letter '{guess}' has alreay been guessed, please try a different one.\n {stages[lives]}")
    else:
        guessed_letters.append(guess)
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = guess             
        if guess not in chosen_word:    
            lives -= 1  
        if lives == 0:
            print(f"{stages[0]}\n Letter '{guess}' is not in the word, no lives left. The word was {chosen_word}. You lose.")
            break
        elif guess in chosen_word:
            print(f"The letter '{guess}' is in the word!")
        else:
            print(f"{stages[lives]}\n The letter '{guess}' is not found in the word! {lives} lives left!")
        print(f"{' '.join(display)}")
        if "_" not in display:
            end_of_game = True
            print(f"You win. The word is '{chosen_word}'. You won with {lives} lives left.\n {stages[lives]}")
guessed_letters = list(dict.fromkeys(guessed_letters))
print(f"You tried these letters: {' '.join(guessed_letters)}.")