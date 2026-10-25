# Python Projects

A collection of standalone Python projects ranging from CLI utilities to desktop GUI applications.

## 📁 Repository Structure

```text
.
├── .gitignore
├── README.md
├── requirements.txt
│
├── todo_cli/
│   ├── main.py                     # Interactive task manager
│   └── README.md
│
├── weather_cli/
│   ├── main.py                     # Real-time weather CLI via Open-Meteo API
│   └── README.md
│
├── number_guessing_game/
│   ├── main.py                     # Modern CustomTkinter GUI game
│   └── README.md
│
├── word_frequency_analyzer/
|   ├── main.py                     # Text processing & word counter
|   ├── sample.txt                  # Sample test text
|   └── README.md
|
└── file_organiser/
    ├── main.py                     # File Organiser Tool
    └── README.md
```

---

## 🚀 Projects Overview

| Project | Type | Dependencies | Run Command |
| :--- | :--- | :--- | :--- |
| [**Todo CLI**](todo_cli/) | CLI Tool | Standard Library | `python todo_cli/main.py` |
| [**Weather CLI**](weather_cli/) | CLI Tool | `requests` | `python weather_cli/main.py` |
| [**Number Guessing Game**](number_guessing_game/) | Desktop GUI | `customtkinter` | `python number_guessing_game/main.py` |
| [**Word Frequency Analyzer**](word_frequency_analyzer/) | CLI Tool | Standard Library | `python word_frequency_analyzer/main.py` |

---

## 🛠️ Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SaswataNX05/Python-Git.git
   cd Python-Git
   ```

2. **(Optional) Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## ➕ Adding New Projects

To add a new project to this repository:
1. Create a dedicated folder: `mkdir my_new_project`
2. Place your entry script inside: `my_new_project/main.py`
3. Add a brief `README.md` inside the project folder.
4. If your project uses new third-party libraries, add them to `requirements.txt`.
