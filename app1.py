import streamlit as st
from datetime import date

# Set up page configuration
st.set_page_config(page_title="BiYourFusion Health App", page_icon="🌱", layout="wide")

# Define Color Palette
primaryColor = "#4CAF50"  # Green for primary elements (buttons, active elements)
secondaryColor = "#FFEB3B"  # Yellow for highlights and accents
backgroundColor = "#FFFFFF"  # White background
textColor = "#2C6B2F"  # Dark Green text for contrast and readability
accentColor = "#388E3C"  # Slightly darker green for some accents
buttonColor = "#FFEB3B"  # Yellow for buttons

# Custom CSS for styling
st.markdown(f"""
    <style>
        .main {{
            background-color: {backgroundColor};
            color: {textColor};
        }}
        .sidebar .sidebar-content {{
            background-color: {secondaryColor};
            color: {textColor};
        }}
        .icon {{
            font-size: 2em;
            color: {primaryColor};
            margin-right: 10px;
        }}
        .tile {{
            background-color: {accentColor};
            border-radius: 10px;
            padding: 20px;
            margin: 10px 0;
            color: #fff;
            text-align: center;
            font-weight: bold;
        }}
        .stButton {{
            background-color: {buttonColor};
            color: {textColor};
            border-radius: 5px;
            padding: 10px;
            font-weight: bold;
        }}
        .stTextInput, .stNumberInput, .stSelectbox, .stTextArea {{
            background-color: #f7f7f7;
            color: {textColor};
        }}
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("🌐 Navigation")
tabs = st.sidebar.radio("Select a Tab:", [
    "🥗 Diet", "🏋️ Exercise", "🧘 Wellness", "💖 Health", "Log Health Metrics", "Log Menstrual Cycle", 
    "Fitness & Exercise", "View Dashboard", "Set Goals", "Health Records", "Immunization Records", "Terms of Service and Privacy Policy"
])

# Date in Sidebar
st.sidebar.write("### 📅 Current Date")
st.sidebar.write(date.today())

# App Title and Description
st.title("🌱 BiYourFusion Health App")
st.write("""
    Welcome to your all-in-one health and wellness platform. Track your health metrics, set goals, log your exercise, manage your menstrual cycle, and access health records – all in one place.
""")

# Combine content based on selected tab

# Diet Tab
if tabs == "🥗 Diet":
    st.title("🥗 Diet Tracker")
    st.image("https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjR0MXdiN3dnb2R0b2Rxb3Azdnhjb2pxeXd1amkxNmo1YTY1MTQ5ciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Pu4gYo3wjgnucHTpM7/giphy.gif", width=200)
    
    st.header("🎯 Diet Goals")
    st.text_input("Enter your diet goals", key="diet_goals")
    
    st.header("🍏 Calorie Counting")
    st.number_input("Daily Calorie Goal", min_value=0, step=50, key="calorie_goal")
    
    st.header("📋 Meal Ideas")
    st.text_area("Add meal ideas or recipes", key="meal_ideas")
    
    st.header("⚙️ Additional Features")
    st.checkbox("Track macros")
    st.checkbox("Track hydration")

# Exercise Tab
elif tabs == "🏋️ Exercise":
    st.title("🏋️ Exercise Tracker")
    st.image("https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjR0MXdiN3dnb2R0b2Rxb3Azdnhjb2pxeXd1amkxNmo1YTY1MTQ5ciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Pu4gYo3wjgnucHTpM7/giphy.gif", width=200)
    
    st.header("🎯 Workout Goals")
    st.text_input("Enter your workout goals", key="workout_goals")
    
    st.header("🔥 Calories Burned")
    st.number_input("Enter calories burned per workout", min_value=0, step=10, key="calories_burned")
    
    st.header("💪 Workout Examples")
    st.selectbox("Select a workout type", ["Running", "Cycling", "Weightlifting", "Yoga"])
    
    st.header("📈 Exercise Tracking")
    st.number_input("Miles Ran", min_value=0.0, step=0.1, key="miles_ran")

# Wellness Tab
elif tabs == "🧘 Wellness":
    st.title("🧘 Wellness Hub")
    st.image("https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjR0MXdiN3dnb2R0b2Rxb3Azdnhjb2pxeXd1amkxNmo1YTY1MTQ5ciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Pu4gYo3wjgnucHTpM7/giphy.gif", width=200)
    
    st.header("🧠 Mental Health")
    st.text_area("Write down your thoughts")
    
    st.header("💌 Positive Messages of Encouragement")
    st.text("Remember: Progress is progress, no matter how small!")
    
    st.header("🌬️ Breathing Relaxation")
    if st.button("Start Breathing Exercise"):
        st.write("Breathe in... Breathe out...")

# Health Tab
elif tabs == "💖 Health":
    st.title("💖 Health Overview")
    st.image("https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjR0MXdiN3dnb2R0b2Rxb3Azdnhjb2pxeXd1amkxNmo1YTY1MTQ5ciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Pu4gYo3wjgnucHTpM7/giphy.gif", width=200)
    
    st.header("📄 Import Health Records")
    st.file_uploader("Upload health record file", type=["pdf", "txt", "csv"])
    
    st.header("🚫 Allergies and Dietary Restrictions")
    st.text_input("List any allergies or dietary restrictions", key="allergies")
    
    st.header("🩺 Conditions")
    st.text_input("Enter any health conditions to adjust diet and exercise")
    
    st.header("📅 Period Tracker")
    st.date_input("Last menstrual period start date")
    
    st.header("📈 Personal Health Tracking")
    st.text_input("Track personal health matters")

# Log Health Metrics
elif tabs == "Log Health Metrics":
    st.subheader("Log Daily Health Metrics 🩺")
    
    steps = st.number_input("Steps Walked Today", min_value=0, max_value=50000, step=100)
    sleep = st.number_input("Hours of Sleep", min_value=0.0, max_value=24.0, step=0.5)
    water_intake = st.number_input("Water Intake (oz)", min_value=0, max_value=300, step=1)
    
    if st.button("Save Entry", key="log_metrics"):
        st.success("Health metrics logged successfully!", icon="✅")

# Log Menstrual Cycle
# Log Menstrual Cycle
elif tabs == "Log Menstrual Cycle":
    st.subheader("Log Menstrual Cycle 🌸")
    cycle_start = st.date_input("Start Date")
    cycle_end = st.date_input("End Date", min_value=cycle_start)
    cycle_length = (cycle_end - cycle_start).days
    st.write(f"Cycle Length: {cycle_length} days")

    ovulation_date = st.date_input("Ovulation Date (estimated)", min_value=cycle_start, max_value=cycle_end)
    st.write(f"Estimated Ovulation Date: {ovulation_date}")

    contraceptive_type = st.selectbox("Select Contraceptive Method", [
        "None", "Birth Control Pill", "IUD", "Condom", "Natural Rhythm Method", "Other"
    ])
    contraceptive_notes = st.text_area("Additional Notes on Contraceptive Use (if any)")
    
    # Fixing the incomplete st.button() statement
    if st.button("Save Cycle Data", key="log_cycle"):
        st.success("Cycle data saved successfully!", icon="✅")

