# 📚 Study Tracker CLI

A simple Python command-line application to track and manage study hours per subject using JSON-based persistent storage.

---

## 🚀 Features

- Add study hours per subject
- Automatically accumulates total hours per subject
- View all saved study data
- Reset all stored data
- Persistent storage using `study.json`
- Lightweight CLI-based interaction (no external dependencies)

---

## 🧠 How it Works

The program uses a Python dictionary to store subject-wise study hours and saves it in a JSON file (`study.json`).

Example internal structure:

```json
{
  "Math": 5,
  "Physics": 3,
  "Chemistry": 2
}
