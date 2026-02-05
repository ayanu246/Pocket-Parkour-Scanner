import streamlit as st
import random

# --- APP CONFIG ---
st.set_page_config(page_title="Wonders Study Hub - GGUSD", page_icon="📚")

# Custom CSS to make it look like the Wonders Portal
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #007bff; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("📚 GGUSD Wonders Study Hub")
st.caption("Master your Weekly Assessments and Shared Reads")

# --- SIDEBAR: NAVIGATION ---
st.sidebar.header("Select Your Level")
grade = st.sidebar.selectbox("Select Grade", ["Grade 1", "Grade 2", "Grade 3", "Grade 4", "Grade 5", "Grade 6"])
unit_week = st.sidebar.selectbox("Select Unit & Week", ["Unit 1 - Week 1", "Unit 1 - Week 2", "Unit 2 - Week 1"]) # We can add all of them

# --- DATABASE (Placeholder for GGUSD Wonders Data) ---
# We will fill this with the actual 'Small Version' stories and Vocab
wonders_data = {
    "Grade 5": {
        "Unit 1 - Week 1": {
            "story_title": "A Fresh Idea",
            "essential_question": "How do shared goals help people?",
            "vocab": {"Catastrophe": "A sudden disaster", "Strategy": "A plan for reaching a goal", "Motivation": "The reason why someone acts a certain way"},
            "summary": "This 'Shared Read' focuses on a community garden project where characters have to work together..."
        }
    }
}

# --- MAIN INTERFACE ---
tab1, tab2, tab3 = st.tabs(["📖 The Story", "🗂️ Flashcards", "📝 Practice Quiz"])

# Tab 1: The Small Story (Shared Read)
with tab1:
    if grade in wonders_data and unit_week in wonders_data[grade]:
        data = wonders_data[grade][unit_week]
        st.header(f"Story: {data['story_title']}")
        st.info(f"**Essential Question:** {data['essential_question']}")
        st.write("### Small Version Summary")
        st.write(data['summary'])
    else:
        st.warning("Data for this week is coming soon! Select Grade 5 / Unit 1 for a demo.")

# Tab 2: Vocabulary Flashcards
with tab2:
    st.header("Vocab Mastery")
    if grade in wonders_data and unit_week in wonders_data[grade]:
        vocab_list = wonders_data[grade][unit_week]['vocab']
        for word, definition in vocab_list.items():
            with st.expander(f"🔍 Word: {word}"):
                st.write(f"**Definition:** {definition}")
                if st.button(f"Mark '{word}' as Learned"):
                    st.toast(f"Good job! {word} added to your brain!")
    else:
        st.write("Choose a week to see the vocab list.")

# Tab 3: AI-Style Practice Quiz
with tab3:
    st.header("Test Prep")
    if grade in wonders_data and unit_week in wonders_data[grade]:
        st.write("Answer the following based on the 'Shared Read':")
        q1 = st.radio("What is the main theme of this week's reading?", 
                     ["Competition", "Collaboration", "Individualism"])
        
        if st.button("Submit Quiz"):
            if q1 == "Collaboration":
                st.success("Correct! GGUSD tests love focusing on the theme of working together.")
            else:
                st.error("Try again! Look back at the Essential Question.")

# --- FOOTER ---
st.divider()
st.write("✨ **Tip:** Most GGUSD Wonders tests use the same 'Vocabulary Strategy' every week (like Context Clues or Metaphors).")
