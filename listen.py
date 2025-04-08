import streamlit as st
import random

st.set_page_config(page_title="Random Quote Generator", page_icon="📝", layout="centered")

# Title with emoji and spacing
st.title("📝 Random Quote Generator")
st.markdown("### Get your daily dose of inspiration!")

# Spacer
st.markdown("---")

# List of quotes
quotes = [
    "Believe in yourself.",
    "Stay hungry, stay foolish.",
    "Success is no accident.",
    "Dream big and dare to fail.",
    "Turn your wounds into wisdom.",
    "Whatever you are, be a good one.",
]

# Layout using columns to center the button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("✨ Show me a quote"):
        quote = random.choice(quotes)
        st.markdown("#### 💬 Here's your quote:")
        st.success(f"_{quote}_")
    else:
        st.info("Click the button to get inspired!")

# Footer spacer
st.markdown("---")
st.caption("Powered by Streamlit")
