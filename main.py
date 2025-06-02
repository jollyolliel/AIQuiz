import tkinter as tk
import sys
import os
from openai import OpenAI
import json
# import serial

# Global variables to store quiz state
#ser = serial.Serial('COM3', 115200)
questions = []
current_question_index = 0
correct_answers = 0
got_question_wrong = False

client = OpenAI(
    api_key="OPENAI_API_KEY")


def create_quiz(topic, diff):
    response = client.responses.create(
        model="gpt-4o-2024-08-06",
        input=[
            {"role": "system", "content": "Make a quiz based on what the user requested"},
            {
                "role": "user",
                "content": f"Create a quiz on {topic} with {diff} difficulty and 8 questions. It has to be a True false questions and has to have 8 questions.",
            },
        ],
        text={
            "format": {
                "type": "json_schema",
                "name": "quiz",
                "schema": {
                    "type": "object",
                    "properties": {
                        "questions": {
                            "type": "array",
                            "description": "A list of quiz questions.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "question_text": {
                                        "type": "string",
                                        "description": "The text of the quiz question."
                                    },
                                    "correct_answer": {
                                        "type": "boolean",
                                        "description": "The correct answer to the quiz question, represented as a boolean."
                                    }
                                },
                                "required": [
                                    "question_text",
                                    "correct_answer"
                                ],
                                "additionalProperties": False
                            }
                        }
                    },
                    "required": [
                        "questions"
                    ],
                    "additionalProperties": False
                },
                "strict": True,
            }
        }
    )

    return response.output[0].content[0].text


def generates_questions(topic, diff):
    result = create_quiz(topic, diff)
    result = json.loads(result)

    return result


def start_quiz():
    global questions, current_question_index, total_questions
    topic = topic_entry.get()
    difficulty = difficulty_var.get()  # Get selected difficulty

    start_frame.pack_forget()
    current_question_index = 0

    questions_data = generates_questions(topic, difficulty)
    questions = questions_data['questions']
    total_questions = len(questions)
    show_question()

def answer_question(user_answer):
    global current_question_index, correct_answers, got_question_wrong

    correct_answer = questions[current_question_index]['correct_answer']
    if correct_answer == True:
        correct_answer = "Yes"
    elif correct_answer == False:
        correct_answer = "No"

    if user_answer == correct_answer:
        result_label.config(text="Correct! Well done.", fg="green")
        current_question_index += 1
        if current_question_index < len(questions):
            if not got_question_wrong:
                correct_answers += 1
                result_to_send = "1"
            else:
                result_to_send = "2"
            # ser.write(f"{result_to_send}#".encode())
            got_question_wrong = False
            root.after(1000, show_question)
        else:
            result_label.config(text="Quiz completed!", fg="blue")
            question_label.config(text="")
            restart_btn = tk.Button(text="Restart", font=("Helvetica", 14), bg="#4CAF50", fg="white",
                                        command=restart_quiz, relief="raised")
            restart_btn.pack(pady=20)
            continue_button.pack(pady=10)
            for widget in answer_buttons_frame.winfo_children():
                widget.destroy()
    else:
        got_question_wrong = True
        result_label.config(text="Incorrect. Try again.", fg="red")

def show_question():
    for widget in answer_buttons_frame.winfo_children():
        widget.destroy()

    question_text = questions[current_question_index]['question_text']
    correct_answer = questions[current_question_index]['correct_answer']

    if correct_answer == True:
        correct_answer = "Yes"
    elif correct_answer == False:
        correct_answer = "No"

    question_label.config(text=question_text)
    result_label.config(text="")
    score_label.config(text=f"Score: {correct_answers}/{total_questions}")

    for answer in ["Yes", "No"]:
        button = tk.Button(answer_buttons_frame, text=answer, font=("Helvetica", 14), bg="#2196F3", fg="white",
                           width=20, command=lambda a=answer: answer_question(a), relief="raised")
        button.pack(pady=5)

def restart_quiz():
    python = sys.executable
    os.execl(python, python, *sys.argv)

# Create the main window
root = tk.Tk()
root.title("Quiz App")
root.geometry("800x450")
root.config(bg="#F0F0F0")

# Start screen
start_frame = tk.Frame(root, bg="#F0F0F0")
start_frame.pack(pady=20)

topic_label = tk.Label(start_frame, text="Enter Topic", font=("Helvetica", 14), bg="#F0F0F0")
topic_label.pack(pady=10)

topic_entry = tk.Entry(start_frame, font=("Helvetica", 14), width=25, borderwidth=2, relief="solid")
topic_entry.pack(pady=10)

difficulty_label = tk.Label(start_frame, text="Select Difficulty", font=("Helvetica", 14), bg="#F0F0F0")
difficulty_label.pack(pady=10)

# Difficulty dropdown
difficulty_var = tk.StringVar(value="Easy")
difficulty_dropdown = tk.OptionMenu(start_frame, difficulty_var, "Easy", "Medium", "Hard")
difficulty_dropdown.config(font=("Helvetica", 14), bg="#4CAF50", fg="white")
difficulty_dropdown.pack(pady=10)

continue_button = tk.Button(start_frame, text="Continue", font=("Helvetica", 14), bg="#4CAF50", fg="white", command=start_quiz, relief="raised")
continue_button.pack(pady=10)

# Quiz screen widgets
score_label = tk.Label(root, font=("Helvetica", 16), bg="#F0F0F0")
score_label.pack(pady=20)

question_label = tk.Label(root, font=("Helvetica", 16), bg="#F0F0F0")
question_label.pack(pady=20)

answer_buttons_frame = tk.Frame(root, bg="#F0F0F0")
answer_buttons_frame.pack(pady=20)

result_label = tk.Label(root, font=("Helvetica", 14), bg="#F0F0F0")
result_label.pack(pady=10)

# Run the app
root.mainloop()
