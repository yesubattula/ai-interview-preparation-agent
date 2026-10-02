import streamlit as st
from agent import generate_interview_questions, evaluate_answer


# ==========================================
# PAGE SETTINGS
# ==========================================

st.set_page_config(
    page_title="AI Interview Preparation Agent",
    page_icon="🎯",
    layout="centered"
)


# ==========================================
# TITLE
# ==========================================

st.title("🎯 AI Interview Preparation Agent")

st.write(
    "Prepare for your interview with an AI-powered interview coach."
)


# ==========================================
# INTERVIEW PREPARATION
# ==========================================

st.subheader("📚 Interview Preparation")

interview_type = st.selectbox(
    "Select Interview Type",
    [
        "Technical Interview",
        "HR Interview"
    ]
)


# ==========================================
# JOB ROLE
# ==========================================

job_role = st.text_input(
    "Enter your Job Role",
    placeholder="Example: Python Developer"
)


# ==========================================
# GENERATE QUESTIONS
# ==========================================

if st.button("🚀 Generate Interview Questions"):

    if not job_role.strip():

        st.warning("Please enter a job role.")

    else:

        with st.spinner("Preparing interview questions..."):

            try:

                questions = generate_interview_questions(
                    job_role,
                    interview_type
                )

                st.session_state["questions"] = questions
                st.session_state["job_role"] = job_role

                st.success(
                    "Interview questions generated successfully!"
                )

            except Exception as e:

                st.error("Something went wrong.")

                st.error(str(e))


# ==========================================
# DISPLAY QUESTIONS
# ==========================================

if "questions" in st.session_state:

    st.markdown("---")

    st.subheader("📋 Interview Questions")

    st.write(
        st.session_state["questions"]
    )


# ==========================================
# PRACTICE YOUR ANSWER
# ==========================================

if "questions" in st.session_state:

    st.markdown("---")

    st.subheader("📝 Practice Your Answer")

    question = st.text_area(
        "Enter an interview question",
        placeholder="Example: What is Python?",
        height=100
    )

    answer = st.text_area(
        "Write your answer",
        placeholder="Type your interview answer here...",
        height=180
    )


    # ======================================
    # EVALUATE ANSWER
    # ======================================

    if st.button("🎯 Evaluate My Answer"):

        if not question.strip():

            st.warning(
                "Please enter an interview question."
            )

        elif not answer.strip():

            st.warning(
                "Please write your answer."
            )

        else:

            with st.spinner(
                "🤖 AI is evaluating your answer..."
            ):

                try:

                    feedback = evaluate_answer(
                        st.session_state["job_role"],
                        question,
                        answer
                    )

                    st.markdown("---")

                    st.subheader("📊 AI Evaluation")

                    st.write(feedback)

                except Exception as e:

                    st.error(
                        "Something went wrong while evaluating the answer."
                    )

                    st.error(str(e))


# ==========================================
# CLEAR BUTTON
# ==========================================

st.markdown("---")

if st.button("🔄 Start New Interview"):

    st.session_state.clear()

    st.rerun()