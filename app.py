import streamlit as st
from google import genai

st.set_page_config(page_title="AI FAQ Generator")

st.title("🤖 AI FAQ Generator")
st.write("Generate frequently asked questions using AI.")

api_key = st.text_input("Enter your Gemini API Key", type="password")

topic = st.text_area(
    "Enter your topic or content",
    placeholder="Example: Our college offers CSE, ISE, ECE and AIML courses."
)

number = st.slider("Number of FAQs", 3, 10, 5)

if st.button("Generate FAQs"):

    if not api_key:
        st.warning("Please enter your Gemini API key.")

    elif not topic.strip():
        st.warning("Please enter some content.")

    else:
        try:
            client = genai.Client(api_key=api_key)

            prompt = f"""
Generate {number} frequently asked questions and answers
from the following content:

{topic}

Make the questions clear and the answers simple and accurate.

Format:
1. Question:
   Answer:

2. Question:
   Answer:
"""

            with st.spinner("Generating FAQs..."):
                response = client.models.generate_content(
                    model="gemini-3.5-flash-lite",
                    contents=prompt
                )

            st.subheader("Generated FAQs")
            st.write(response.text)

        except Exception as e:
            st.error(f"Error: {e}")