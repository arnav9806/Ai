import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)


def generate_questions(topic, language, difficulty, question_type):

    prompt = f"""
    Generate 5 {difficulty} level {question_type} interview questions 
    about {topic} related to {language}
    if {question_type} is programming it should not give any example just programing question .
    """

    response = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt}
        ],
        model="llama-3.3-70b-versatile"
    )

    return response.choices[0].message.content