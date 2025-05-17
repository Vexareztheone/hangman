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