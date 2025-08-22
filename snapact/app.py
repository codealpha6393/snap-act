import os
import streamlit as st
from groq import Groq

# Load API Key
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    st.error("❌ No GROQ_API_KEY found. Please set it in GitHub Secrets or .env file.")
    st.stop()

# Initialize Groq client
client = Groq(api_key=groq_api_key)

# Streamlit App UI
st.set_page_config(page_title="Snap Act", layout="centered")

st.title("📸 Snap Act")
st.write("Generate **instant action plans** from any situation using AI 🚀")

user_input = st.text_area("Describe your situation:", placeholder="e.g., I missed my project deadline...")

if st.button("Generate Action Plan"):
    if not user_input.strip():
        st.warning("⚠️ Please enter a situation before generating a plan.")
    else:
        with st.spinner("Thinking..."):
            try:
                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",  # Free + fast model
                    messages=[
                        {"role": "system", "content": "You are SnapAct AI. Provide step-by-step action plans that are clear and easy to follow."},
                        {"role": "user", "content": user_input}
                    ],
                    max_tokens=300
                )

                plan = response.choices[0].message.content
                st.subheader("✅ Your Action Plan")
                st.write(plan)

            except Exception as e:
                st.error(f"❌ Error: {e}")
