# ♟️ N-Queens AI Solver

A Python-based **Artificial Intelligence and algorithmic problem-solving project** that solves the N-Queens problem using **backtracking**.

---

## 📌 Project Overview

The N-Queens problem requires placing **N queens on an N × N chessboard** so that no two queens can attack each other.

This project uses a backtracking approach to systematically explore possible board configurations and find a valid solution.

---

## 🎯 Objectives

* Solve the N-Queens problem programmatically.
* Apply backtracking and recursive problem-solving.
* Implement constraint checking for queen placements.
* Practice algorithm design and search techniques.
* Visualize the solution through a Python-based interface.

---

## 🧠 Algorithm

### Backtracking

The algorithm places queens row by row.

For each row:

1. Select a column.
2. Check whether the position is safe.
3. If it is safe, place the queen.
4. Move to the next row.
5. If no valid position exists, backtrack and change the previous queen's position.

A position is considered unsafe if another queen exists in the same:

* Column
* Main diagonal
* Secondary diagonal

---

## 🔄 Algorithm Workflow

```text
Start
  │
  ▼
Select a row
  │
  ▼
Try a column
  │
  ▼
Is the position safe?
  │
 ┌┴─────────────┐
 │              │
Yes             No
 │              │
 ▼              │
Place Queen     │
 │              │
 ▼              │
Next Row        │
 │              │
 ▼              │
Solution? ──────┘
 │
 ├── Yes → Return Solution
 │
 └── No → Backtrack
```

---

## 🛠️ Technologies

* **Python**
* **Artificial Intelligence**
* **Backtracking**
* **Recursion**
* **Algorithms**
* **Problem Solving**

---

## 🚀 How to Run

Clone the repository:

```bash
git clone https://github.com/AbdlerahmanGihad/Nqueens-AI-Solver.git
```

Navigate to the project:

```bash
cd Nqueens-AI-Solver
```

Run the Python program according to the project's main Python file.

---

## 💡 Key Learning Outcomes

Through this project, I practiced:

* Recursive problem solving.
* Backtracking algorithms.
* Constraint checking.
* Search-based problem solving.
* Algorithm implementation in Python.
* Translating an AI problem into a computational solution.

---

## 👨‍💻 Author

### Abdelrahman Gihad

Artificial Intelligence Student

GitHub:
https://github.com/AbdlerahmanGihad

---

⭐ If you find this project useful, consider giving the repository a star.
