import streamlit as st

st.set_page_config(page_title="Bitcoin Quiz", layout="centered")

st.title("🧠 Bitcoin Quiz App")
st.subheader("Test your Bitcoin knowledge!")

questions = [
    {
        "question": "Who is the creator of Bitcoin?",
        "options": ["Vitalik Buterin", "Elon Musk", "Satoshi Nakamoto", "Charles Hoskinson"],
        "answer": "Satoshi Nakamoto"
    },
    {
        "question": "What is the maximum supply of Bitcoin?",
        "options": ["10 million", "21 million", "100 million", "Unlimited"],
        "answer": "21 million"
    },
    {
        "question": "What is Bitcoin halving?",
        "options": [
            "A software bug",
            "A drop in value",
            "A reduction of block rewards",
            "A fork in the blockchain"
        ],
        "answer": "A reduction of block rewards"
    },
    {
        "question": "What year was Bitcoin launched?",
        "options": ["2008", "2009", "2010", "2012"],
        "answer": "2009"
    },
    {
        "question": "Which technology is Bitcoin built on?",
        "options": ["Ethereum", "Blockchain", "AI", "Cloud Computing"],
        "answer": "Blockchain"
    }
]

score = 0

for q in questions:
    st.write("### " + q["question"])
    user_answer = st.radio("Select an answer:", q["options"], key=q["question"])
    if user_answer == q["answer"]:
        score += 1

st.write("---")
st.write(f"✅ Your Score: {score} / {len(questions)}")

if score == len(questions):
    st.success("🎉 You're a Bitcoin genius!")
elif score >= 3:
    st.info("💪 Good job! Keep learning.")
else:
    st.warning("👀 Brush up on your Bitcoin basics.")
