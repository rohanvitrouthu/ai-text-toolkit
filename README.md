# AI Text Toolkit
A simple yet powerful web application that uses the OpenAI API to perform various text transformations. This project serves as a clear, hands-on example of a client-server architecture where a frontend communicates with a secure Python backend to leverage the power of Large Language Models.

## Features
1. Summarize: Condense long articles or paragraphs into key bullet points.
2. Extract Keywords: Pull out the most important terms from a body of text.
3. Change Tone: Rewrite text in different styles: Formal & Professional, Casual & Friendly
4. As Sheldon from The Big Bang Theory.

## Secure API Handling
The OpenAI API key is stored securely on the backend and is never exposed to the user's browser.

## Clean, Responsive UI
A simple and intuitive web interface built with HTML and Tailwind CSS that works on any device.

## Extensible
Easily add new text transformation tools by modifying a single Python dictionary and adding a button to the frontend.

## How It Works
This application follows a standard client-server model:Frontend (Client): The index.html file, which runs in the user's web browser. It provides the user interface (text box, buttons). When a user clicks a button, JavaScript sends the input text and the desired transformation type to our backend server.

Backend (Server): The app.py Python script, which is a simple web server built with Flask. It listens for requests from the frontend.

API Communication: Upon receiving a request, the backend server securely uses the stored OpenAI API key to call the official OpenAI API, passing along the text and the transformation instructions.

Response: The OpenAI API processes the request and sends the transformed text back to the Flask server. The server then relays this result back to the frontend, where it is displayed to the user.This separation ensures that the secret API key is never compromised.

### Technology Stack
#### Backend
- Python Flask: A micro web framework for creating the server and API endpoint.
- python-dotenv: For managing environment variables (like the API key).
- openai: The official OpenAI Python client library.
- Flask-Cors: To handle Cross-Origin Resource Sharing, allowing the frontend and backend to communicate.

#### Frontend:
- HTML5, Tailwind CSS: For modern, utility-first styling.
- JavaScript (ES6+): For handling user interactions and communicating with the backend via the fetch API.

## Setup and Installation:
Follow these steps to get the project running on your local machine.

### Prerequisites
Python 3.8 or newer
An active OpenAI API Key. You can get one from the OpenAI Platform.

1. Clone the Repository: git clone https://github.com/your-username/ai-text-toolkit.git
cd ai-text-toolkit
2. Backend Setup: First, set up the Python environment and install the required dependencies.

### Create a virtual environment
python -m venv venv

### Activate the virtual environment
#### On macOS/Linux:
source venv/bin/activate
#### On Windows:
.\venv\Scripts\activate

### Install Python packages
pip install -r requirements.txt
(Note: You will need to create a requirements.txt file containing Flask, openai, python-dotenv, and Flask-Cors)

3. Configure API Key: Create a file named .env in the root of the project directory. This file will hold your secret API key. OPENAI_API_KEY="sk-YourSecretKeyGoesHere"

Important: Add .env to your .gitignore file to prevent accidentally committing your secret key to GitHub.

## Usage
To run the application, you need to start the backend server and then open the frontend file.
1. Start the Backend Server: With your virtual environment still active, run the Flask application from your terminal:python app.py
The server will start and listen for requests on http://127.0.0.1:5000. You should see a message confirming it's running. Keep this terminal window open.
2. Open the Frontend: Navigate to the project folder on your computer and double-click the index.html file. It will open in your default web browser.You can now use the AI Text Toolkit!

Security Note: NEVER expose your OPENAI_API_KEY in frontend code (JavaScript, HTML). ALWAYS use a .env file and a .gitignore file to keep your API keys and other secrets from being published. 

The client-server model used in this project is the recommended approach for building applications that use paid APIs with secret keys.

## Future Improvements
1. Add More Tools: Implement other transformations like "Translate," "Fix Grammar," or "Explain Like I'm 5."
2. Streaming Responses: For longer text generations, modify the API call to stream the response back to the user for a more real-time feel.
3. Error Handling: Improve UI feedback for different types of errors (e.g., network issues vs. API key errors).Model Selection: Add a dropdown menu to allow the user to choose different OpenAI models (e.g., GPT-4 vs. GPT-3.5-turbo).