# 21 Classic Snake Game

## Overview
The **Classic Snake Game** is a Python-based recreation of the timeless arcade game, built using the `turtle` graphics library. The objective is simple: control the snake, eat food to grow, and avoid colliding with the walls or your own tail. This project focuses on clean code organization using Object-Oriented Programming (OOP) and modular design principles.

---

## Concepts Implemented
- **Object-Oriented Programming (OOP):** Classes like `Snake`, `Food`, and `Scoreboard` encapsulate game logic and promote reusability.
- **Modularization:** Code is split into multiple files (`snake.py`, `food.py`, `scoreboard.py`, `main.py`) for better organization.
- **Slicing and List Manipulation:** Efficient handling of the snake segments as a list for smooth movement and growth.
- **Class Inheritance:** The `Food` class inherits from the `Turtle` class, extending its functionality to manage food appearance and behavior dynamically.


## 🎮 Game Logic Explained

### 1. **Screen Setup and Snake Creation**
- Initializes a game screen (600x600 pixels) with a black background.
- The snake starts with three square segments aligned horizontally.
  
### 2. **Snake Movement**
- The snake moves automatically in its current direction.
- Each segment follows the position of the previous one to simulate smooth movement.
- Movement is continuous and managed through a game loop with `screen.update()` and `time.sleep()` for consistent frame rates.

### 3. **Controls**
- Arrow keys (`Up`, `Down`, `Left`, `Right`) allow you to control the snake.
- The snake cannot reverse directly into itself (e.g., moving from `Up` directly to `Down`).

### 4. **Collision Detection**
- **Food Collision:** Eating food triggers the `refresh()` method, which randomly places a new food item on the screen.
- **Wall Collision:** Hitting the game boundary ends the game.
- **Self Collision:** If the snake's head touches any part of its body, the game terminates.

### 5. **Game Progression**
- Each time food is consumed:
  - The snake grows by adding a new segment.
  - The score increases.
- The game gradually becomes more challenging as the snake gets longer and harder to control.

---

## 🔧 How to Run
1. Clone this repository.
2. Install dependencies:
    - Requires Python 3.x (no additional libraries needed since turtle is included in the standard library).
3. Run the game.


## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute the game as you like.

## Acknowledgments

Inspired by classic arcade games and built as part of a Python learning journey through Dr. Angela Yu’s **100 Days of Code: Python Pro Bootcamp.**


---
<section align="center">
  <code>coderBri © 2025</code>
</section>
