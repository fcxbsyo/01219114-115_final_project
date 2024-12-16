# 01219114-115_final_project

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

## Installation
To run the game, make sure you have Python installed on your computer. The game uses the Turtle and Pygame libraries 
for graphics and sound.

1. Install Python 3.x from python.org.
2. Install Pygame by running: pip install pygame
3. Download the game repository and navigate to the game directory.
4. Run the game by executing the following command: python main.py

## Gameplay
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

## Game Flow
1. The game begins with the start screen. Press "space" to start.
2. The player defends the space station by bouncing and launching balls at asteroids and threats.
3. The game ends when an asteroid collides with the player. The player's score is saved, and the leaderboard 
is displayed.
4. Players can pause or resume the game at any time.

## License
This project is open-source and available under the MIT License.