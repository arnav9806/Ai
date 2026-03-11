import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)


def generate_questions(topic, language, difficulty, question_type):

    system_prompt = """
You are an AI interview assistant.
Your task is to generate interview questions.

Rules:
1. Always generate exactly 5 questions.
2. Questions must be clear and concise.
3. Do not include explanations.
4. Return only a numbered list.
5. If question type is Programming, do NOT include code examples.
"""

    user_prompt = f"""
Generate 5 {difficulty} level {question_type} interview questions 
about the topic '{topic}' in the programming language '{language}'.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content