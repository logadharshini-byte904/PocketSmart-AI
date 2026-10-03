import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# API Key Config
API_KEY = os.getenv("AQ.Ab8RN6IP2eyzxaHLhoA97XBZHyGf-qYgFwU4_XOUkYyq2SS1Pg")
genai.configure(api_key=API_KEY)

# Page Setup
st.set_page_config(page_title="PocketSmart AI", page_icon="💰", layout="wide")
st.title("💰 PocketSmart AI: Your Smart Budget & Recommendation Assistant")

# Sidebar - Choice of Planner
planner_type = st.sidebar.selectbox(
    "Select Budget Planner",
    ["Home Interior Planner", "Party Budget Planner", "Jewelry Budget Planner"]
)

# 1. Home Interior Planner
if planner_type == "Home Interior Planner":
    st.header("🏠 Home Interior Budget Planner")
    total_budget = st.number_input("Total Budget (in ₹)", min_value=1000, value=50000)
    room_type = st.selectbox("Room Type", ["Living Room", "Kitchen", "Bedroom", "Full House"])
    items = st.text_input("Items Needed (e.g., Sofa, Lights, Dining Table, Fan)", "Sofa, Ceiling Fan, Dining Table")
    
    if st.button("Generate Home Budget Plan 🚀"):
        prompt = f"""
        Act as a Smart Interior Decorator and Budget Planner.
        Total Budget: ₹{total_budget}
        Room Type: {room_type}
        Required Items: {items}
        
        Provide a detailed allocation of budget, product recommendations (like IKEA, Amazon), and cost-saving tips.
        """
        with st.spinner("Analyzing budget & recommendations..."):
            try:
                model = genai.GenerativeModel('gemini-3.8-flash')
                response = model.generate_content(prompt)
                st.success("Your Home Interior Recommendation Plan is Ready!")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Error: {e}")

# 2. Party Budget Planner
elif planner_type == "Party Budget Planner":
    st.header("🎉 AI-Based Party Budget Planner")
    total_budget = st.number_input("Total Event Budget (in ₹)", min_value=1000, value=20000)
    event_type = st.selectbox("Event Type", ["Birthday Party", "Get-Together", "Corporate Event", "Wedding Ceremony"])
    guests = st.number_input("Number of Guests", min_value=1, value=25)
    
    if st.button("Generate Party Plan 🚀"):
        prompt = f"""
        Act as an Event Planner.
        Total Budget: ₹{total_budget}
        Event Type: {event_type}
        Guest Count: {guests}
        
        Allocate budget proportionally across Catering (Swiggy/Zomato), Decoration, Venue, and Entertainment with smart options.
        """
        with st.spinner("Calculating party plan..."):
            try:
                model = genai.GenerativeModel('gemini-3.8-flash')
                response = model.generate_content(prompt)
                st.success("Your Party Budget Plan is Ready!")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Error: {e}")

# 3. Jewelry Budget Planner
elif planner_type == "Jewelry Budget Planner":
    st.header("💎 Jewelry Budget Planner for Occasions")
    total_budget = st.number_input("Jewelry Budget (in ₹)", min_value=5000, value=100000)
    metal_pref = st.selectbox("Preference", ["Gold (22K/18K)", "Diamond", "Silver", "Fashion/Artificial"])
    occasion = st.selectbox("Occasion", ["Wedding", "Festival", "Daily Wear", "Gift"])
    
    if st.button("Generate Jewelry Recommendations 🚀"):
        prompt = f"""
        Act as a Jewelry Shopping Assistant.
        Budget: ₹{total_budget}
        Preference: {metal_pref}
        Occasion: {occasion}
        
        Suggest suitable jewelry options, estimated weights/types, and trusted platforms or styles within budget.
        """
        with st.spinner("Finding best jewelry options..."):
            try:
                model = genai.GenerativeModel('gemini-3.8-flash')
                response = model.generate_content(prompt)
                st.success("Your Jewelry Shopping Guide is Ready!")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Error: {e}")