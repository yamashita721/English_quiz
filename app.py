import streamlit as st
import random
import sqlite3
from datetime import datetime
from typing import List, Dict, Any
import os

# Import questions from the original file
from english_quiz import questions

# Page config
st.set_page_config(
    page_title="English Grammar Quiz",
    page_icon="🎓",
    layout="wide"
)

# Database setup
def init_database():
    """Initialize the database and create tables if they don't exist"""
    conn = sqlite3.connect('quiz_data.db')
    c = conn.cursor()
    
    # Create table for quiz attempts
    c.execute('''
        CREATE TABLE IF NOT EXISTS quiz_attempts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            score INTEGER,
            total_questions INTEGER,
            percentage REAL,
            quiz_mode TEXT,
            difficulty TEXT,
            timestamp TEXT,
            date TEXT
        )
    ''')
    
    # Create table for detailed results
    c.execute('''
        CREATE TABLE IF NOT EXISTS quiz_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            attempt_id INTEGER,
            question TEXT,
            user_answer TEXT,
            correct_answer TEXT,
            is_correct INTEGER,
            category TEXT,
            difficulty TEXT,
            FOREIGN KEY (attempt_id) REFERENCES quiz_attempts(id)
        )
    ''')
    
    conn.commit()
    return conn

def save_quiz_result(conn, username, score, total, percentage, mode, difficulty, results_data):
    """Save quiz attempt and detailed results to database"""
    c = conn.cursor()
    
    # Insert quiz attempt
    timestamp = datetime.now().isoformat()
    date = datetime.now().strftime("%Y-%m-%d")
    
    c.execute('''
        INSERT INTO quiz_attempts 
        (username, score, total_questions, percentage, quiz_mode, difficulty, timestamp, date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (username, score, total, percentage, mode, difficulty, timestamp, date))
    
    attempt_id = c.lastrowid
    
    # Insert detailed results
    for result in results_data:
        c.execute('''
            INSERT INTO quiz_results 
            (attempt_id, question, user_answer, correct_answer, is_correct, category, difficulty)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            attempt_id,
            result['question'],
            result['user_answer'],
            result['correct_answer'],
            1 if result['is_correct'] else 0,
            result.get('category', 'General'),
            result.get('difficulty', 'Medium')
        ))
    
    conn.commit()
    return attempt_id

def get_statistics(conn):
    """Get overall statistics from database"""
    c = conn.cursor()
    
    # Total attempts
    c.execute('SELECT COUNT(*) FROM quiz_attempts')
    total_attempts = c.fetchone()[0]
    
    # Average score
    c.execute('SELECT AVG(percentage) FROM quiz_attempts')
    avg_score = c.fetchone()[0] or 0
    
    # Total users
    c.execute('SELECT COUNT(DISTINCT username) FROM quiz_attempts')
    total_users = c.fetchone()[0]
    
    # Today's attempts
    today = datetime.now().strftime("%Y-%m-%d")
    c.execute('SELECT COUNT(*) FROM quiz_attempts WHERE date = ?', (today,))
    today_attempts = c.fetchone()[0]
    
    return {
        'total_attempts': total_attempts,
        'avg_score': round(avg_score, 1),
        'total_users': total_users,
        'today_attempts': today_attempts
    }

def get_user_history(conn, username):
    """Get quiz history for a specific user"""
    c = conn.cursor()
    c.execute('''
        SELECT score, total_questions, percentage, quiz_mode, difficulty, timestamp
        FROM quiz_attempts
        WHERE username = ?
        ORDER BY timestamp DESC
        LIMIT 10
    ''', (username,))
    return c.fetchall()

# Initialize database
conn = init_database()

# Main app
def main():
    st.title("🎓 English Grammar Quiz")
    st.markdown("---")
    
    # Sidebar for navigation and stats
    with st.sidebar:
        st.header("📊 Dashboard")
        
        # Get and display statistics
        stats = get_statistics(conn)
        st.metric("Total Attempts", stats['total_attempts'])
        st.metric("Average Score", f"{stats['avg_score']}%")
        st.metric("Total Users", stats['total_users'])
        st.metric("Today's Attempts", stats['today_attempts'])
        
        st.markdown("---")
        st.header("🔍 View Data")
        if st.button("View All Results"):
            st.session_state['view_data'] = True
            st.session_state['start_quiz'] = False
        if st.button("📊 View Statistics"):
            st.session_state['view_stats'] = True
            st.session_state['start_quiz'] = False
    
    # Initialize session state
    if 'quiz_started' not in st.session_state:
        st.session_state['quiz_started'] = False
    if 'current_question' not in st.session_state:
        st.session_state['current_question'] = 0
    if 'score' not in st.session_state:
        st.session_state['score'] = 0
    if 'user_answers' not in st.session_state:
        st.session_state['user_answers'] = []
    if 'quiz_questions' not in st.session_state:
        st.session_state['quiz_questions'] = []
    if 'quiz_finished' not in st.session_state:
        st.session_state['quiz_finished'] = False
    if 'username' not in st.session_state:
        st.session_state['username'] = ""
    if 'view_data' not in st.session_state:
        st.session_state['view_data'] = False
    if 'view_stats' not in st.session_state:
        st.session_state['view_stats'] = False
    
    # View data page
    if st.session_state.get('view_data'):
        view_data_page(conn)
        return
    
    # View statistics page
    if st.session_state.get('view_stats'):
        view_statistics_page(conn)
        return
    
    # Quiz hasn't started
    if not st.session_state['quiz_started']:
        show_quiz_setup()
    
    # Quiz in progress
    elif st.session_state['quiz_started'] and not st.session_state['quiz_finished']:
        show_question()
    
    # Quiz finished
    elif st.session_state['quiz_finished']:
        show_results(conn)

def show_quiz_setup():
    """Display quiz setup page"""
    st.header("🎯 Welcome to the English Grammar Quiz!")
    
    # Get username
    username = st.text_input("Enter your name (optional):", placeholder="Your name here...")
    
    # Build topic list from questions
    topic_set = sorted({q.get('category', 'General') for q in questions})
    topic_options = ["All Topics"] + topic_set
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📝 Quiz Options")
        selected_topic = st.selectbox("Select Topic:", topic_options, index=0)
        shuffle_questions = st.checkbox("🔀 Shuffle questions", value=False)
    
    with col2:
        st.subheader("ℹ️ About the Quiz")
        st.info("""
        Choose a topic to focus your practice (e.g., Nouns, Adjectives, Tenses). 
        You can also select "All Topics" to include everything and optionally shuffle.
        
        **Examples of Topics:**
        - Nouns and Main Verbs; Number and Collection; Countable/Uncountable Nouns
        - Verb Forms and Helping Verbs; Possessive Nouns and Apostrophes
        - Pronouns and Possessive Pronouns; Adjectives; Articles; Prepositions; Question Words
        - Contractions and Interjections; Tenses; Possession
        - Tense Practice (Usual Activities, Factual Descriptions, Opinions, etc.)
        """)
    
    if st.button("🚀 Start Quiz", type="primary", use_container_width=True):
        # Prepare questions based on topic and shuffle preference
        if selected_topic == "All Topics":
            quiz_questions = questions.copy()
        else:
            quiz_questions = [q for q in questions if q.get('category', 'General') == selected_topic]
        
        if not quiz_questions:
            st.warning("No questions found for the selected topic.")
            return
        
        if shuffle_questions:
            random.shuffle(quiz_questions)
        
        # Initialize quiz state
        st.session_state['quiz_started'] = True
        st.session_state['quiz_questions'] = quiz_questions
        st.session_state['current_question'] = 0
        st.session_state['score'] = 0
        st.session_state['user_answers'] = []
        st.session_state['quiz_finished'] = False
        st.session_state['username'] = username if username else "Anonymous"
        st.session_state['quiz_mode'] = f"Topic: {selected_topic}"
        st.session_state['difficulty'] = selected_topic
        st.rerun()

def show_question():
    """Display current question"""
    current_idx = st.session_state['current_question']
    quiz_questions = st.session_state['quiz_questions']
    
    if current_idx >= len(quiz_questions):
        st.session_state['quiz_finished'] = True
        st.rerun()
        return
    
    question = quiz_questions[current_idx]
    
    # Progress bar
    progress = (current_idx + 1) / len(quiz_questions)
    st.progress(progress)
    st.caption(f"Question {current_idx + 1} of {len(quiz_questions)}")
    
    # Question display
    st.subheader(f"📝 {question['question']}")
    
    # Category and difficulty
    category = question.get('category', 'General')
    difficulty = question.get('difficulty', 'Medium')
    
    col1, col2 = st.columns(2)
    with col1:
        st.caption(f"📚 Category: {category}")
    with col2:
        difficulty_emoji = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴"}.get(difficulty, "⚪")
        st.caption(f"{difficulty_emoji} Difficulty: {difficulty}")
    
    st.markdown("---")
    
    # Options
    options = question['options']
    user_answer = st.radio(
        "Select your answer:",
        options,
        key=f"question_{current_idx}"
    )
    
    # Navigation buttons
    col1, col2, col3 = st.columns([1, 1, 2])
    
    with col1:
        if current_idx > 0:
            if st.button("⬅️ Previous", use_container_width=True):
                st.session_state['current_question'] -= 1
                st.rerun()
    
    with col2:
        if st.button("✅ Submit Answer", type="primary", use_container_width=True):
            # Extract answer letter
            answer_letter = user_answer[0]
            correct = answer_letter == question['answer']
            
            # Store result
            st.session_state['user_answers'].append({
                'question': question['question'],
                'user_answer': answer_letter,
                'correct_answer': question['answer'],
                'is_correct': correct,
                'category': category,
                'difficulty': difficulty
            })
            
            if correct:
                st.session_state['score'] += 1
            
            # Move to next question or finish
            st.session_state['current_question'] += 1
            
            if st.session_state['current_question'] >= len(quiz_questions):
                st.session_state['quiz_finished'] = True
            
            st.rerun()
    
    with col3:
        if st.button("🏁 Finish Quiz Early", use_container_width=True):
            st.session_state['quiz_finished'] = True
            st.rerun()

def show_results(conn):
    """Display quiz results and save to database"""
    quiz_questions = st.session_state['quiz_questions']
    user_answers = st.session_state['user_answers']
    score = st.session_state['score']
    total = len(user_answers) if user_answers else len(quiz_questions)
    percentage = (score / total * 100) if total > 0 else 0
    
    st.header("🏆 Quiz Results")
    
    # Score display
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Score", f"{score}/{total}")
    with col2:
        st.metric("Percentage", f"{percentage:.1f}%")
    with col3:
        if percentage >= 90:
            st.metric("Grade", "🌟 Excellent")
        elif percentage >= 80:
            st.metric("Grade", "🎉 Great")
        elif percentage >= 70:
            st.metric("Grade", "👍 Good")
        elif percentage >= 60:
            st.metric("Grade", "📚 Fair")
        else:
            st.metric("Grade", "💪 Keep Trying")
    
    st.markdown("---")
    
    # Save to database
    if user_answers:
        save_quiz_result(
            conn,
            st.session_state['username'],
            score,
            total,
            percentage,
            st.session_state.get('quiz_mode', 'Full Quiz'),
            st.session_state.get('difficulty', 'All'),
            user_answers
        )
        st.success("✅ Your results have been saved!")
    
    # Show incorrect answers
    incorrect = [ans for ans in user_answers if not ans['is_correct']]
    
    if incorrect:
        with st.expander(f"📝 Review {len(incorrect)} Incorrect Answers", expanded=False):
            for i, ans in enumerate(incorrect, 1):
                st.markdown(f"**{i}. {ans['question']}**")
                st.error(f"Your answer: {ans['user_answer']} | Correct: {ans['correct_answer']}")
                st.markdown("---")
    
    # User history
    if st.session_state['username']:
        history = get_user_history(conn, st.session_state['username'])
        if history:
            with st.expander("📊 Your Quiz History", expanded=False):
                for h in history[:5]:
                    st.text(f"Score: {h[0]}/{h[1]} ({h[2]:.1f}%) - {h[3]} - {h[5]}")
    
    # Restart button
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🔄 Take Another Quiz", type="primary", use_container_width=True):
            st.session_state['quiz_started'] = False
            st.session_state['quiz_finished'] = False
            st.session_state['current_question'] = 0
            st.session_state['score'] = 0
            st.session_state['user_answers'] = []
            st.rerun()

def view_data_page(conn):
    """Display all quiz data"""
    st.header("📊 All Quiz Results")
    
    c = conn.cursor()
    c.execute('''
        SELECT username, score, total_questions, percentage, quiz_mode, timestamp
        FROM quiz_attempts
        ORDER BY timestamp DESC
        LIMIT 100
    ''')
    
    results = c.fetchall()
    
    if results:
        # Display as table
        import pandas as pd
        df = pd.DataFrame(results, columns=['Username', 'Score', 'Total', 'Percentage', 'Mode', 'Timestamp'])
        st.dataframe(df, use_container_width=True)
        
        # Download button
        csv = df.to_csv(index=False)
        st.download_button(
            label="📥 Download as CSV",
            data=csv,
            file_name="quiz_results.csv",
            mime="text/csv"
        )
    else:
        st.info("No quiz results yet. Take a quiz to see results here!")
    
    if st.button("🔙 Back to Quiz"):
        st.session_state['view_data'] = False
        st.rerun()

def view_statistics_page(conn):
    """Display detailed statistics"""
    st.header("📈 Detailed Statistics")
    
    c = conn.cursor()
    
    # Category performance
    st.subheader("📚 Performance by Category")
    c.execute('''
        SELECT category, 
               COUNT(*) as total,
               SUM(CASE WHEN is_correct = 1 THEN 1 ELSE 0 END) as correct,
               ROUND(SUM(CASE WHEN is_correct = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1) as accuracy
        FROM quiz_results
        GROUP BY category
        ORDER BY total DESC
    ''')
    
    category_stats = c.fetchall()
    if category_stats:
        import pandas as pd
        df = pd.DataFrame(category_stats, columns=['Category', 'Total Questions', 'Correct', 'Accuracy %'])
        st.dataframe(df, use_container_width=True)
    
    st.markdown("---")
    
    # Recent attempts
    st.subheader("🕐 Recent Quiz Attempts")
    c.execute('''
        SELECT username, score, total_questions, percentage, timestamp
        FROM quiz_attempts
        ORDER BY timestamp DESC
        LIMIT 10
    ''')
    
    recent = c.fetchall()
    if recent:
        import pandas as pd
        df = pd.DataFrame(recent, columns=['Username', 'Score', 'Total', 'Percentage', 'Time'])
        st.dataframe(df, use_container_width=True)
    
    if st.button("🔙 Back to Quiz"):
        st.session_state['view_stats'] = False
        st.rerun()

if __name__ == "__main__":
    main()

