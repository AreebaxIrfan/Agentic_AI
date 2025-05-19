import streamlit as st
import random
from datetime import datetime
# Configure page

st.set_page_config(
    page_title="Growth Mindset Companion",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed"
)
# Enhanced professional CSS with dark theme
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&family=Montserrat:wght@400;600;700&display=swap');
    
    :root {
        --primary: #3a86ff;
        --secondary: #8338ec;
        --accent: #ff006e;
        --background: #1a1a2e;
        --card-bg: #2a2a40;
        --text: #e0e1dd;
        --shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
    }
    
    body {
        font-family: 'Montserrat', sans-serif;
        background-color: var(--background);
        color: var(--text);
    }
    
    .main {
        background: var(--background);
    }
    
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
        padding: 2rem;
    }
    
    .card {
        background: var(--card-bg);
        border-radius: 12px;
        color: var(--text);
        padding: 2rem;
        margin: 1.5rem 0;
        box-shadow: var(--shadow);
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 12px rgba(0, 0, 0, 0.3);
    }
    
    .quote-container {
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        color: white;
        border-radius: 12px;
        padding: 2rem;
        margin: 1.5rem 0;
        font-size: 1.2rem;
        box-shadow: var(--shadow);
        text-align: center;
    }
    
    .progress-bar {
        height: 12px;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 6px;
        overflow: hidden;
        margin-top: 1.5rem;
    }
    
    .progress-fill {
        height: 100%;
        background: linear-gradient(90deg, var(--primary), var(--secondary));
        transition: width 0.5s ease;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        color: white;
        border: none;
        padding: 0.8rem 1.5rem;
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: var(--shadow);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.3);
    }
    
    .stExpander {
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        overflow: hidden;
        margin: 1.5rem 0;
    }
    
    .stExpander > div[role="button"] {
        background-color: var(--card-bg);
        color: var(--primary);
        font-weight: 600;
        padding: 1rem;
    }
    
    .stExpander > div[role="button"]:hover {
        color: var(--secondary);
    }
    
    .stTextArea > div > div > textarea {
        background-color: rgba(255, 255, 255, 0.05);
        color: var(--text);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 8px;
        padding: 1rem;
    }
    
    h1, h2, h3 {
        color: var(--primary);
        font-weight: 700;
    }
    
    h1 {
        text-align: center;
        margin-bottom: 2rem;
        font-size: 3rem;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
    }
    
    h2 {
        margin-top: 1.5rem;
        font-size: 2rem;
    }
    
    h3 {
        font-size: 1.6rem;
        margin-bottom: 1rem;
    }
    
    @media (max-width: 768px) {
        .stApp {
            padding: 1rem;
        }
        
        h1 {
            font-size: 2.5rem;
        }
        
        .card, .quote-container {
            padding: 1.5rem;
        }
        
        .stButton > button {
            width: 100%;
        }
    }
    </style>
""", unsafe_allow_html=True)

# App content
st.title("🌱 Growth Mindset Companion")

# Initialize session state
if 'progress' not in st.session_state:
    st.session_state.progress = 0
if 'streak' not in st.session_state:
    st.session_state.streak = 0
if 'entries' not in st.session_state:
    st.session_state.entries = []

# Motivational Quote Generator
def get_quote():
    quotes = [
        "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
        "It's not that I'm so smart, it's just that I stay with problems longer. - Albert Einstein",
        "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill"
    ]
    return random.choice(quotes)

# Daily Challenge Generator
def daily_challenge():
    challenges = [
        "Learn something new outside your comfort zone",
        "Reframe a recent mistake as a learning opportunity",
        "Teach someone else a concept you're learning",
        "Identify 3 areas for improvement in your work",
        "Practice deliberate focus for 25 minutes"
    ]
    return random.choice(challenges)

# Main App Layout
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown(f'<div class="quote-container">📖 {get_quote()}</div>', unsafe_allow_html=True)

    # Progress Section
    st.markdown(f"""
        <div class="card">
            <h3>Your Progress</h3>
            <div class="progress-bar">
                <div class="progress-fill" style="width: {st.session_state.progress}%"></div>
            </div>
            <p style="margin-top: 1.5rem">🔥 Current Streak: {st.session_state.streak} days</p>
        </div>
    """, unsafe_allow_html=True)

    # Interactive Features
    with st.expander("💪 Daily Growth Challenge", expanded=True):
        challenge = daily_challenge()
        st.subheader("Today's Challenge:")
        st.markdown(f"**{challenge}**")
        if st.button("Complete Challenge ✅"):
            st.session_state.progress = min(st.session_state.progress + 15, 100)
            st.session_state.streak += 1
            st.success("Great work! Your progress has been updated.")

    with st.expander("📝 Reflection Journal"):
        reflection = st.text_area("What did you learn today?", height=150)
        if st.button("Save Reflection"):
            entry = {
                "date": datetime.now().strftime("%Y-%m-%d"),
                "content": reflection
            }
            st.session_state.entries.append(entry)
            st.success("Reflection saved!")

with col2:
    with st.expander("🧠 Growth Mindset Toolkit", expanded=True):
        st.markdown("""
            ### Core Principles
            - **Neuroplasticity**: Your brain grows with practice
            - **Process over Outcome**: Value learning over perfect results
            - **Constructive Struggle**: Difficulty leads to growth
            
            ### Actionable Strategies
            1. Add 'yet' to self-limiting statements
            2. Analyze mistakes for learning opportunities
            3. Celebrate small improvements
        """)

    # Learning Resources
    with st.expander("📚 Recommended Resources", expanded=True):
        st.markdown("""
            - **Books**: 
              - *Mindset* by Carol Dweck
              - *Grit* by Angela Duckworth
            - **Tools**:
              - Pomodoro Timer (25min focus sessions)
              - SMART Goal Planner
            - **Courses**:
              - Learning How to Learn (Coursera)
              - Mindshift: Break Through Obstacles (FutureLearn)
        """)
