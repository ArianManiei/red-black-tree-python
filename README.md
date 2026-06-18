# 🌳 Red-Black Tree Implementation (Work in Progress)

> **🚧 Status: Active Development (WIP)**
> This project is currently under development. Core data structure mechanics are being built and tested.

## 📌 Overview
This project is an advanced, object-oriented implementation of a **Red-Black Tree** in Python. It is designed to practically apply complex algorithmic concepts (AuD), ensuring balanced data operations with $O(\log n)$ time complexity for insertions, deletions, and lookups. 

The ultimate goal of this project is not just the backend logic, but also to build an interactive Graphical User Interface (GUI) to visualize how nodes balance, rotate, and change colors in real-time.

## 🛠️ Tech Stack & Tools
* **Language:** Python 3
* **GUI Framework:** PyQt6 (Planned for graphical visualization)
* **Concepts:** Object-Oriented Programming (OOP), Data Structures, Self-Balancing Trees

## 🚀 Features & Roadmap

### Backend (Algorithmic Core)
- [x] Base Node structure and Sentinel logic
- [x] Standard Binary Search Tree (BST) operations (Search)
- [x] Tree Insertion logic
- [x] Insertion Fixup (Coloring and Left/Right Rotations)
- [x] Core Deletion structure (`transplant`, `minimum`)
- [x] Deletion Fixup (Handling double-black nodes and rebalancing)

### Frontend (Visualization)
- [ ] PyQt6 window setup and graphics scene
- [ ] Real-time node rendering (differentiating Red and Black nodes)
- [ ] Visualizing rotations and tree balancing steps

## 💡 What's Next?
Currently focusing on completing the intricate `delete_fixup` logic to perfectly handle all 4 rebalancing cases when a black node is removed. Once the backend is fully rock-solid, the integration with the PyQt6 GUI will begin.
