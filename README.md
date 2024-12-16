# 01219114-115_final_project

## Project Title:
The Space Station Defense Game

## Overview
The Space Station Defense Game is an action-packed cooperative game where players defend a space station from incoming 
threats using bouncing balls and missiles. The game features a physics engine for realistic mechanics, strategic 
cooperation between players, and various ball types with different properties.

## Features
- Player Movement: Control the player with keyboard inputs.
- Ball Launching: Use various ball types to defend the space station.
- Deflecting and Destroying Threats: Bounce or destroy incoming asteroids.
- Missile Firing: Fire missiles to eliminate threats.
- Power-ups: Activate special powers such as freezing enemies or creating additional balls.
- Score Saving: Save and display player scores in a leaderboard.
- Game States: Pause, resume, and game overstates are supported.

## Requirements
- Python 3.x
- Turtle Graphics (built-in with Python)
- Pygame (for sound and additional graphics)
- CSV support for saving and loading scores

## How to Install and Run the Project:
### Step-by-Step Installation:
1. Clone the Repository: https://github.com/your-username/space-station-defense.git
2. Install Required Libraries: Ensure you have Python 3.x installed. You will need the following libraries:
   - Pygame
   - Turtle
   - CSV (for saving scores)
   Install dependencies using pip: pip install pygame
3. Run the Game: Navigate to the project directory and run the game using Python: python main.py
4. Exit the Game: Press the "x" key on the main start screen to exit the game.

## Usage
Once you run the game, the following controls are available:
- Start the Game: Press the "space" key to start the game.
- Show Instructions: Press the "s" key to view the game instructions.
- Pause and Resume: Press the "Escape" key to pause and resume the game.
- Fire Missiles: Press the "space" key to fire missiles at incoming threats.
- Rotate the Player: Use the "left" and "right" arrow keys to rotate the player and aim.
- View Leaderboard: Press the "g" key to see the top scores.

## Game Controls
- Left Arrow Key: Rotate the player to the left.
- Right Arrow Key: Rotate the player to the right.
- Space-bar: Fire missiles or launch balls.
- Escape Key: Pause or unpause the game.
- S Key: Show game instructions.
- G Key: Display the scoreboard with top player scores.
- X Key: Exit the game.
- ** every key must be lower-case **

## Project Design and Implementation:

### UML Class Diagram:
https://github.com/fcxbsyo/01219114-115_final_project/blob/main/UML-Diagram.jpg

#### Class Descriptions:
- Game: The main class controlling the game flow, including starting the game, pausing, displaying instructions, 
and handling user input.
- Player: Represents the player, controls the player's ship, manages the score, and interacts with the game world.
- Asteroid: Represents asteroids that are randomly generated and move towards the space station.
- Missile: Represents missiles that the player can fire to destroy incoming asteroids.
- Ball: Represents bouncing balls that can be launched with different powers and interact with game objects.

#### Game Flow and Interactions:
- The game uses event-driven programming to capture user input (such as key presses) to control player actions like 
firing missiles, rotating, and pausing the game.
- The Game class is the core of the project, managing the main game loop, collision detection, object interactions, 
and power-ups.
- The Player, Asteroid, Missile, and Ball classes work together to simulate interactions between game objects, 
- including the physics-based movement and collision mechanics.
- The game also provides a scoring system, saving player scores to a CSV file, and showing the top scores.

#### Code Modifications:
- The baseline code (event-driven bouncing simulator and user interactivity) was modified to incorporate the cooperative 
gameplay mechanic, ball types with specific powers, and a space station defense theme.
- Custom classes like Asteroid, Ball, and Missile were created to represent different objects in the game, 
and each was equipped with properties and methods for managing interactions (e.g., collisions, power-ups).

#### Testing:
- The game has been tested for correct collision detection, physics behavior, and power-up mechanics.
- Known issues (if any) will be listed here. Example:
  - Asteroids may sometimes spawn off-screen due to a random number generation issue (being worked on).
  - Minor delay when switching between game states.

## Project Sophistication Level:
I would rate this project at 85, as it involves multiple interactive game objects (balls, missiles, asteroids) 
that behave according to physics principles and requires careful handling of user input and game state transitions.
But there's still some bugs (e.g., double Escape, Score shows at the middle of screen).

## License
This project is open-source and available under the MIT License.
