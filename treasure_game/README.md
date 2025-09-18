
# 🌍 Adventure Quest

Adventure Quest is a text-based exploration game built with Python. Players embark on a thrilling journey across mysterious lands, searching for treasures, surviving dangers, and managing their health and inventory along the way.

---

## 🎮 Game Features
- **Dynamic Exploration:** Choose from multiple areas like forests, caves, mountains, and more, each filled with unique treasures and dangers.
- **Random Events:** Discover valuable items, face unexpected dangers, or sometimes find nothing at all.
- **Player Progression:** Track your **health** and **inventory**, which updates as you explore.
- **Save & Load:** Save your journey to continue later using the `player.json` file.

---

## 🕹️ How to Play
1. **Start the Game:**  
   Run the game using:
   ```bash
   python main.py
   ```
2. **Choose an Option:**  
   At the main menu, select:
   ```
   <1> New Game
   <2> Load Game
   ```
3. **Explore the World:**  
   After starting, you can:
   ```
   <1> Explore the areas
   <2> View stats
   <3> Save progress
   <4> Exit the game
   ```
4. **Make Your Choices:**  
   - Pick an area to explore.
   - Encounter random events (treasure, danger, or nothing).
   - Manage your health and inventory wisely.

---

## 📂 Project Structure
```
├─ main.py        # Main game logic and functions
├─ map.json       # Contains areas, treasures, and dangers
└─ player.json    # Stores player data (name, health, inventory)
```

---

## 💡 Tips
- Saving your game overwrites the previous save.
- Danger events reduce health—if health drops to 0, the game ends.
- Treasures can appear multiple times, and duplicates are counted in the inventory.

---

## 🛠️ Requirements
- Python 3.8 or higher

No external libraries are required—just run it in a terminal.

---

## ⚡ Example Gameplay
```
Welcome, Alice. Prepare yourself for the journey ahead.
Press enter to continue...

<1> Explore the areas
<2> View stats
<3> Save progress
<4> Exit the game

Where do you want to explore?
-> Forest

Alice stumbled upon a gold coin.
```
