import streamlit as st
import sys
import os
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.chatbot import generate_questions

st.title("AI Interview Question Generator")

# Programming language dropdown
language = st.selectbox(
    "Select Programming Language",
    ["Python", "Java", "JavaScript", "C++", "Go", "Rust"]
)

# Question type dropdown
question_type = st.selectbox(
    "Select Question Type",
    ["Technical", "Programming"]
)

# Difficulty level dropdown
difficulty = st.selectbox(
    "Select Difficulty Level",
    ["Beginner", "Intermediate", "Advanced"]
)

# Topic input
topic = st.text_input("Enter Topic")

if st.button("Generate Questions"):

    # Validation
    if not topic.strip():
        st.error("Sorry, please provide a proper input.")

    elif len(topic) < 3:
        st.error("Sorry, please provide a more meaningful topic.")

    elif not re.search("[a-zA-Z]", topic):
        st.error("Sorry, please provide a valid topic.")

    else:
        with st.spinner("Generating questions..."):
            questions = generate_questions(
                topic,
                language,
                difficulty,
                question_type
            )

        st.success("Questions Generated")
        st.write(questions)


# import streamlit as st
# import sys
# import os

# # add project root to path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from app.chatbot import generate_questions

# st.title("AI Interview Question Generator")

# topic = st.text_input("Enter Topic")

# if st.button("Generate Questions"):

#     if topic:
#         with st.spinner("Generating questions..."):
#             questions = generate_questions(topic)

#         st.success("Questions Generated")
#         st.write(questions)

#     else:
#         st.warning("Please enter a topic")