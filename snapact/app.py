import io
import streamlit as st
from dotenv import load_dotenv
from PIL import Image
import pytesseract
from portia import Config, Portia, DefaultToolRegistry
from hooks import SafetyHooks

import os
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
PORTIA_API_KEY = os.environ.get("PORTIA_API_KEY")

load_dotenv(override=True)
config = Config.from_default()
portia = Portia(config=config, tools=DefaultToolRegistry(config=config), execution_hooks=SafetyHooks())

st.set_page_config(page_title="Snap→Act", layout="wide")
st.title("📸 Snap→Act — Screenshot/Text → Actions")

mode = st.radio("Input mode", ["Text", "Image (OCR)"])

text_input = ""
if mode == "Text":
    text_input = st.text_area(
        "Paste text from screenshot or message",
        height=160,
        value="INVITE: Hackathon kickoff on 21 Aug, 10:00 AM, Zoom. Reply to dev@org.com"
    )
else:
    file = st.file_uploader("Upload screenshot (PNG/JPG)", type=["png", "jpg", "jpeg"])
    if file:
        image = Image.open(io.BytesIO(file.read()))
        st.image(image, caption="Uploaded screenshot", use_column_width=True)
        with st.spinner("Running OCR..."):
            text_input = pytesseract.image_to_string(image)
        st.text_area("Extracted text", value=text_input, height=160)

col1, col2 = st.columns(2)
with col1:
    run_plan = st.button("Propose Plan")
with col2:
    st.markdown("Actions will pause for approval via Portia clarifications.")

if run_plan and text_input.strip():
    task = f"""
    You are Snap→Act. Parse the input and identify type: invite | bill | tasklist | receipt | other.
    Propose a short, safe plan with steps and clarifications. Do not run tools yet.
    For invites: create Google Calendar event; draft a polite Gmail reply to sender.
    For bills: add a calendar reminder; log to Sheet (date, amount, vendor) if available; draft acknowledgement.
    For tasklist: create tasks in Notion or a Google Sheet; schedule follow ups.
    For receipts: save to Drive under /SnapAct/Receipts/YYYY/MM and log to Sheet.
    Always present a clear plan + specific clarifications for any assumptions.
    Input:\n{text_input}
    """
    plan = portia.run(task)
    st.subheader("Proposed Plan")
    st.code(str(plan))
