# Turtle Crossing Game (Python Turtle)

A **Turtle Crossing Game** inspired by the classic Frogger arcade game.  
In this game, the player controls a turtle that must cross busy lanes of traffic without colliding with moving cars. Each successful crossing increases the score and the game speed, while collisions reduce lives.

This project demonstrates **Object-Oriented Programming (OOP), event handling, game loops, collision detection, and dynamic difficulty** in Python.

---

## Features

- Control a turtle to cross moving cars
- Randomly colored cars spawn in multiple lanes
- Dynamic car speed increases with each successful crossing
- Score tracking system
- Lives system (player has 3 lives)
- Pause and resume game
- Collision detection with cars
- Game over screen when lives reach zero

---

## Technologies Used

- Python 3
- Turtle Graphics Module
- Object-Oriented Programming (OOP)
- Event Handling
- Game loop and collision logic

---

## 📂 Project Structure

```bash
turtle-crossing/
│
├── main.py          # Main game loop
├── player.py        # Player turtle class
├── car_manager.py   # Car spawning and movement logic
├── scoreboard.py    # Score, lives, and game over display
│
└── README.md
```

---

## Requirements

Before running the game, ensure **Python 3.x** is installed:

https://www.python.org/downloads/

Check installation:

#### Windows

```bash
python --version
```

#### Mac / Linux

```bash
python3 --version
```

---

## How to Run the Game

### Clone the Repository

```bash
git clone https://github.com/adebayoadesugba/turtle-crossing.git
```

### Navigate into the Project Folder

```bash
cd turtle-crossing
```

### Run the Game

#### Windows

```bash
python main.py
```

#### Mac / Linux

```bash
python3 main.py
```

The game window will open and you can start playing.

---

## Controls

| Action | Key |
|--------|-----|
| Move Turtle Up | W or Up Arrow |
| Pause/Resume Game | P |

---

## Game Rules

- Guide the turtle from the bottom to the top of the screen.
- Avoid colliding with moving cars.
- Each successful crossing increases the **level** and slightly **increases car speed**.
- Collisions reduce **lives**. The player starts with 3 lives.
- The game ends when all lives are lost.

---

## Key Concepts Demonstrated

- Object-Oriented Programming (classes for player, cars, scoreboard)
- Game loops with `while` and `screen.update()`
- Event handling using `screen.onkeypress()`
- Randomized car generation
- Collision detection between turtle and cars
- Dynamic difficulty (car speed increases with level)
- Modular code organization

---

## Future Improvements

- Add sound effects for collisions and level completion
- Add multiple difficulty levels
- Add graphical enhancements (background, road markings)
- Store high scores
- Implement multiple lives display on the turtle itself
- Add restart game functionality without closing the window

---

## Author

**Adebayo Adesugba**

Full Stack Developer  
Python | JavaScript | React | Node.js | AI Development

---

⭐ If you like this project, feel free to **star the repository on GitHub**.
