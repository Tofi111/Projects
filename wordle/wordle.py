import random
NUM_OF_ATTEMPTS = 5
def choose_word(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return random.choice(words)

def check_guess(secret_word, guessed_word):

    mismatched_letters = [guessed_char for secret_char, guessed_char in zip(secret_word, guessed_word) if
                          secret_char != guessed_char]

    correct_positions = sum(c1 == c2 for c1, c2 in zip(secret_word, guessed_word))
    incorrect_positions = len(mismatched_letters)


    feedback = f"Correct positions: {correct_positions}/{len(secret_word)}\n"
    feedback += f"Mismatched positions: {incorrect_positions}/{len(secret_word)}\n"
    feedback += f"Incorrect letters: {', '.join(mismatched_letters)}"

    return feedback

def wordle_game():
    file_path = 'word_list.txt'
    secret_word = choose_word(file_path)
    attempts = 0

    print("Welcome to Wordle!")
    print("Try to guess the secret word.")

    for i in range(1, NUM_OF_ATTEMPTS + 1):
        print(f"Attempt {i}: ")
        guess = input("Enter your guess: ").lower()

        if guess == secret_word:
            print(f"Congratulations! You guessed the word '{secret_word}' in {attempts} attempts.")
            exit()
        else:
            feedback = check_guess(secret_word, guess)
            print(feedback)
            attempts += 1

    print(f"The correct word was {secret_word}")



if __name__ == "__main__":
    wordle_game()
