# AI True/False Quiz App

A smart, customizable **True/False quiz application** powered by **OpenAI GPT-4o**. Users can choose a topic and difficulty level, and the app generates 8 AI-driven questions in real-time with a clean GUI using **Tkinter**.

---

## 🚀 Features

- ✅ AI-generated quiz questions (based on user topic and difficulty).
- 📊 Tracks your score and handles incorrect answers with retry logic.
- 🧠 Designed to be educational and engaging for all age groups.
- 🖼️ Simple, responsive Tkinter interface.
- 🔁 One-click quiz restart.
- 🔌 *(Optional)* Serial communication integration (e.g. for Micro:bit).

---

## 🛠️ Tech Stack

- Python 3.7+
- OpenAI Python SDK (`openai`)
- Tkinter (built-in GUI library)
- *(Optional)* pyserial for hardware output

---

## 🧰 Requirements

```bash
pip install openai
# Optional (if using hardware like Micro:bit):
# pip install pyserial
```

---

## 🧠 How It Works

1. **OpenAI API Key**
   - Replace the OPENAI_API_KEY with your own key.

2. **User Inputs**:
   - Enters a topic (e.g., "computers", "space", "biology").
   - Selects difficulty (`Easy`, `Medium`, or `Hard`).

3. **Question Generation**:
   - Uses `gpt-4o` to generate 8 structured **True/False** questions in JSON format via OpenAI’s `responses.create` API.

4. **Gameplay**:
   - Player answers questions one at a time.
   - Wrong answers prompt a retry (only first-correct attempts count toward score).
   - Final score is displayed upon quiz completion.

5. **Restart**:
   - One-click restart resets the app and prompts for a new quiz.

---

## 🖼️ GUI Preview

| Screen       | Description                         |
|--------------|-------------------------------------|
| Start Page   | Topic entry and difficulty dropdown |
| Quiz Screen  | Question display, True/False buttons, score |
| End Screen   | Final score and restart option      |

---

## ⚙️ Optional: Serial Hardware Integration

Uncomment the following lines to enable serial output (e.g., Micro:bit feedback):

```python
# import serial
# ser = serial.Serial('COM3', 115200)
# ser.write(f"{result_to_send}#".encode())
```

- `1#`: Sent for a correct answer on the first try
- `2#`: Sent for an incorrect attempt

---

## 🧪 Sample Usage

1. Launch the app:
   ```bash
   python quiz_app.py
   ```

2. Enter topic: `Artificial Intelligence`

3. Select difficulty: `Medium`

4. Answer 8 AI-generated True/False questions.

--

## 👨‍💻 Author

[Oliver](https://github.com/jollyolliel)

---
