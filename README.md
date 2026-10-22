# Datheon_Python_Programming_Internship
Python programming projects for the Datheon internship.
1.🎮 Hangman Pro — Python Game

A feature-rich, console-based Hangman word-guessing game built with Python. This project is designed to practise Python programming concepts while creating an interactive game that runs on Pydroid 3 and other Python environments.

📌 Project Overview

Hangman Pro is a word-guessing game where players try to discover a hidden word one letter at a time. Players can select difficulty levels, use hints, earn points, and track their gaming statistics.

✨ Features

- 🎯 Difficulty Levels: Choose Easy, Medium, or Hard.
- 🎨 Hangman Drawing: ASCII illustrations update as incorrect guesses increase.
- 🏆 Scoring System: Earn points based on word length, remaining attempts, and hints used.
- 💡 Hint System: Get a clue to help guess the secret word.
- 🔄 Play Again: Return to the main menu to start another round.
- 📊 Game Statistics: Track games played, wins, losses, total points, and win percentage.
- 💾 Persistent High Score: Save your high score between sessions.
- 📁 JSON Data Storage: Store game progress and statistics locally.
- ✅ Input Validation: Handle invalid inputs and repeated guesses.

🛠️ Technologies Used

- Language: Python 3
- Modules: "random", "json", "os"
- Storage: JSON file
- Platform: Pydroid 3, Windows, Linux, and macOS

No external Python packages are required.

🚀 How to Run

Option 1: Run on Android using Pydroid 3

1. Install and open Pydroid 3.
2. Open the "hangman.py" file.
3. Tap the Run button.
4. Select an option from the main menu.
5. Choose a difficulty level and start guessing letters.

Option 2: Run on a Computer

1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

python hangman.py

On some systems, use:

python3 hangman.py

🎮 How to Play

1. Start the game and select Play Game.
2. Choose Easy, Medium, or Hard.
3. Guess one letter at a time.
4. Type "hint" to get a clue.
5. Type "quit" to cancel the current round and return to the menu.
6. Guess all the letters before your attempts run out to win.
7. Visit Game Statistics to view your progress.

📂 Project Structure

Hangman-Game/
├── hangman.py
├── hangman_data.json  # Created when progress is saved
└── README.md

The "hangman_data.json" file stores your high score and game statistics. It is created automatically when the game saves its progress.

🧠 Python Concepts Practised

- Variables and data types
- Lists, dictionaries, and sets
- Loops and conditional statements
- Functions and modular programming
- Random selection
- File handling
- JSON serialization and deserialization
- Exception handling
- Input validation

🔮 Future Improvements

- Add more words and categories.
- Create a graphical user interface (GUI).
- Add sound effects and animations.
- Introduce player profiles and leaderboards.
- Add timed challenges and achievements.

👨‍💻 Author

vasavikhubaji 

First-year Computer Science and Engineering student learning Python and building programming projects.

📄 License

This project is available for educational and learning purposes. A formal open-source license can be added if the project is published under a specific license.
