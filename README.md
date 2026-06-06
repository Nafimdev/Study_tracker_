# 📚 Study Tracker CLI

| Section | Details |
|---|---|
| 🚀 Overview | A simple Python command-line application to track and manage study hours per subject using JSON-based persistent storage. |
| 🎯 Purpose | Built to practice file handling, JSON storage, and basic CLI application design while creating a useful personal study tracker. |
| ⚙️ Features | - Add study hours per subject<br>- Automatically accumulates total hours per subject<br>- View all saved study data<br>- Reset all stored data<br>- Persistent storage using `study.json`<br>- Lightweight CLI-based interaction |
| 🧠 How It Works | The program uses a Python dictionary to store subject-wise study hours and saves it in a JSON file (`study.json`). When you add hours, existing subjects are updated and new subjects are created automatically. |
| 📦 Data Example | <pre><code>{<br>  "Math": 5,<br>  "Physics": 3,<br>  "Chemistry": 2<br>}</code></pre> |
| ▶️ How to Run | <pre><code>python study_tracker.py</code></pre> |
| 💡 Example Usage | <pre><code>--- Study Tracker ---<br>1. Add Study Hours<br>2. View Data<br>3. Reset Data<br>4. Exit<br><br>Choose option: 1<br>Subject: Math<br>Hours: 2<br>Updated!</code></pre> |
| 📂 File Structure | <pre><code>study-tracker-cli/<br>│<br>├── study_tracker.py<br>├── study.json<br>└── README.md</code></pre> |
| 🛠️ Tech Used | Python 3<br>Built-in `json` module<br>File handling<br>Command-line interface (CLI) |
| ⚠️ Notes | - Beginner-level project<br>- No timestamps yet, only cumulative totals<br>- `study.json` is auto-created on first run |
| 🔧 Future Improvements | - Add date-wise tracking<br>- Weekly/monthly summaries<br>- Graphs and visual reports<br>- CSV export<br>- Input validation<br>- GUI version using Tkinter or Flask |
