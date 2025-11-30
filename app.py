from flask import Flask, render_template, request, jsonify
from pyngrok import ngrok
import random

class Question:
    def __init__(self, question, answer, category="General"):
        self.question = question
        self.answer = answer
        self.category = category

    def to_dict(self):
        return {
            "question": self.question,
            "answer": self.answer,
            "category": self.category
        }

questions = [
    Question("What is the capital of France?", "Paris", "Geography"),
    Question("What is 2 + 2?", "4", "Math"),
    Question("Who wrote 'Romeo and Juliet'?", "William Shakespeare", "Literature"),
    Question("What is the largest planet in our solar system?", "Jupiter", "Science"),
    Question("In which year did World War II end?", "1945", "History"),
    Question("What is the chemical symbol for gold?", "Au", "Science"),
    Question("Which ocean is the largest?", "Pacific Ocean", "Geography"),
    Question("What is the square root of 144?", "12", "Math"),
    Question("Who painted the Mona Lisa?", "Leonardo da Vinci", "Art"),
    Question("What is the capital of Japan?", "Tokyo", "Geography")
]

app = Flask(__name__, template_folder='template')

@app.route("/")
def home():
    return render_template("trivia.html", questions=questions)

@app.route("/api/questions", methods=["GET"])
def get_questions():
    return jsonify([q.to_dict() for q in questions])

@app.route("/api/questions", methods=["POST"])
def add_question():
    data = request.get_json()
    if not data or "question" not in data or "answer" not in data:
        return jsonify({"error": "Question and answer required"}), 400
    category = data.get("category", "General")
    new_question = Question(data["question"], data["answer"], category)
    questions.append(new_question)
    return jsonify(new_question.to_dict()), 201

@app.route("/api/questions/random")
def get_random_question():
    if not questions:
        return jsonify({"error": "No questions available"}), 404
    random_question = random.choice(questions)
    return jsonify(random_question.to_dict())

if __name__ == "__main__":
    try:
        public_url = ngrok.connect(5000)
        print(f"Ngrok tunnel: {public_url}")
    except Exception as e:
        print(f"Ngrok failed: {e}. Running locally only.")
    app.run(debug=True)
