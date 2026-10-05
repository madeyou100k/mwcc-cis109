import random

wordlist = [
    "cyber",
    "labradoodle",
    "security"
]

word = wordlist[random.randint(0, len(wordlist) - 1)]
board = list("_" * len(word))
bad_guesses = []
max_wrong = 6

while len(bad_guesses) < max_wrong and "_" in board:
    print()

    print("Welcome to HANGMAN!")
    print()

    match len(bad_guesses):
        case 0:
            print("")

        case 1:
            print("""
+---+
|
|
|
|
=======
""".strip())

        case 2:
            print("""
+---+
|   |
|
|
|
=======
""".strip())

        case 3:
            print("""
+---+
|   |
|   0
|
|
=======
""".strip())

        case 4:
            print("""
+---+
|   |
|   0
|   |
|
=======
""".strip())

        case 5:
            print("""
+---+
|   |
|   0
|  /|\
|
=======
""".strip())

    print()
    print(board)
    print()
    print("Bad Guesses:", bad_guesses)
    print()

    guess = input("Guess a letter: ").lower()

    # Validate Input
    if len(guess) != 1 or not guess.isalpha():
        print("\n⚠️ Please enter one letter.")
        input("Press [enter] to continue.")
        continue

    if guess in bad_guesses or guess in board:
        print("\n⚠️ You already guessed that letter!")
        input("Press [enter] to continue.")
        continue

    is_found = False

    for i, letter in enumerate(word, start=0):
        if letter == guess:
            board[i] = word[i]
            is_found = True

    if is_found:
        print(f"\n✅ '{guess}' is in the word!")
    else:
        bad_guesses.append(guess)
        print(f"\n❌ '{guess}' is not in the word.")

    input("Press [enter] to continue.")

if "_" not in board:
    print(f"\n🎉 YOU WON! The word was '{word}'")
else:
    print("""
+---+
|   |
|   0
|  /|\
|  / \
=======
""".strip())

    print(f"\n💀 YOU LOST! The word was '{word}'")

print("\nThank you for playing!")
