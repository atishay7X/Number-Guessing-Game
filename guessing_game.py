import random

def play_game():
    print("\n🎯 Welcome to the Number Guessing Game!")
    print("=" * 40)

    while True:
        try:
            difficulty = input("\nChoose difficulty:\n  1. Easy   (1–50,  10 guesses)\n  2. Medium (1–100,  7 guesses)\n  3. Hard   (1–200,  5 guesses)\nEnter 1, 2, or 3: ").strip()
            if difficulty not in ("1", "2", "3"):
                print("Please enter 1, 2, or 3.")
                continue
            break
        except KeyboardInterrupt:
            print("\nThanks for playing. Goodbye!")
            return

    settings = {
        "1": (1, 50,  10, "Easy"),
        "2": (1, 100,  7, "Medium"),
        "3": (1, 200,  5, "Hard"),
    }
    low, high, max_guesses, label = settings[difficulty]

    secret = random.randint(low, high)
    guesses_left = max_guesses

    print(f"\n[{label}] I'm thinking of a number between {low} and {high}.")
    print(f"You have {max_guesses} guesses. Good luck!\n")

    while guesses_left > 0:
        try:
            raw = input(f"Guess ({guesses_left} left): ").strip()
            guess = int(raw)
        except ValueError:
            print("  ⚠️  Please enter a whole number.")
            continue
        except KeyboardInterrupt:
            print("\nGame aborted. Goodbye!")
            return

        if guess < low or guess > high:
            print(f"  ⚠️  Out of range! Pick a number between {low} and {high}.")
            continue

        guesses_left -= 1

        if guess == secret:
            used = max_guesses - guesses_left
            print(f"\n🎉 Correct! You got it in {used} guess{'es' if used != 1 else ''}!")
            break
        elif guess < secret:
            hint = "Much higher! 🔥" if secret - guess > (high - low) // 5 else "A bit higher ↑"
        else:
            hint = "Much lower! 🧊"  if guess - secret > (high - low) // 5 else "A bit lower  ↓"

        if guesses_left > 0:
            print(f"  ❌ Wrong — {hint}  ({guesses_left} guess{'es' if guesses_left != 1 else ''} remaining)")
        else:
            print(f"\n💀 Out of guesses! The number was {secret}.")

    play_again = input("\nPlay again? (y/n): ").strip().lower()
    if play_again == "y":
        play_game()
    else:
        print("Thanks for playing. Goodbye! 👋\n")

if __name__ == "__main__":
    play_game()
