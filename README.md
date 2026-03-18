# Alien Invasion 🚀👾

A classic space shooter game built with Python and Pygame where you defend Earth from waves of alien invaders.

## Description

Control a spaceship at the bottom of the screen and shoot down incoming alien fleets. The game gets progressively harder as you advance through levels, with aliens moving faster and being worth more points.

## Features

- Smooth ship movement (arrow keys)
- Bullet shooting mechanics (spacebar)
- Progressive difficulty levels
- Score tracking and high score system
- Lives system
- Start/restart button interface

## Requirements

- Python 3.x
- Pygame

## Installation

1. Clone or download this repository

2. Install the required dependency:
```bash
pip install pygame
```

## How to Run

Simply run the main game file:
```bash
python alien_invasion.py
```

## Controls

- **Arrow Keys**: Move ship (up, down, left, right)
- **Spacebar**: Fire bullets
- **Q**: Quit game
- **Mouse Click**: Click "Start game" button to begin

## Gameplay

- Destroy all aliens to advance to the next level
- Avoid letting aliens reach the bottom of the screen
- Avoid collisions with aliens
- You have 3 ships (lives) to start
- Score increases with each alien destroyed
- Difficulty and points increase with each level

## Project Structure

- `alien_invasion.py` - Main game loop and logic
- `ship.py` - Player ship class
- `alien.py` - Alien enemy class
- `bullet.py` - Bullet projectile class
- `button.py` - UI button class
- `game_stats.py` - Game statistics tracking
- `scoreboard.py` - Score display system
- `settings.py` - Game configuration and settings
- `images/` - Game sprites and graphics

## Credits

Built with Python and Pygame.
