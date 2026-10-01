# AI FAQ Generator

## Project Description

AI FAQ Generator is a web application that uses Generative AI to create frequently asked questions and answers from user-provided content.

## Features

- Generate FAQs using AI
- Accept user-provided topics or content
- Select the number of FAQs
- Generate clear questions and answers
- Simple and user-friendly interface
- Handles empty input and API errors

## Technologies Used

- Python
- Streamlit
- Google Gemini API

## Workflow

User Input
↓
Prompt Design
↓
Gemini AI API
↓
Response Generation
↓
Generated FAQs

## How to Run

1. Install the required packages:

   pip install -r requirements.txt

2. Run the application:

   streamlit run app.py

3. Enter your Gemini API key.
4. Enter the topic or content.
5. Select the number of FAQs.
6. Click **Generate FAQs**.

## Expected Outcome

The application generates relevant frequently asked questions and answers based on the content provided by the user.

## Testing

The application was tested with college-related content and successfully generated multiple questions and answers.

## Conclusion

The AI FAQ Generator demonstrates the use of prompt design, AI API integration, context handling, and response generation using Python and Streamlit.