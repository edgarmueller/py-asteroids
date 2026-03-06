# py-asteroids 🚀

This README was AI generated.

`py-asteroids` is a basic Python recreation of the classic Asteroids arcade game, built as a learning project inspired by the [boot.dev](https://boot.dev) curriculum. It uses `pygame` for rendering and input handling.

## 🛠 Features

- Player-controlled spaceship that rotates and accelerates
- Asteroid field with randomly generated rocks
- Shooting mechanics to break apart asteroids
- Simple collision detection and game-over condition
- Modular code with classes for `Asteroid`, `Player`, `Shot`, and geometry utilities

## 📦 Requirements

This project targets Python 3.10+ and depends on the following packages (see `requirements.txt`):

- `pygame` – for graphics, sound, and input

You should run the game inside a virtual environment to avoid polluting your global Python installation.

```bash
python3 -m venv venv              # create virtual environment
source venv/bin/activate          # activate it (macOS/Linux)
# On Windows use `venv\Scripts\activate` instead
pip install -r requirements.txt   # install dependencies
```

## 🚀 Running the Game

Once dependencies are installed and your virtual environment is active, start the game with:

```bash
python3 main.py
```

A window will open where you can control the spaceship:

- **Left / Right arrows** – rotate the ship
- **Up arrow** – thrust forward
- **Spacebar** – fire a shot

The objective is to destroy all asteroids without colliding with any.

## 🧱 Project Structure

```
py-asteroids/             # root of repository
├─ asteroid.py            # Asteroid class and behavior
├─ asteroidfield.py       # Manages groups of asteroids
├─ circleshape.py         # Utility for circle-based collision and drawing
├─ constants.py           # Game constants (screen size, speeds, etc.)
├─ player.py              # Player spaceship class
├─ shot.py                # Projectile fired by player
├─ main.py                # Game loop and initialization
├─ README.md              # This documentation
├─ requirements.txt       # Python dependencies
```

Each module corresponds to a core game component.

## 🛠 Development Tips

- To add features, edit or extend the relevant class file and update `main.py` accordingly.
- Use `python -m pdb main.py` or insert `breakpoint()` calls to debug gameplay logic.
- Add new assets or sounds by placing them in a subdirectory and loading them where needed.

## 📄 License

This project is released under the MIT License. See [LICENSE](LICENSE) for details (if you add one).

---

