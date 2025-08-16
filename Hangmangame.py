import random

def hangman():
    words = ["python", "hangman", "programming", "developer", "code"]
    word_to_guess = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    word_display = "_" * len(word_to_guess)

    print("Welcome to Hangman!")
    print("Guess the word: " + " ".join(word_display))

    while incorrect_guesses < max_incorrect_guesses and "_" in word_display:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Good guess!")
           
            word_display = "".join([letter if letter in guessed_letters else "_" for letter in word_to_guess])
        else:
            incorrect_guesses += 1
            print(f"Incorrect guess! You have {max_incorrect_guesses - incorrect_guesses} guesses left.")

        print("Current word: " + " ".join(word_display))

    if "_" not in word_display:
        print("Congratulations! You've guessed the word: " + word_to_guess)
    else:
        print("Sorry, you've run out of guesses. The word was: " + word_to_guess)

if __name__ == "__main__":
    hangman()
