Customer Support Email Generator
This Flask web application allows users to generate automated email components based on product descriptions. It integrates with OpenAI's GPT-3.5-turbo model to create comments, summaries, subject lines, and perform sentiment analysis based on user-provided product descriptions. This can be useful for automating customer support or marketing responses.

**Features**
Generate Comments: Create a 100-word comment based on a product description.
Generate Subject Lines: Create an email subject line from the generated comment.
Summarize Comments: Provide a brief summary (1-2 sentences) of the comment.
Sentiment Analysis: Determine if the comment sentiment is positive, negative, or neutral.
Supports Multiple Languages: Generate responses in various languages based on user selection.
**Prerequisites**
Before you begin, ensure you have met the following requirements:

Python 3.8+
An OpenAI account with API access.
Flask installed (pip install flask)
requests library installed (pip install requests)

**Setup**
1. Clone the repository:
git clone https://github.com/your-username/customerSupportChatbot.git
cd customerSupportChatbot

2. **Install dependencies:**
pip install -r requirements.txt

3. **Set your OpenAI API Key:**
Replace the OPENAI_API_KEY in app.py with your actual OpenAI API key.
OPENAI_API_KEY = 'sk-your-api-key-here'

5. **Run the Flask application:**

**Usage**
Open the application and navigate to the home page.
Enter the product description and select the preferred language.
Click on "Generate Comment" to receive a 100-word comment.
To generate a complete response with subject line, summary, and sentiment analysis:
Submit the form on the /process route.
The app will return the generated outputs in JSON format.

**Example API Requests**
**Generate Comment**
Endpoint: /generate-comment
Method: POST
Parameters:

{
    "description": "This is a high-quality leather wallet, designed to be both stylish and durable.",
    "language": "English"
}

**Response**

{
    "subject": "Stylish & Durable Leather Wallet - Customer Review",
    "summary": "This is a positive review highlighting the wallet's stylish design and durability.",
    "sentiment": "positive",
    "email": "user@example.com"
}

**Dependencies**
Add these dependencies to your requirements.txt:
Flask==2.2.5
requests==2.31.0




