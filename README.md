# 📩 Message Spamming Script

A simple Python automation script that uses **PyAutoGUI** to automatically type and send a predefined message multiple times. It also supports playing a notification sound when the task is complete.

> ⚠️ **Disclaimer:** This project is intended **only for educational purposes and personal automation/testing** (for example, automating input in your own applications). Do **not** use it to harass, spam, or violate the Terms of Service of any platform.

---

## ✨ Features

- ⌨️ Automatically types messages
- 🔁 Sends a message multiple times
- ⏳ Configurable start delay
- 🔔 Plays a notification sound after completion
- 🖥️ Cross-platform (Windows, macOS, Linux)

---

## 📂 Project Structure

```text
Message-Spamming-Script/
│
├── main.py          # Main Python script
├── khatam.mp3       # Notification sound (optional)
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone git@github.com:ThatGuySoumik/Message-Spamming-Script-.git
cd Message-Spamming-Script-
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

**macOS / Linux**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 📦 Requirements

- Python 3.13+
- PyAutoGUI
- pygame

Install manually if needed:

```bash
pip install pyautogui pygame
```

---

## ▶️ Usage

1. Open the application or chat window where you want to automate typing.
2. Run the script:

```bash
python main.py
```

3. Switch to the target window before the countdown finishes.
4. The script will automatically type and send the configured message.

---

## ⚙️ Configuration

Modify the following values in the script:

```python
msg = "Good Morning"
```

Change the number of repetitions:

```python
while i <= 10:
```

Adjust the initial delay:

```python
time.sleep(4)
```

Change the notification sound:

```python
pg.mixer.music.load("khatam.mp3")
```

---

## 🛠 Technologies Used

- Python
- PyAutoGUI
- pygame

---

## ⚠️ Notes

- Keep the destination window focused while the script is running.
- Ensure the notification audio file exists in the project directory.
- Automation may not work correctly if the target application blocks simulated keyboard input.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Soumik Pal**

GitHub: https://github.com/ThatGuySoumik