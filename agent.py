import os
from dotenv import load_dotenv
from openai import OpenAI

# Load .env when running locally
load_dotenv(override=True)

# Get API key from local .env
api_key = os.getenv("OPENAI_API_KEY")

# If running on Streamlit Cloud, get API key from Streamlit Secrets
if not api_key:
    try:
        import streamlit as st
        api_key = st.secrets["OPENAI_API_KEY"]
    except Exception:
        api_key = None

# Check API key
if not api_key:
    raise ValueError(
        "OPENAI_API_KEY was not found. "
        "Add it to .env locally or Streamlit Secrets when deployed."
    )

# Create OpenAI client
client = OpenAI(api_key=api_key)


# --------------------------------------------------
# Generate Interview Questions
# --------------------------------------------------

def generate_interview_questions(job_role, interview_type):

    prompt = f"""
You are an expert interview preparation coach.

The candidate is preparing for:

Job Role: {job_role}
Interview Type: {interview_type}

Generate 5 important interview questions suitable for this role.

For each question:
1. Give the question.
2. Explain what the interviewer is looking for.
3. Give key points the candidate should include.

Keep the questions practical and suitable for a student or fresher.
"""

    response = client.responses.create(
        model="gpt-6-luna",
        input=prompt
    )

    return response.output_text


# --------------------------------------------------
# Evaluate Candidate Answer
# --------------------------------------------------

def evaluate_answer(job_role, question, answer):

    prompt = f"""
You are an expert interview evaluator.

Job Role: {job_role}

Interview Question:
{question}

Candidate Answer:
{answer}

Evaluate the candidate's answer.

Give the following:

1. Score out of 10
2. What was done well
3. What was missing
4. How to improve the answer
5. A better sample answer

Be constructive and suitable for a student or fresher.
"""

    response = client.responses.create(
        model="gpt-6-luna",
        input=prompt
    )

    return response.output_text
