# Snap→Act — AI that turns screenshots into instant actions

**One-liner**  
Snap→Act transforms your screenshot into real actions: extract info, propose a plan, approve, and let Portia execute (like adding events, drafting emails, reminders).

---

##  Problem  
Important tasks—like event invites, invoices, and to-do notes—often live in screenshots. Copying details manually wastes time.

---

##  Solution  
1. Upload a screenshot or paste text  
2. OCR → extract actionable items  
3. Portia plans tasks with clarifications (safe-by-design)  
4. You approve → tasks execute in Calendar, Gmail, Drive, etc.

---

##  Demo  
1. Drag-and-drop a screenshot of an event or bill.  
2. Click *Propose Plan*.  
3. Review the plan, approve it.  
4. Actions play out (e.g., new Calendar event, draft email).  
*(Add a GIF or screenshots here later!)*

---

##  Tech Stack  
- **Portia SDK** — structured planning + safe execution  
- **Streamlit** — quick UI  
- **Tesseract OCR** — image to text  
- Google APIs (Calendar, Gmail, Drive)

---

##  Setup & Run (Cloud or Local)  
### Local:
```bash
git clone https://github.com/codealpha6393/snap-act.git
cd snap-act

pip install -r requirements.txt

