import streamlit as st
import random

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        background-color: #1e1e1e;
        color: white;
        font-family: 'Arial', sans-serif;
    }
    .stButton>button {
        width: 100%;
        font-size: 18px;
        padding: 10px;
        border-radius: 10px;
        transition: 0.3s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #ff4757 !important;
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# Game Title
st.markdown("<h1 style='text-align: center; color: #ff4757;'>🪨📜✂️ Rock, Paper, Scissors</h1>", unsafe_allow_html=True)
st.write("### 🤖 Play against the Computer!")

# Game Choices
choices = ["Rock ✊", "Paper 📜", "Scissors ✂️"]
user_choice = st.selectbox("👉 Select your move:", choices)

# Play Button
if st.button("🔥 Play Now!"):
    computer_choice = random.choice(choices)

    # Display Choices
    st.markdown(f"<h3>🧑‍💻 You chose: {user_choice}</h3>", unsafe_allow_html=True)
    st.markdown(f"<h3>🤖 Computer chose: {computer_choice}</h3>", unsafe_allow_html=True)

    # Determine Winner
    user_choice_clean = user_choice.split(" ")[0]  # Extract text without emoji
    computer_choice_clean = computer_choice.split(" ")[0]

    if user_choice_clean == computer_choice_clean:
        result = "😮 It's a tie!"
    elif (
        (user_choice_clean == "Rock" and computer_choice_clean == "Scissors") or
        (user_choice_clean == "Paper" and computer_choice_clean == "Rock") or
        (user_choice_clean == "Scissors" and computer_choice_clean == "Paper")
    ):
        result = "🎉 You win!"
    else:
        result = "😢 Computer wins!"

    # Display Result
    st.markdown(f"<h2 style='text-align: center; color: #ff4757;'>{result}</h2>", unsafe_allow_html=True)

# Reset Button (Clears game state)
if st.button("🔄 Reset Game"):
    st.rerun()  # ✅ Corrected method to restart Streamlit app

# Footer
st.markdown("<h4 style='text-align: center; color: #ff4757;'>Made with ❤️ by <a >Mohsin</a></h4>", unsafe_allow_html=True)