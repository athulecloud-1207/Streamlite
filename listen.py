import streamlit as st
import random

st.set_page_config(page_title="Random Quote Generator", page_icon="📝")

st.title("📝 Random Quote Generator")

quotes = [
    "Believe in yourself.",
    "Stay hungry, stay foolish.",
    "Success is no accident.",
    "Dream big and dare to fail.",
    "Turn your wounds into wisdom.",
    "Whatever you are, be a good one.",
]

if st.button("✨ Show me a quote"):
    st.success(random.choice(quotes))
else:
    st.write("Click the button to get inspired!")
