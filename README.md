## TEAM: SUDO MOTTO
- Borabo, Aira
- Dela Cruz, Angel Jared
- Mariñas, Justin Kylle
- Medina, Karylle Jade
- Obligado, Athena Ashley

# Trivia App

A simple Python Flask-based trivia application that displays trivia questions and answers locally, serves them via API, and allows adding new questions.

## Features

- **Local Display**: View trivia questions in a web interface.
- **API Endpoints**: RESTful API to get and add questions.
- **OOP Management**: Questions managed using a Question class.
- **Ngrok Integration**: Expose the API publicly using ngrok.
- **In-Memory Storage**: No database required; questions stored in memory.
- **Random Question**: Get a random trivia question with toggle answer display.
- **Interactive UI**: Buttons to randomize questions and toggle answer visibility.

## Installation

1. Clone the repository.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. (Optional) Set up ngrok for public access:
   - Sign up at https://dashboard.ngrok.com/signup
   - Get your authtoken from https://dashboard.ngrok.com/get-started/your-authtoken
   - Run: `ngrok config add-authtoken YOUR_TOKEN`

4. Run the app:
   ```
   python app.py
   ```
   The app will start on `http://localhost:5000`. If ngrok is configured, it will also create a public tunnel.

## Usage

### Web Interface
- Visit the home page to view existing questions.
- Use the form to add new questions.
- Click "Get Random Question" to display a random question.
- Click "Toggle Answers" to show/hide the answer for the random question.

### API Endpoints

- **GET /api/questions**: Retrieve all questions.
- **POST /api/questions**: Add a new question. JSON body: `{"question": "Q", "answer": "A", "category": "Cat"}`
- **GET /api/questions/random**: Get a random question.

## Project Structure

- `app.py`: Main Flask application.
- `template/trivia.html`: HTML template for the web interface.
- `requirements.txt`: Python dependencies.
- `static/`: Static files (if any).
