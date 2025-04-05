# pygame-web-game

## Overview
This project is a web-based version of a Turtle Graphics Game implemented using Pygame. The game features a player-controlled turtle that can move around the screen, interact with various elements, and enjoy a fun graphical experience.

## Project Structure
```
pygame-web-game
├── src
│   ├── main.py          # Entry point of the game
│   ├── assets
│   │   ├── images       # Contains image files for sprites and backgrounds
│   │   └── sounds       # Contains sound files for music and effects
│   └── utils
│       └── helpers.py   # Utility functions for asset management and game logic
├── requirements.txt      # Lists dependencies for the project
└── README.md             # Documentation for the project
```

## Installation
To run this game, you need to have Python and Pygame installed. You can install the required dependencies by running:

```
pip install -r requirements.txt
```

## Running the Game
To start the game, navigate to the `src` directory and run the following command:

```
python main.py
```

## Features
- Player-controlled turtle movement
- Interactive game elements
- Sound effects and background music
- Beautiful graphics and animations

## Contributing
Feel free to contribute to this project by submitting issues or pull requests. Your feedback and suggestions are welcome!

## License
This project is open-source and available under the MIT License.

## If you are running from Codespaces you need to run this command
sudo apt-get update && sudo apt-get install -y xvfb

xvfb-run -s "-screen 0 1024x768x24" python /workspaces/pygame/pygame-web-game/src/main.py


