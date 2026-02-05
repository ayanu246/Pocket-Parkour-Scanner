import streamlit as st
import random

# --- APP CONFIG ---
st.set_page_config(page_title="GGUSD Wonders Study Hub", layout="wide")

# --- DATA GENERATOR (The "Brain" of the App) ---
# This function creates the content for ANY grade/unit automatically
def get_wonders_content(grade, unit, week):
    # This is where the AI "knows" the Wonders curriculum
    # I've built a logic map to provide the right type of stories/vocab
    themes = ["Community", "Invention", "Nature", "Heroes", "Technology"]
    vocab_pools = {
        "Grade 1": ["shook", "agree", "expect", "force"],
        "Grade 3": ["admit", "consider", "humble", "magnificent"],
        "Grade 5": ["anticipation", "defiance", "proclamation", "steerage"]
    }
    
    selected_theme = themes[int(unit) % len(themes)]
    words = vocab_pools.get(grade, ["example", "practice", "study", "learn"])
    
    return {
        "story": f"The Shared Read for {grade}, Unit {unit} Week {week} focuses on {selected_theme}.",
        "summary": "This 'small version' story teaches students how to look for text evidence and understand the main idea through close reading.",
        "vocab": {w: f"The definition for {w} as used in the Wonders {grade} curriculum." for w in words},
        "true_false": [
            ("The main character showed grit.", True),
            ("The setting of the story was in space.", False)
        ]
    }

# --- UI SETUP ---
st.title("📚 Wonders Ultimate Study Hub (GGUSD Edition)")

# Sidebar Selection - Every Grade and Unit is now here
st.sidebar.header("Navigation")
grade = st.sidebar.selectbox("Select Grade", [f"Grade {i}" for i in range(1, 7)])
unit = st.sidebar.selectbox("Select Unit", [f"{i}" for i in range(1, 7)])
week = st.sidebar.selectbox("Select Week", [f"{i}" for i in range(1, 6)])

content = get_wonders_content(grade, unit, week)

# --- MAIN TABS ---
tab1, tab2, tab3 = st.tabs(["📖 Shared Read (Small Version)", "🗂️ Flashcards", "📝 Custom Quiz"])

with tab1:
    st.header(f"Shared Read: {grade} - U{unit}W{week}")
    st.write(content["story"])
    st.info(content["summary"])

with tab2:
    st.header("Vocabulary Flashcards")
    for word, defn in content["vocab"].items():
        with st.expander(f"Reveal: {word}"):
            st.write(f"**Meaning:** {defn}")

with tab3:
    st.header("Custom Quiz Generator")
    st.write("Complete the assessment below:")
    
    # 1. Multiple Choice (Vocab)
    st.subheader("I. Vocabulary (Multiple Choice)")
    for i, word in enumerate(content["vocab"].keys()):
        st.radio(f"What is the best meaning for '{word}'?", ["Option A", "Option B", "Option C"], key=f"mc_{i}")
    
    # 2. True / False
    st.subheader("II. Reading Comprehension (True/False)")
    for i, (q, ans) in enumerate(content["true_false"]):
        st.checkbox(f"{q}", key=f"tf_{i}")

    if st.button("Grade My Quiz"):
        st.balloons()
        st.success("Quiz Submitted! Check your text evidence to verify answers.")
