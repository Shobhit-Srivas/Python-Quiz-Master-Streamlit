import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Python Quiz Master",
    page_icon="🐍",
    layout="centered"
)

# Questions Dictionary
questions = {
    "1. Who developed Python?": "Guido van Rossum",
    "2. What keyword is used to define a function in Python?": "def",
    "3. Which data type is used to store True or False values?": "bool",
    "4. What symbol is used for comments in Python?": "#",
    "5. Which function is used to display output in Python?": "print",
    "6. Which function is used to take user input in Python?": "input",
    "7. What is the file extension of Python files?": ".py",
    "8. Which keyword is used to create a loop that runs while a condition is true?": "while",
    "9. Which keyword is used to import modules in Python?": "import",
    "10. Which data structure uses key-value pairs in Python?": "dictionary"
}

# Title
st.title("🐍 Python Quiz Master")
st.write("Answer all 10 questions before submitting the quiz.")

st.markdown("---")

# Quiz Form
with st.form("quiz_form"):

    user_answers = {}

    for question in questions:
        user_answers[question] = st.text_input(question)

    submit = st.form_submit_button("🚀 Submit Quiz")

# Submit Logic
if submit:

    # Check for unanswered questions
    unanswered_questions = []

    for question, answer in user_answers.items():
        if answer.strip() == "":
            unanswered_questions.append(question)

    # If questions are missing
    if len(unanswered_questions) > 0:

        st.error(
            f"⚠️ Please answer all {len(questions)} questions before submitting."
        )

        st.subheader("❌ Unanswered Questions")

        for q in unanswered_questions:
            st.write(q)

    # If all questions answered
    else:

        score = 0

        st.markdown("---")
        st.subheader("📊 Quiz Results")

        for question, correct_answer in questions.items():

            user_answer = user_answers[question]

            if user_answer.strip().lower() == correct_answer.lower():

                st.success(f"✅ Correct: {question}")
                score += 1

            else:

                st.error(
                    f"❌ Wrong: {question}\n\nCorrect Answer: {correct_answer}"
                )

        percentage = (score / len(questions)) * 100

        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("🏆 Score", f"{score}/{len(questions)}")

        with col2:
            st.metric("📈 Percentage", f"{percentage:.2f}%")

        st.progress(int(percentage))

        if percentage >= 80:
            st.balloons()
            st.success(
                "🎉 Excellent! You have strong Python knowledge."
            )

        elif percentage >= 50:
            st.info(
                "👍 Good Job! Keep practicing and you'll improve even more."
            )

        else:
            st.warning(
                "📚 Keep Learning and Try Again!"
            )

        st.markdown("---")

        st.subheader("📌 Final Result")

        if score == 10:
            st.success("🌟 Perfect Score! 10/10")

        elif score >= 8:
            st.success("🔥 Outstanding Performance!")

        elif score >= 5:
            st.info("👍 Good Performance!")

        else:
            st.warning("💡 Practice Python basics and try again.")