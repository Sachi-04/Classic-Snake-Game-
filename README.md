🐍 Classic-Snake-Game
A classic recreation of the arcade Snake game built using Python's standard turtle graphics library. This project features a colorful snake, randomized food, and a live scoreboard, all contained within a single Python script.

🎮 Game Features
Classic Gameplay: Navigate the snake to eat food and grow longer.
Collision Detection: Game over occurs if you hit the wall or your own tail.
Live Scoreboard: Tracks your current score in real-time at the top of the screen.
Randomized Elements: Food spawns at random coordinates with random colors.
Smooth Animation: Uses screen tracing controls for non-jittery movement.

📋 Prerequisites
You only need Python 3.x installed on your computer.
This game uses the following standard Python libraries (no external pip install required):
turtle (Graphics)
time (Animation delay)
random (Randomizing food generation)

🚀 How to Run
Create the file: Create a new file named main.py (or snake_game.py) and paste the entire code into it.
Run the script: Open your terminal or command prompt, navigate to the folder containing the file, and run:
    python main.py

🕹️ Controls
Use the Arrow Keys on your keyboard to control the snake:
 Arrow Keys 
 ← =Left
 → =Right
 ↑ =Up
 ↓ = Down
Note: The snake cannot reverse direction immediately (e.g., you cannot go directly Down if you are currently moving Up).

📂 Code Structure
Since the project is contained in a single file, the logic is divided into three main classes:
Snake Class: Handles the creation of the snake body, movement logic, and direction control.
Food Class: Inherits from Turtle. Handles the rendering of food and randomizing its location/color upon collision.
Scoreboard Class: Inherits from Turtle. Handles the text display for the score and the "Game Over" sequence.

 ⚙️ Customization
You can easily tweak the game by modifying the constants at the top of the file:
MOVE_DISTANCE: Change this to make the snake move in larger or smaller steps.
colors: Add or remove colors from the food list.
time.sleep(0.3): Modify this value in the while loop to change the game speed (lower number = faster snake).

📝 License Distributed under the MIT License. See LICENSE for more information.
