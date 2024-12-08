import random
from hangman_words import word_list

print("\n------------- Word Guessing Game -------------\n\n")
word_guess_count = 3
is_guessed = False
letter_guessed = False
word_to_guess = random.choice(word_list).lower()
guessed_letter = ""
place_string = "_" * len(word_to_guess)
letter_place_count = 0
place_list = list(place_string)
fill_word = ""

while not is_guessed:
    if word_guess_count > 0:
        for string in place_list:
            fill_word += string
        print(f"Word to guess: {fill_word}")
        word_guessed = False
        letter_guessed = False
        letter_place_count = 0
        guessed_letter = input("Guess a letter: ")
        word_guess_count -= 1
        for letter in word_to_guess:
            if letter == guessed_letter:
                letter_guessed = True
                fill_word = ""
                letter_place_count += 1
                place_list[letter_place_count-1] = guessed_letter
            else:
                letter_place_count += 1
                fill_word = ""
        if letter_guessed:
            print("The letter you guessed is in the word!\n")
        else:
            print("The letter you guessed is not in the word!\n")
    else:
        for string in place_list:
            fill_word += string
        print("------------- Final Turn -------------\n")
        print(f"Word to guess: {fill_word}")
        guessed_word = input("This is the final turn, please guess the word: ").lower()
        if guessed_word == word_to_guess:
            print("You guessed the correct word!")
            is_guessed = True
        else:
            print("You guessed the wrong word!")
            print(f"The word is {word_to_guess}\n")
            is_guessed = True