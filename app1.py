import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, date

# CSS styling for improved visuals
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
        .stButton>button {
            background-color: #2196F3;
            color: white;
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# Set up the app title and description with emojis
st.title("🌱 **BiYourFusion Mobile Health App**")
st.write("Welcome to your personal health and wellness management app. Track your daily health insights, set goals, monitor your progress, and store your health records.")

# Sidebar for navigation with emojis and options
st.sidebar.title("🌐 Navigation")
app_mode = st.sidebar.selectbox("Choose a section", [
    "🏠 Home", "❓ Why BiYourFusion?", "📊 Log Health Metrics", "🌸 Log Menstrual Cycle", 
    "🏋️‍♂️ Fitness & Exercise", "📈 View Dashboard", "🎯 Set Goals", "📝 Health Records", "💉 Immunization Records", 
    "📜 Terms of Service and Privacy Policy"
])

# Date in Sidebar
st.sidebar.write("### 📅 Current Date")
st.sidebar.write(date.today())

# Home Page with tiles (showing quick health data)
if app_mode == "🏠 Home":
    st.subheader("Welcome to your Health Dashboard")
    st.write("Use this app to log daily health metrics and track your progress over time.")
    
    # Create a row of tiles for key metrics (dummy values for now)
    st.markdown(f"""
    <div class="tile">🚶 Steps Today: 5000</div>
    <div class="tile">💧 Water Intake: 60 oz</div>
    <div class="tile">💤 Sleep: 7 hrs</div>
    """, unsafe_allow_html=True)

# Log Health Metrics Page with icons and styles
elif app_mode == "📊 Log Health Metrics":
    st.subheader("Log Daily Health Metrics 🩺")
    
    steps = st.number_input("Steps Walked Today", min_value=0, max_value=50000, step=100)
    sleep = st.number_input("Hours of Sleep", min_value=0.0, max_value=24.0, step=0.5)
    water_intake = st.number_input("Water Intake (oz)", min_value=0, max_value=300, step=1)
    
    if st.button("Save Entry"):
        st.success("Health metrics logged successfully! 🎉")

# Log Menstrual Cycle Page with emojis and additional helpful info
elif app_mode == "🌸 Log Menstrual Cycle":
    st.subheader("Log Menstrual Cycle 🌸")
    
    # Cycle tracking inputs
    st.write("### Menstrual Cycle Details")
    cycle_start = st.date_input("Start Date")
    cycle_end = st.date_input("End Date", min_value=cycle_start)
    cycle_length = (cycle_end - cycle_start).days
    st.write(f"Cycle Length: {cycle_length} days")
    
    # Ovulation tracking
    st.write("### Ovulation Tracking")
    ovulation_date = st.date_input("Ovulation Date (estimated)", min_value=cycle_start, max_value=cycle_end)
    st.write(f"Estimated Ovulation Date: {ovulation_date}")
    
    # Save button
    if st.button("Save Cycle Data"):
        st.success("Menstrual cycle data logged successfully! 🎉")
        st.write("### Summary of Recorded Data")
        st.write(f"- Cycle Start Date: {cycle_start}")
        st.write(f"- Cycle End Date: {cycle_end}")
        st.write(f"- Cycle Length: {cycle_length} days")
        st.write(f"- Estimated Ovulation Date: {ovulation_date}")
    
    # Menstrual phase tips with a friendly tone
    st.write("### Tips for Each Phase of the Menstrual Cycle 🌸")
    phase = st.radio("Select a Cycle Phase to Learn More", [
        "Menstrual Phase", "Follicular Phase", "Ovulation Phase", "Luteal Phase"
    ])

    if phase == "Menstrual Phase":
        st.write("""
        **Tips during your period:**
        - **Foods to Indulge In:** Iron-rich foods (spinach, lentils), magnesium-rich foods (dark chocolate, nuts).
        - **Foods to Avoid:** Processed foods, caffeine, and alcohol.
        - **Exercises to Try:** Light yoga, walking, or stretching.
        - **Other Tips:** Use heating pads for cramps and prioritize hydration.
        """)
    elif phase == "Follicular Phase":
        st.write("""
        **Tips during the follicular phase:**
        - **Foods to Indulge In:** Protein-rich foods (eggs, chicken, fish), healthy fats (avocado, nuts).
        - **Foods to Avoid:** High-sugar snacks and refined carbs.
        - **Exercises to Try:** Cardio, weight training, or high-energy activities.
        - **Other Tips:** This is the best time to focus on productivity and creative projects.
        """)

    elif phase == "Ovulation Phase":
        st.write("""
        **Tips during ovulation:**
        - **Foods to Indulge In:** Antioxidant-rich foods (berries, leafy greens), hydration-focused foods (watermelon, cucumber).
        - **Foods to Avoid:** Inflammatory foods (fried or overly salty foods).
        - **Exercises to Try:** High-intensity interval training (HIIT), running, or dancing.
        - **Other Tips:** Socialize and take advantage of peak energy and confidence.
        """)

    elif phase == "Luteal Phase":
        st.write("""
        **Tips during the luteal phase:**
        - **Foods to Indulge In:** Complex carbs (sweet potatoes, quinoa), omega-3-rich foods (salmon, flaxseed).
        - **Foods to Avoid:** Excess sodium and caffeine to reduce bloating.
        - **Exercises to Try:** Pilates, moderate-intensity workouts, or swimming.
        - **Other Tips:** Manage mood changes by practicing mindfulness or journaling.
        """)

# Fitness & Exercise Page
elif app_mode == "🏋️‍♂️ Fitness & Exercise":
    st.subheader("Fitness & Exercise 🏋️‍♂️")

    # Section 1: Log Exercises
    st.write("### Log Your Exercises")
    exercise_type = st.text_input("Type of Exercise (e.g., running, yoga, weightlifting)")
    duration = st.number_input("Duration (minutes)", min_value=0, step=1)
    calories_burned = st.number_input("Estimated Calories Burned", min_value=0, step=1)

    if st.button("Save Exercise"):
        st.success("Exercise logged successfully!")
        st.write(f"**Exercise Type:** {exercise_type}")
        st.write(f"**Duration:** {duration} minutes")
        st.write(f"**Calories Burned:** {calories_burned}")

    # Section 2: Explore Trainer Tips
    st.write("### Trainer Tips & Free Resources")
    st.write("Access free workout videos and meditations:")
    st.video("https://www.youtube.com/watch?v=example_workout_video")  # Replace with real URLs
    st.video("https://www.youtube.com/watch?v=example_meditation_video")  # Replace with real URLs

    # Section 3: Activity Trends
    st.write("### Track Your Activity Trends")
    steps = st.slider("Steps Taken Today", 0, 20000, step=100)
    standing_time = st.slider("Standing Time (hours)", 0, 24, step=1)
    distance = st.slider("Distance Traveled (miles)", 0.0, 10.0, step=0.1)

    # Display trends
    st.write("### Activity Overview")
    st.bar_chart({"Steps": steps, "Standing Hours": standing_time, "Distance (miles)": distance})

    # Section 4: Custom Plans & Rewards
    st.write("### Personalized Activity Plans")
    custom_plan_name = st.text_input("Name Your Plan")
    weekly_goal = st.slider("Weekly Goal (hours)", 0, 20, step=1)
    st.write("Earn badges for achieving milestones and stay motivated!")

    if st.button("Create Plan"):
        st.success(f"Your plan '{custom_plan_name}' has been created!")
        st.write(f"**Weekly Goal:** {weekly_goal} hours")
        st.write("Keep pushing towards your goal and collect rewards!")

    # Section 5: Social Sharing
    st.write("### Share Your Progress")
    share_option = st.selectbox("Who would you like to share with?", ["Trainers", "Friends", "Both", "None"])
    if share_option != "None":
        st.write(f"Your progress will be shared with: {share_option}")
    st.button("Share Now", key="share_progress")


# View Dashboard Page with line chart
elif app_mode == "📈 View Dashboard":
    st.subheader("Health Dashboard 📊")
    st.write("View your health metrics over time.")
    
    # Sample data for health metrics
    df = pd.DataFrame({
        "Date": pd.date_range(start="2023-01-01", periods=10, freq="D"),
        "Steps": np.random.randint(1000, 10000, 10),
        "Sleep (hrs)": np.random.uniform(5, 9, 10),
        "Water Intake (oz)": np.random.randint(30, 100, 10),
        "Calories Consumed": np.random.randint(1500, 2500, 10),
    })
    
    # Display a line chart with Streamlit's built-in charting functions
    st.line_chart(df.set_index("Date")[["Steps", "Sleep (hrs)", "Water Intake (oz)"]])

# Set Goals Page with icons (continued)
elif app_mode == "🎯 Set Goals":
    st.subheader("Set Health Goals 🎯")
    current_weight = st.number_input("Current Weight (lbs)", min_value=50, max_value=500, step=1)
    ideal_weight = st.number_input("Ideal Weight (lbs)", min_value=50, max_value=500, step=1)
    height = st.number_input("Height (inches)", min_value=36, max_value=96, step=1)

    if st.button("Save Goals"):
        st.success("Your health goals have been saved successfully! 🎯")
        st.write(f"**Current Weight:** {current_weight} lbs")
        st.write(f"**Ideal Weight:** {ideal_weight} lbs")
        st.write(f"**Height:** {height} inches")

# Health Records Page with icons
elif app_mode == "📝 Health Records":
    st.subheader("Log Health Records 📋")
    conditions = st.text_area("Existing Health Conditions", placeholder="e.g., Diabetes, Hypertension")
    allergies = st.text_area("Known Allergies", placeholder="e.g., Pollen, Nuts")
    
    if st.button("Save Health Records"):
        st.success("Health records saved successfully! 📝")
        st.write(f"**Health Conditions:** {conditions}")
        st.write(f"**Allergies:** {allergies}")

# Immunization Records Page
elif app_mode == ""💉 Immunization Records":
    st.subheader("Store and View Immunization Records 💉")
    st.write("Keep a record of your immunizations for easy reference. You can log new immunizations and view your existing records.")

    # Input fields for logging immunizations
    st.write("### Add a New Immunization Record")
    vaccine_name = st.text_input("Vaccine Name", placeholder="e.g., Influenza, COVID-19")
    date_received = st.date_input("Date Received")
    provider_name = st.text_input("Healthcare Provider", placeholder="e.g., Clinic or Doctor's Name")
    additional_notes = st.text_area("Additional Notes (Optional)", placeholder="e.g., Any side effects or remarks")

    if st.button("Save Immunization Record"):
        st.success(f"Immunization record for {vaccine_name} saved successfully!")

    # Example of displaying stored records (you would replace this with actual data retrieval logic)
    st.write("### Your Immunization Records")
    sample_records = pd.DataFrame({
        "Vaccine Name": ["Influenza", "COVID-19 Booster"],
        "Date Received": ["2023-10-10", "2024-01-15"],
        "Healthcare Provider": ["City Health Clinic", "County Hospital"],
        "Notes": ["No side effects", "Mild fever after injection"]
    })
    st.table(sample_records)

# Terms of Service and Privacy Policy Page with emoji
elif app_mode == "📜 Terms of Service and Privacy Policy":
    st.subheader("Terms of Service and Privacy Policy 📜")
    st.write("""
    **Privacy Policy:**
    - Your health data is confidential and not shared without your consent.
    - You can delete your account at any time, and your data will be permanently removed.

    **Terms of Service:**
    - By using this app, you agree to our terms and conditions.
    - We are not responsible for any medical advice, diagnosis, or treatment.
    """)

# Add a footer with friendly reminder
st.markdown("""
    <div style="text-align:center; padding: 20px; font-size: 14px;">
        🌱 **BiYourFusion** - A holistic approach to health management! Stay healthy, stay happy! 😊
    </div>
""", unsafe_allow_html=True)
