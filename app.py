import random


def select_random_word():
    words = ['python', 'hangman', 'programming', 'computer', 'openai', 'artificial', 'intelligence']
    return random.choice(words)


def display_word_progress(word, guessed_letters):
    return ''.join(letter if letter in guessed_letters else '_' for letter in word)


def play_hangman():
    word = select_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")

    while incorrect_guesses < max_incorrect_guesses:
        print("\n" + display_word_progress(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            print(f"Good guess! {guess} is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Incorrect guess. You have {max_incorrect_guesses - incorrect_guesses} incorrect guesses left.")

        if set(word).issubset(guessed_letters):
            print(f"Congratulations! You guessed the word: {word}")
            break
    else:
        print(f"Sorry, you've been hanged! The word was: {word}")


play_hangman()