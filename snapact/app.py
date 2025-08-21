import os
from dotenv import load_dotenv
import streamlit as st
from portia import Portia

# =============================
# 🔑 Load API Keys (Hybrid Setup)
# =============================
load_dotenv()  # Loads .env file locally (ignored on GitHub if secrets are set)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PORTIA_API_KEY = os.getenv("PORTIA_API_KEY")

if not OPENAI_API_KEY or not PORTIA_API_KEY:
    raise ValueError("❌ API keys missing! Please set them in .env or GitHub Secrets.")

# =============================
# 🤖 Initialize Portia
# =============================
portia = Portia(
    api_key=PORTIA_API_KEY,
    model="gpt-4o-mini",   # you can change to "gpt-4.1-mini" or others
    openai_api_key=OPENAI_API_KEY
)

# =============================
# 🎯 Streamlit UI
# =============================
st.set_page_config(page_title="SnapAct - AI Action Planner", page_icon="🤖")

st.title("🤖 SnapAct - AI Powered Action Planner")
st.markdown("Turn your **natural language ideas** into an **action plan with steps!**")

# Input from user
task = st.text_area("📝 What do you want to do?", placeholder="e.g. Plan a weekend trip to Goa")

if st.button("✨ Generate Action Plan"):
    if task.strip() == "":
        st.warning("⚠️ Please enter a task first.")
    else:
        try:
            with st.spinner("🔮 Thinking..."):
                plan = portia.run(task)

            st.success("✅ Here’s your AI-generated action plan:")
            st.write(plan)

        except Exception as e:
            st.error(f"❌ Oops! Something went wrong: {e}")
