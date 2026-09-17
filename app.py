import streamlit as st
import os

# Dropdowns for subject and difficulty
subject = st.selectbox("Choose a subject", [
    "Math", "Science", "English", "Hindi", 
    "Marathi", "Social Studies", "General Knowledge", "Computer Science"
])

difficulty = st.selectbox("Choose difficulty", [
    "Easy", "Medium", "Hard", "Difficult"
])

# Map subject to file
file_map = {
    "Math": "math.md",
    "Science": "science.md",
    "English": "english.md",
    "Hindi": "hindi.md",
    "Marathi": "marathi.md",
    "Social Studies": "social_studies.md",
    "General Knowledge": "general_knowledge.md",
    "Computer Science": "computer_science.md"
}

# Load questions
file_path = os.path.join("questions", file_map[subject])
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Split by difficulty heading
sections = content.split("**")
questions = {}
for i in range(1, len(sections), 2):
    level = sections[i].strip()
    block = sections[i+1].strip()
    questions[level] = block.split("\n\n")

# Show questions for chosen difficulty
st.header(f"{subject} - {difficulty}")

score = 0
for idx, q in enumerate(questions.get(difficulty, [])):
    lines = q.split("\n")
    question = lines[0].replace("Q: ", "")
    options_line = [l for l in lines if l.startswith("Options:")][0]
    answer_line = [l for l in lines if l.startswith("Answer:")][0]

    options = options_line.replace("Options:", "").strip().split(",")
    correct = answer_line.replace("Answer:", "").strip()

    choice = st.radio(question, options, key=f"{difficulty}_{idx}")
    if choice == correct:
        score += 1

st.write(f"Your score: {score}/{len(questions.get(difficulty, []))}")
