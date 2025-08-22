import random

words = ["apple", "chair", "plane", "water", "music"]
secret_word = random.choice(words)
guessed_letters = []
max_wrong_guesses = 6
wrong_guesses = 0

while True:
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_ "
    print("\nWord: ", display_word)

    if all(letter in guessed_letters for letter in secret_word):
        print("🎉 You win! The word was:", secret_word)
        break

    if wrong_guesses >= max_wrong_guesses:
        print("💀 You lose! The word was:", secret_word)
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Good guess!")
    else:
        wrong_guesses += 1
        print("❌ Wrong guess! Mistakes:", wrong_guesses, "/", max_wrong_guesses)
