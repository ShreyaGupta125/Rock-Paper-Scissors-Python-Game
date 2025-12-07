# 🪨 Rock-Paper-Scissors Tournament 🎮

A fun, terminal-based Rock-Paper-Scissors Tournament game written in Python, featuring classic moves plus powerful special moves that can change the outcome of a round in unexpected ways. Inspired by the traditional game but extended with creative mechanics for extra excitement.

# ✨ Features
- 🧠 Play a multi-round tournament against the computer with automatic score tracking.
- 🪨📄✂️ Classic moves: Rock, Paper, Scissors.
- ⚡ Special moves from 3 to 9 with unique names and effects (e.g., Rockslide, Lightning Strike, Dynamite).
- 📊 Final summary showing wins out of total rounds and who wins the tournament.
- 🧾 Clean, simple command-line interface suitable for beginners learning Python game logic.

# 🎮 Game Rules
- On each round, the computer randomly chooses one of:
  - 0 → Rock
  - 1 → Paper
  - 2 → Scissors

- You can choose:
  - 0 → Rock
  - 1 → Paper
  - 2 → Scissors
  - 3–9 → Special moves with custom behavior.

- Scoring:
  - Win → +1 point
  - Draw → 0 points
  - Loss → 0 points
  - At the end:
    - More than half rounds won → 🏆 "You won the tournament!"
    - Exactly half → 🤝 "It's a tie!"
    - Less than half → 💀 "You lost the tournament."

# 💥 Special Moves
The game includes a dictionary of special moves that are triggered when you enter a number from 3 to 9:

special_moves = {
    3: 'Rockslide',
    4: 'Paper Plane',
    5: 'Tornado',
    6: 'Scissor Storm',
    7: 'Fireball',
    8: 'Lightning Strike',
    9: 'Dynamite'
}

When you use a special move, the game prints its name and uses the check(comp, user) function to determine the outcome based on custom cases for values 0–2 vs 3–9 plus the standard rock-paper-scissors rules.

# 🧠 Core Logic

check(comp, user)
- Inputs:
  - comp: integer 0–2 (computer's move).
  - user: integer 0–9 (your move; 0–2 normal, 3–9 special).
- Returns:
  - 1 → you win
  - 0 → draw
  - -1 → you lose

Logic includes:
- Specific matchups for:
  - user == 0 with comp in {3, 8, 9}
  - user == 1 with comp in {4, 5, 9}
  - user == 2 with comp in {6, 7, 9}
- Fallback:
  - If comp == user → draw.
  - Standard rules:
    - Rock loses to Paper, Paper loses to Scissors, Scissors loses to Rock.

tournament()
- Greets the player and explains the rules.
- Asks for the number of rounds (must be > 0).
- For each round:
  - Computer picks a random move 0–2 using random.randint.
  - Player enters a move (0–9).
  - Prints either the classic move name or special move name.
  - Evaluates outcome using check.
  - Updates and displays score and round result.
- After all rounds, prints:
  - Total score.
  - Tournament result message.

The script ends by calling tournament() so the game starts immediately when run.

🛠️ Installation & Setup

# ✅ Requirements
- Python 3.7+ installed on your system.
- No external libraries are required (only the standard random module is used).

 # 🔧 Steps
1. Clone this repository
   git clone https://github.com/<your-username>/rock-paper-scissors-tournament.git

2. Move into the project directory
   cd rock-paper-scissors-tournament

3. Run the game (replace filename if needed)
   python main.py

# 🕹️ Example Session
Welcome to the Rock-Paper-Scissors Tournament!
In this tournament, you will play a series of rounds against the computer.
You score 1 point for each win.
At the end of the tournament, the player with the most points wins!

Enter the number of rounds you want to play: 3
Enter 0 for rock, 1 for paper, 2 for scissors, or 3-9 for special moves: 3
You used a special move: Rockslide
Computer chose: paper

Round 1
You won!

...
Tournament Over!
Your score: 2 out of 3
Congratulations! You won the tournament!

# 📁 Project Structure
Suggested structure for your repo:

rock-paper-scissors-tournament/
├── main.py        # Contains check() and tournament() and calls tournament()
└── README.md      # Project documentation

# 🚀 Possible Extensions
- 🧑‍🤝‍🧑 Local 2-player mode (player vs player).
- 🧠 Smarter computer using basic pattern learning or ML.
- 🖼️ GUI version using Tkinter or Pygame.
- 💾 Save past results and show history/leaderboard.
- 🌐 Convert to a web app using Flask or Django.

# 🤝 Contributing
Contributions, ideas, and suggestions are welcome:

1. Fork the repository.
2. Create a new branch: git checkout -b feature/my-feature
3. Commit your changes: git commit -m "Add my feature"
4. Push to the branch: git push origin feature/my-feature
5. Open a Pull Request.

📄 License
You can release this project under the MIT License or any license you prefer. Popular open-source Rock-Paper-Scissors tutorials and projects often use MIT for simplicity and reuse.
