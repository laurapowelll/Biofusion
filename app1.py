import streamlit as st
import pandas as pd
from datetime import date, timedelta
import plotly.express as px

# CSS styling
st.markdown("""
    <style>
        .main {background-color: #f0f2f6;} /* Light gray background for main content */
        .sidebar .sidebar-content {background-color: #e3f2fd;} /* Light blue background for sidebar */
        .icon {
            font-size: 2em; /* Icon size */
            color: #2196F3; /* Icon color */
            margin-right: 10px;
        }
        .tile {
            background-color: #90caf9; /* Light blue background for tiles */
            border-radius: 10px;
            padding: 20px;
            margin: 10px 0;
            color: #fff;
            text-align: center;
            font-weight: bold;
        }
        .info-box {
            background-color: #f1f8e9;
            border-radius: 8px;
            padding: 15px;
            margin-top: 20px;
            font-size: 16px;
        }
        .goal-section {
            background-color: #d3e5ff;
            border-radius: 8px;
            padding: 15px;
            margin-top: 20px;
        }
        .card {
            background-color: #ffffff;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
    </style>
""", unsafe_allow_html=True)

# App Title and Description
st.title("🌱 BiYourFusion Health App")
st.write("""
Welcome to your personal health and wellness app. Track your health goals, fitness, menstrual cycle, nutrition, and immunization records all in one place.
""")

# Sidebar for navigation
st.sidebar.title("🌐 Navigation")
app_mode = st.sidebar.selectbox("Choose a section", [
    "Home", "WhyBiyourFusion", "Log Health Metrics", "Log Menstrual Cycle", 
    "Fitness & Exercise", "View Dashboard", "Set Goals", "Health Records", "Immunization Records", 
    "Terms of Service and Privacy Policy"
])

# Current Date Display
st.sidebar.write("### 📅 Current Date")
st.sidebar.write(date.today())

# Helper function for introducing the app
def show_intro():
    st.title("WhyBiyourFusion 🌟")
    st.markdown("""
        **BiyourFusion** is your ultimate health and wellness app, designed to help you track everything in one place. We offer features from fitness tracking, menstrual cycle logging, health records, to personalized wellness goals. Here's how we compare to other apps:

        ### Key Features:
        - **Health Goals**: Set and track goals for weight, calories, macronutrients, and more.
        - **Menstrual Cycle Tracking**: Log cycle phases, ovulation, contraception, and receive cycle tips.
        - **Fitness & Exercise**: Log workouts, track calories burned, access workout videos, and receive fitness plans.
        - **Health Records**: Keep a history of your health records and share them with your doctor.

        Our app simplifies your health management, providing you with personalized feedback and suggestions.
    """)

# Home Page with key metrics and tiles
if app_mode == "Home":
    st.subheader("Welcome to your Health Dashboard")
    st.write("Track your health metrics here and monitor your progress.")
    
    st.markdown("""
    <div class="tile">🚶 Steps Today: 0</div>
    <div class="tile">💧 Water Intake: 0 oz</div>
    <div class="tile">💤 Sleep: 0 hrs</div>
    """, unsafe_allow_html=True)

    st.write("### Daily Health Overview")
    st.write("Track your daily goals and metrics. You can log your steps, water intake, and sleep hours to stay on top of your health.")

# Log Health Metrics Page with icons and style improvements
elif app_mode == "Log Health Metrics":
    st.subheader("Log Your Health Metrics 🩺")

    steps = st.number_input("Steps Walked Today", min_value=0, max_value=50000, step=100, label_visibility="collapsed")
    sleep = st.number_input("Hours of Sleep", min_value=0.0, max_value=24.0, step=0.5)
    water_intake = st.number_input("Water Intake (oz)", min_value=0, max_value=300, step=1)

    st.button("Save Entry", key="save_health_metrics")
    
    if st.button("Save Entry"):
        st.success("Health metrics logged successfully!")
        # Save this data in a more complex system (like database or in-memory for real-time tracking)
    
    st.markdown(f"**📊 Health Insights**")
    st.write("Monitor your health with graphs and trends over time. Here's a simple trend chart for your steps today:")
    
    # Example graph for steps:
    df = pd.DataFrame({"Date": [date.today()], "Steps": [steps]})
    st.line_chart(df.set_index("Date"))

# Log Menstrual Cycle Page with deeper functionality
elif app_mode == "Log Menstrual Cycle":
    st.subheader("Log Your Menstrual Cycle 🌸")

    cycle_start = st.date_input("Cycle Start Date")
    cycle_end = st.date_input("Cycle End Date", min_value=cycle_start)
    cycle_length = (cycle_end - cycle_start).days
    st.write(f"Cycle Length: {cycle_length} days")
    
    ovulation_date = st.date_input("Ovulation Date (estimated)", min_value=cycle_start, max_value=cycle_end)

    contraceptive_type = st.selectbox("Contraceptive Method", [
        "None", "Birth Control Pill", "IUD", "Condom", "Natural Rhythm", "Other"
    ])
    contraceptive_notes = st.text_area("Additional Notes (Optional)")

    trying_to_conceive = st.radio("Trying to Conceive?", ["Yes", "No"])
    had_unprotected_sex = st.radio("Had Unprotected Sex?", ["Yes", "No"])
    
    # Save button
    if st.button("Save Cycle Data"):
        st.success("Menstrual cycle data saved!")
        st.write(f"Cycle Start: {cycle_start}, Cycle End: {cycle_end}, Ovulation Date: {ovulation_date}")

    st.markdown("""
        ### Tips for Each Phase
        Learn more about what to eat, how to exercise, and mental wellness during different phases of your cycle.
    """)

    phase = st.radio("Select a Phase", ["Menstrual", "Follicular", "Ovulation", "Luteal"])
    if phase == "Menstrual":
        st.write("""
        **During Your Period**:
        - Eat Iron-rich foods (spinach, lentils), avoid caffeine and processed foods.
        - Gentle exercise like walking, yoga is recommended.
        """)
    elif phase == "Follicular":
        st.write("""
        **Follicular Phase**:
        - Great time to boost productivity and tackle creative projects.
        - Include protein-rich foods and engage in intense exercise like running or HIIT.
        """)
    elif phase == "Ovulation":
        st.write("""
        **Ovulation Phase**:
        - Antioxidants (berries, leafy greens) will help boost energy.
        - High-intensity workouts like HIIT are recommended.
        """)
    elif phase == "Luteal":
        st.write("""
        **Luteal Phase**:
        - Complex carbs and omega-3s are great for mood regulation.
        - Engage in low-intensity workouts, mindfulness, and stretching.
        """)

# Fitness & Exercise Page with deeper features
elif app_mode == "Fitness & Exercise":
    st.subheader("Log Your Fitness & Exercises 🏋️‍♂️")

    st.write("### Log Your Daily Workouts")
    exercise_type = st.text_input("Type of Exercise (e.g., Yoga, Running)")
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, step=1)
    calories_burned = st.number_input("Calories Burned", min_value=0, step=10)
    
    if st.button("Save Exercise"):
        st.success(f"Your {exercise_type} workout has been saved!")
        st.write(f"Duration: {duration} minutes, Calories Burned: {calories_burned} kcal")

    # Exercise Trend Graphs
    st.write("### View Exercise Trends")
    df = pd.DataFrame({
        "Date": [date.today()],
        "Calories Burned": [calories_burned],
        "Exercise Duration (min)": [duration]
    })
    st.line_chart(df.set
