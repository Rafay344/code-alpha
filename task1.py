import random

words = ["python", "computer", "gaming", "program", "keyboard"]

word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("🎮 Welcome to Hangman! - task1.py:10")

while wrong_guesses < max_wrong:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord: - task1.py:21", display_word)
    print("Wrong guesses: - task1.py:22", wrong_guesses, "/", max_wrong)

    if all(letter in guessed_letters for letter in word):
        print("🎉 Congratulations! You guessed the word: - task1.py:25", word)
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter one letter only. - task1.py:31")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter. - task1.py:35")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct guess! - task1.py:41")
    else:
        wrong_guesses += 1
        print("❌ Wrong guess! - task1.py:44")

else:
    print("\n💀 Game Over! - task1.py:47")
    print("The word was: - task1.py:48", word)