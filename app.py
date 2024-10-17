from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Set your OpenAI API key here
OPENAI_API_KEY = 'your Api key'

# Helper function to interact with the ChatGPT API
def ask_chatgpt(prompt):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {OPENAI_API_KEY}',
    }

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": prompt},
        ],
        "max_tokens": 300,
        "temperature": 0.7,
    }

    try:
        response = requests.post(
            'https://api.openai.com/v1/chat/completions',
            headers=headers,
            json=payload
        )
        response.raise_for_status()
        result = response.json()
        return result['choices'][0]['message']['content'].strip()

    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

# Route to render the home page with the HTML form
@app.route('/')
def index():
    return render_template('index.html')

# Route to generate the 100-word comment based on product description
@app.route('/generate-comment', methods=['POST'])
def generate_comment():
    description = request.form.get('description')
    language = request.form.get('language', 'English')

    comment_prompt = (
        f"The following text is the product's description. Please generate a 100-word "
        f"comment about the product in {language}.\n\n===> {description}"
    )

    comment = ask_chatgpt(comment_prompt)

    return jsonify({
        'comment': comment
    })

# Route to handle the POST request and generate all necessary outputs
@app.route('/process', methods=['POST'])
def process_comment():
    description = request.form.get('description')
    language = request.form.get('language', 'English')

    # Step 1: Generate a subject based on the comment
    comment_prompt = (
        f"The following text is the product's description. Please generate a 100-word "
        f"comment about the product in {language}.\n\n===> {description}"
    )
    comment = ask_chatgpt(comment_prompt)

    subject_prompt = (
        f"The following text is the customer's comment about the product. "
        f"Generate a subject in {language}.\n\n===> {comment}"
    )
    subject = ask_chatgpt(subject_prompt)

    summary_prompt = (
        f"The following text is the customer's comment about the product. "
        f"Generate a 1-2 sentence summary in {language}.\n\n===> {comment}"
    )
    summary = ask_chatgpt(summary_prompt)

    sentiment_prompt = (
        f"The following text is the customer's comment about the product. "
        f"Analyze the sentiment (positive, negative, or neutral) in {language}.\n\n===> {comment}"
    )
    sentiment = ask_chatgpt(sentiment_prompt)

    email = request.form.get('email')

    return jsonify({
        'subject': subject,
        'summary': summary,
        'sentiment': sentiment,
        'email': email
    })

if __name__ == '__main__':
    app.run(debug=True)