import streamlit as st

primaryColor = "#4ba3c7"
backgroundColor = "#eaf6fb"
secondaryBackgroundColor = "#cce8f0"
textColor = "#002f4f"
font = "sans serif"

# Set up page title and layout
st.set_page_config(page_title="Health and Wellness App", page_icon="🌱", layout="wide")

# Sidebar navigation with emojis and title
st.sidebar.title("🌟 Navigation")
tabs = st.sidebar.radio("Select a Tab:", ["🥗 Diet", "🏋️ Exercise", "🧘 Wellness", "💖 Health"])

# Moving graphic (replace with an actual GIF file path or URL)
moving_graphic_url = "https://www.google.com/search?sca_esv=639d025745a98286&q=fitness+gifs&udm=2&fbs=AEQNm0Aa4sjWe7Rqy32pFwRj0UkWd8nbOJfsBGGB5IQQO6L3JyWp6w6_rxLPe8F8fpm5a57iruiBaetC-P1z8A1EgSEtGoKiI-tyuuiDuAjQZN76zQqJViCdF78ZMNlQqovfNwuIqqo1RsVD9GtUqCzkz0DVUQ4z-CimdBJ3tn6agrsB0C0fnR33H6lfurv4ZfC2xlrkF2CyxrCbQL4FaLHuYaKtlILmFg&sa=X&ved=2ahUKEwjO2NXhkNeJAxXFEFkFHXe9I0MQtKgLegQIFBAB&biw=1199&bih=828&dpr=2#vhid=6YrhF2FB9Dic5M&vssid=mosaic"  # Example GIF URL
st.sidebar.image(moving_graphic_url, caption="Stay Active!", use_column_width=True)

# Diet Tab
if tabs == "🥗 Diet":
    st.title("🥗 Diet Tracker")
    
    # Moving graphic for Diet section
    st.image(moving_graphic_url, width=200)
    
    # Subsections with emojis and fields
    st.header("🎯 Diet Goals")
    st.text_input("Enter your diet goals", key="diet_goals")
    
    st.header("🍏 Calorie Counting")
    st.number_input("Daily Calorie Goal", min_value=0, step=50, key="calorie_goal")
    
    st.header("📋 Meal Ideas")
    st.text_area("Add meal ideas or recipes", key="meal_ideas")
    
    # Additional diet features
    st.header("⚙️ Additional Features")
    st.checkbox("Track macros")
    st.checkbox("Track hydration")

# Exercise Tab
elif tabs == "🏋️ Exercise":
    st.title("🏋️ Exercise Tracker")
    
    # Moving graphic for Exercise section
    st.image(moving_graphic_url, width=200)
    
    # Subsections with emojis and fields
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
    
    # Moving graphic for Wellness section
    st.image(moving_graphic_url, width=200)
    
    # Subsections with emojis and fields
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
    
    # Moving graphic for Health section
    st.image(moving_graphic_url, width=200)
    
    # Subsections with emojis and fields
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

# Footer section
st.sidebar.write("Health and Wellness App © 2024")

