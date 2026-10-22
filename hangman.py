
import random
import json
import os

# =====================================
# HANGMAN PRO - PYTHON MINI PROJECT
# =====================================

SAVE_FILE = "hangman_data.json"

WORD_BANK = {
    "easy": {
        "python": "A popular programming language",
        "apple": "A fruit that can be red or green",
        "chair": "You sit on it",
        "tiger": "A large striped wild cat",
        "water": "A liquid essential for life",
        "plant": "A living thing that grows in soil"
    },
    "medium": {
        "computer": "An electronic device used for computing",
        "keyboard": "Used to type on a computer",
        "college": "A place where students pursue higher education",
        "internet": "A worldwide network",
        "rainbow": "A colourful arc seen after rain",
        "diamond": "A very hard precious stone"
    },
    "hard": {
        "algorithm": "A step-by-step problem-solving method",
        "developer": "A person who builds software",
        "artificial": "Made by humans rather than occurring naturally",
        "programming": "The process of writing instructions for computers",
        "cybersecurity": "Protecting systems and data from digital attacks",
        "database": "An organized collection of information"
    }
}

HANGMAN_PICTURES = [
    """
     +---+
     |   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """
]

ATTEMPTS_BY_LEVEL = {
    "easy": 8,
    "medium": 6,
    "hard": 5
}


def load_data():
    """Load saved scores and statistics."""
    default_data = {
        "high_score": 0,
        "games_played": 0,
        "wins": 0,
        "losses": 0,
        "total_score": 0
    }

    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as file:
            saved_data = json.load(file)

        if not isinstance(saved_data, dict):
            return default_data

        for key, value in default_data.items():
            if (
                key not in saved_data
                or type(saved_data[key]) is not int
                or saved_data[key] < 0
            ):
                saved_data[key] = value

        return saved_data

    except (OSError, json.JSONDecodeError):
        return default_data


def save_data(data):
    """Save progress between sessions."""
    try:
        with open(SAVE_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    except OSError:
        print("Warning: Progress could not be saved.")


def choose_difficulty():
    print("\nChoose Difficulty")
    print("1. Easy   (8 attempts)")
    print("2. Medium (6 attempts)")
    print("3. Hard   (5 attempts)")

    options = {
        "1": "easy",
        "2": "medium",
        "3": "hard"
    }

    while True:
        choice = input("Enter choice (1-3): ").strip()

        if choice in options:
            return options[choice]

        print("Invalid choice. Please enter 1, 2, or 3.")


def display_word(word, guessed_letters):
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in word
    )


def calculate_score(word, attempts_left, hints_used):
    """Reward longer words and remaining attempts."""
    return max(
        10,
        len(word) * 10 + attempts_left * 5 - hints_used * 10
    )


def play_game(data):
    difficulty = choose_difficulty()
    words = WORD_BANK[difficulty]
    word = random.choice(list(words.keys()))
    hint = words[word]

    guessed_letters = set()
    wrong_letters = set()
    attempts = ATTEMPTS_BY_LEVEL[difficulty]
    hints_used = 0
    won = False

    print("\n" + "=" * 35)
    print("        HANGMAN PRO")
    print("=" * 35)
    print("Difficulty:", difficulty.upper())
    print("Hint: Type 'hint' to reveal a clue.")
    print("Type 'quit' to return to the menu.")

    while attempts > 0:
        print(HANGMAN_PICTURES[
            min(len(wrong_letters), len(HANGMAN_PICTURES) - 1)
        ])

        print("Word:", display_word(word, guessed_letters))
        print("Wrong guesses:", " ".join(sorted(wrong_letters)) or "None")
        print("Attempts left:", attempts)

        if all(letter in guessed_letters for letter in word):
            won = True
            break

        guess = input("Guess a letter: ").strip().lower()

        if guess == "quit":
            print("Round cancelled. Returning to menu.")
            return

        if guess == "hint":
            if hints_used == 0:
                print("Hint:", hint)
                hints_used += 1
            else:
                print("You have already used your hint.")
            continue

        if len(guess) != 1 or not guess.isalpha():
            print("Enter one letter from A to Z.")
            continue

        if guess in guessed_letters or guess in wrong_letters:
            print("You already guessed that letter!")
            continue

        if guess in word:
            guessed_letters.add(guess)
            print("Correct guess!")
        else:
            wrong_letters.add(guess)
            attempts -= 1
            print("Wrong guess!")

    # Show the final state.
    print(HANGMAN_PICTURES[
        min(len(wrong_letters), len(HANGMAN_PICTURES) - 1)
    ])

    if won or all(letter in guessed_letters for letter in word):
        score = calculate_score(word, attempts, hints_used)
        data["wins"] += 1
        data["total_score"] += score

        if score > data["high_score"]:
            data["high_score"] = score
            print("NEW HIGH SCORE!")

        print("Congratulations! You guessed:", word)
        print("Points earned:", score)
    else:
        data["losses"] += 1
        print("Game over! The word was:", word)

    data["games_played"] += 1
    save_data(data)


def show_statistics(data):
    print("\n======= GAME STATISTICS =======")
    print("Games played:", data["games_played"])
    print("Wins:", data["wins"])
    print("Losses:", data["losses"])
    print("Total points:", data["total_score"])
    print("High score:", data["high_score"])

    if data["games_played"] > 0:
        percentage = data["wins"] / data["games_played"] * 100
        print("Win percentage: {:.1f}%".format(percentage))
    else:
        print("Win percentage: 0.0%")

    print("===============================")


def main():
    data = load_data()

    print("\nWelcome to HANGMAN PRO!")
    print("Your saved high score:", data["high_score"])

    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Play Game")
        print("2. View Statistics")
        print("3. View Instructions")
        print("4. Exit")
        print("==============================")

        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            play_game(data)
        elif choice == "2":
            show_statistics(data)
        elif choice == "3":
            print("\nGuess the secret word one letter at a time.")
            print("Each wrong guess uses one attempt.")
            print("Type 'hint' for a clue, or 'quit' to cancel.")
            print("Guess all letters to win and earn points.")
        elif choice == "4":
            save_data(data)
            print("Your progress has been saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
