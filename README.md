# Wator - The Dynamic Aquatic Simulator 🌊

Welcome to **Wator**, an immersive simulator that recreates a vibrant marine ecosystem. In Wator, sharks roam, fish swim, and the survival of the fittest determines who dominates the ocean. Dive in and witness this compelling battle for life in the open sea!

---

## 🌟 Features

- **Dynamic Ecosystem**: A constantly changing world where sharks and fish interact based on hunger, energy, and reproduction cycles.
- **Realistic Simulation**: Animals have lifelike behaviors such as moving, eating, and reproducing.
- **Infinite Loop Simulation**: A continuous simulation to observe the cycle of life in real time.
- **Graphical Interface**: Realistic rendering of marine life using Pygame, with custom visuals and animations.
- **Grid-based Movement**: A 2D grid where each cell represents a part of the ocean, housing fish, sharks, or water.

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+**
- **Pygame** (for graphical simulation)
  
### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/wator.git
   cd wator
   ```

2. Install required packages:
   ```bash
   pip install pygame
   ```

3. Run the simulation:
   ```bash
   python main.py
   ```

---

## 📂 Project Structure

- **pool.py**: Manages the `Grid` class, responsible for creating and updating the 2D ocean grid.
- **fish.py**: Contains the `Fish` class, which defines behaviors like moving, reproducing, and aging.
- **shark.py**: Contains the `Shark` class, a subclass of Fish, adding features like energy management and eating.
- **world.py**: Houses the `World` class, which initializes the ecosystem, populates the grid, and manages interactions between animals.
- **main.py**: The main simulation file, handling Pygame rendering, event handling, and real-time updates.

---

## 🐠 Ecosystem Rules

### Animals

- **Fish**:
  - Move randomly and can reproduce after a set number of steps.
  - Occupy one cell at a time and aim to avoid predators.
- **Sharks**:
  - Hunt fish to maintain energy.
  - Lose energy over time and must feed to survive.
  - Reproduce periodically if conditions allow.

### Grid Movement

- Each cell can contain either a shark, fish, or remain empty.
- Animals interact based on adjacent cells, following specific rules:
  - **Sharks** prioritize cells with fish.
  - **Fish** move to empty cells to avoid sharks.
  
---

## 🕹️ Controls

The simulation runs in a loop until the shark or fish population is exhausted. Simply observe the graphical display for real-time updates on the ecosystem status!

- **Close Simulation**: Click the close button or press `Ctrl+C` in the terminal.
- **Pause/Resume**: Pause the simulation by halting the Python script in your IDE, then continue to observe.

---

## 🔄 Life Cycles and Behaviors

- **Chronon**: Each animal ages per chronon, a time unit in the simulation.
- **Reproduction**: After reaching a threshold chronon count, fish and sharks may reproduce.
- **Energy for Sharks**: Sharks deplete energy with each chronon. Feeding restores energy, simulating hunting success.

---

## 📜 License

This project is licensed under the **Simplon License**. Thanks to Simplon for providing the inspiration and guidance for this project.

---

## 🙏 Acknowledgments

Special thanks to our contributors and everyone who supported this project. May the fish be ever in your favor!

### Contributors

- **Hacene**: Fish creator, bringing life to the ocean’s colorful residents.
- **Gauthier**: Shark master, designing thrilling predator behaviors.
- **Jason**: World architect, creating a harmonious yet thrilling marine environment.
```