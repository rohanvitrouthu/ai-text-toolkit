import os
from openai import OpenAI
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)

# Enable CORS to allow requests from your end
CORS(app)

# OpenAI API Setup
# Load environment variables from the .env file
load_dotenv()

# Initialize the OpenAI client
# The OpenAI library automatically looks for the OPENAI_API_KEY in your environment

try:
    client = OpenAI()
except Exception as e:
    print(f"Error: Could not initialize OpenAI client. Is OPENAI_API_KEY set in your .env file? Details: {e}")
    exit()

def transform_text(transformation_type, original_text):
    """Calls the OpenAI API to perform a specific text transformation.
    
    Args:
    1. transformation_type(str): The type of transformation that needs to be performed on the user provided text. (Summarize, Extracting Keywords, Make it Formal, Make it Casual, Sheldon Mode: Make everything sound like Sheldon from TBBT)
    2. original_text(str): The text that needs to be transformed.
    
    Returns:
    str: The transformed text from the API.""" 

    # Defining the prompts for each transformation type in a dictionary.

    prompts_for_transformation_types = {
        "summarize": "Summarize the following text into 3 concise bullet points:",
        "keywords": "Extract the 5 most important keywords from the following text. List them separated by commas:",
        "formal": "Rewrite the following text in a formal and professional tone:",
        "casual": "Rewrite the following text in a casual, friendly, and simple tone:",
        "sheldon": "Rewrite the following text as if it were spoken by Sheldon, a character in the American sitcom, The Big Bang Theory."
    }

    if client is None:
        return "Error: OpenAI client is not initialized. Check your OpenAI API key in the .env file or available credits in the OpenAI Billing section."
    # Checking whether the transformation specified by the user is available in the pre-defined types. If it is available, store the corresponding prompt in instruction variable.
    instruction = prompts_for_transformation_types.get(transformation_type)
    if not instruction:
        return "Error: Invalid Transformation type specified."
    
    # The following are the instructions for the AI model
    system_prompt = "You are a helpful assistant that transforms text based on user instructions."
    user_prompt = f"{instruction}\n\n--- TEXT ---\n{original_text}"

    try:
        print(f"Requesting '{transformation_type}' transformation from the API...")
        response = client.chat.completions.create(
            model = "gpt-4.1-nano",
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature = 0.5, # Temperature is a parameter that can be adjusted for getting more predictable results or more creative results. Note that more creativity can mean factually wrong results as well.
            max_tokens = 250
        )

        # Extract the content from the response
        transformed_text = response.choices[0].message.content
        return transformed_text.strip()
    
    except Exception as e:
        return f"An error occurred with the API call: {e}"
    
# API Endpoint
@app.route("/api/transform", methods=["POST"])
def handle_transform_request():
    """This is the API endpoint that the frontend will call."""
    data = request.get_json()
    if not data or 'text' not in data or 'transformationType' not in data:
        return jsonify({"error": "Missing 'text' or 'transformationType' in request"})
    
    original_text = data['text']
    transformation_type = data['transformationType']

    transformed_text = transform_text(transformation_type, original_text)

    if transformed_text.startswith("Error:"):
        return jsonify({"Error": transformed_text}), 500
    
    return jsonify({"transformed_text": transformed_text})
    
# This block will run first when we execute the script directly. This block is for CLI app.

"""if __name__== "__main__":
    # Example text to work with:
    sample_text = Artificial intelligence (AI) is intelligence demonstrated by machines,
    as opposed to the natural intelligence displayed by humans and animals.
    Leading AI textbooks define the field as the study of "intelligent agents":
    any device that perceives its environment and takes actions that maximize
    its chance of successfully achieving its goals.
    sample_text = input("Enter text you want to transform:\n")
    print("Types of transformations available:\n1. Summarize\n2. Keywords\n3. Formal\n4. Casual\n5. Sheldon\n")
    transform_type = input("Enter the type of transformation you want to perform on the text: ")

    print("--- Original Text ---")
    print(sample_text)
    print("---------------------\n")

    # Testing the transform_text() function
    output_text = transform_text(transform_type.lower(), sample_text)
    print(f"--- {transform_type.capitalize()} ---")
    print(output_text)"""

# The following block of code is for initializing the Flask server.

if __name__ == "__main__":
    # Runs the Flask server on http://127.0.0.1:5000
    # The debug = True flag provides helpful error messages and auto-reloads the server on changes.
    app.run(debug = True, port = 5000)