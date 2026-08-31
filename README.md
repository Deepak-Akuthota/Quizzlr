# 🧠 Quizzlr - Trivia Quiz GUI App 🎮

A Python-based graphical quiz application that tests your knowledge with True/False trivia questions! ✨

## 🌟 Overview
This project is an interactive trivia game featuring a graphical user interface (GUI). It uses object-oriented programming (OOP) principles to effectively separate the user interface, quiz logic, and data management into distinct modules. 🚀

## 📂 Project Structure
The application is modularized into several key files that work together to run the quiz:
- 🚀 **`main.py`**: The entry point of the application. Run this script to initialize the components and start the game.
- 🖼️ **`ui.py`**: Manages the graphical user interface using Tkinter, displaying the question text and handling user button clicks.
- 🧠 **`quiz_brain.py`**: Contains the core engine and logic of the game, including keeping track of the score, verifying if the user's answer is correct, and advancing to the next question.
- 📋 **`question_model.py`**: Defines the `Question` data model/class, serving as a blueprint for storing the text and correct answer of each individual question.
- 🌐 **`data.py`**: Handles data retrieval, typically fetching fresh trivia questions from an external source or API (such as the Open Trivia Database) and formatting them for the application.
- ✅/❌ **`true.png` & `false.png`**: Image assets used to style the True and False interactive buttons in the UI.

## ✨ Features
- 🖱️ **Interactive GUI**: Built with Python's Tkinter module for a clean, user-friendly experience.
- 🧩 **OOP Design**: Clean, modular code structure making it easy to maintain and expand.
- 🚦 **Instant Feedback**: The UI provides immediate visual feedback (e.g., flashing green or red) based on whether the selected answer is correct or incorrect.
- 📈 **Score Tracking**: Keeps a running total of the user's score throughout the session.

## 🛠️ Prerequisites
To run this project, you will need:
- 🐍 Python 3.x installed on your system.
- 🪟 The `tkinter` library (usually bundled by default with Python).
- 📡 If the application fetches questions from the web, ensure you have the `requests` library installed:
  ```bash
  pip install requests
  ```

## 🚀 How to Run
1. 📁 Ensure all files (`main.py`, `ui.py`, `quiz_brain.py`, `question_model.py`, `data.py`, and the `.png` images) are located in the same root directory.
2. 💻 Open your terminal or command prompt.
3. 📍 Navigate to the project directory.
4. ▶️ Execute the following command:
   ```bash
   python main.py
   ```
