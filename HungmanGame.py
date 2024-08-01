import random

def get_random_word():
    words = ['python', 'java', 'kotlin', 'javascript', 'hangman', 'programming']
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    return displayed_word

def play_hangman():
    word = get_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    
    print("Welcome to Hangman!")
    
    while incorrect_guesses < max_incorrect_guesses:
        print("\nCurrent word: ", display_word(word, guessed_letters))
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            if set(word) == guessed_letters:
                print(f"\nCongratulations! You've guessed the word: {word}")
                break
        else:
            guessed_letters.add(guess)
            incorrect_guesses += 1
            print(f"Incorrect guess. You have {max_incorrect_guesses - incorrect_guesses} incorrect guesses left.")
        
        if incorrect_guesses == max_incorrect_guesses:
            print(f"\nSorry, you've run out of guesses. The word was: {word}")

if __name__ == "__main__":
    play_hangman()
