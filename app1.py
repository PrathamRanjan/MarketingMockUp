import streamlit as st

# Function to load and inject CSS for styling
def load_css():
    css = """
    <style>
    body {
        background-color: #f0fff0; /* A light green background */
        color: #ffffff; /* White text */
    }

    h1, h2, h3 {
        color: #ffffff; /* White for headers */
    }

    .stButton>button {
        border: 2px solid #ffffff;
        color: #004d00;
        background-color: #f0fff0;
        border-radius: 20px; /* Rounded corners for buttons */
        font-size: 16px;
    }

    .stButton>button:hover {
        border: 2px solid #ffffff;
        color: #f0fff0;
        background-color: #004d00;
    }

    .css-18e3th9, .css-1d391kg, .st-cx {
        background-color: #f0fff0;
        color: #ffffff;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

load_css()  # Call it at the start of your app

# Initialize the page state if not already set
if 'page' not in st.session_state:
    st.session_state.page = "home"

def set_page(page):
    st.session_state.page = page

# Home page layout
if st.session_state.page == "home":
    st.title("SaladCraft.AI")
    st.write("Good Afternoon Mr. Ooi, how can I help you today?")
    
    col1, col2 = st.columns(2)
    with col1:
        st.button("Salad Menu", on_click=set_page, args=("salad_menu",))
    with col2:
        st.button("Maintenance Menu", on_click=set_page, args=("maintenance_menu",))

# Salad Menu page layout
elif st.session_state.page == "salad_menu":
    st.title("Salad Menu")
    st.write("You have eaten 5 salads so far.")
    st.button("Salad Recommender")  # Implement feature or navigation as needed
    st.button("Salad Customiser")  # Implement feature or navigation as needed
    st.button("Salad Games")  # Implement feature or navigation as needed
    st.button("Return to Home", on_click=set_page, args=("home",))

# Maintenance Menu page layout
elif st.session_state.page == "maintenance_menu":
    st.title("Maintenance Menu")
    st.warning("The tomatoes need to be replaced by tomorrow morning!")
    st.button("Employee Salad Tracking")  # Implement feature or navigation as needed
    st.button("Supply Tracking")  # Implement feature or navigation as needed
    st.button("Duration of Food")  # Implement feature or navigation as needed
    st.button("Return to Home", on_click=set_page, args=("home",))
