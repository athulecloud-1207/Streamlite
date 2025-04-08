import streamlit as st
import random

st.set_page_config(page_title="Random Dialogue Generator", page_icon="🎭", layout="centered")

st.title("🎭 Random Dialogue Generator")
st.markdown("### Let's see what your characters are saying today...")

# Define characters and possible lines
characters = ["Alex", "Jamie", "Taylor", "Morgan"]

lines = [
    "Did you hear what happened yesterday?",
    "No way! Are you serious?",
    "That was totally unexpected.",
    "I can't believe they actually did it.",
    "This changes everything.",
    "Well, we have to do something about it.",
    "Let’s not rush into anything.",
    "You're right... but we can't ignore it either.",
    "So, what's the plan?",
    "I guess we’re about to find out."
]

# Generate random dialogue
def generate_dialogue(num_lines=6):
    dialogue = []
    current_speaker = random.choice(characters)
    for _ in range(num_lines):
        line = random.choice(lines)
        dialogue.append(f"**{current_speaker}**: {line}")
        # Switch speaker
        other_characters = [char for char in characters if char != current_speaker]
        current_speaker = random.choice(other_characters)
    return dialogue

# Show dialogue on button click
if st.button("🎬 Generate Dialogue"):
    st.markdown("#### 🗯️ Dialogue:")
    for line in generate_dialogue():
        st.markdown(line)
else:
    st.info("Click the button to generate a dialogue between characters.")

# Footer
st.markdown("---")
st.caption("A fun tool for writers, storytellers, and curious minds.")
