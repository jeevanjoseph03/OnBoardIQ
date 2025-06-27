import streamlit as st
from agents.planner_agent import PlannerAgent
from agents.email_agent import EmailAgent
from agents.checklist_agent import ChecklistAgent
from core.watsonx_client import WatsonXClient

ACCESS_TOKEN = ...
PROJECT_ID = ...
MODEL_ID = ...
ENDPOINT = ...

client = WatsonXClient()


planner = PlannerAgent(client)
email_agent = EmailAgent(client)
checklist_agent = ChecklistAgent(client)

st.set_page_config(page_title="OnboardIQ", layout="centered")
st.title("OnboardIQ - AI Onboarding Assistant")

name = st.text_input("👤 Applicant's Name", value="Jeevan George")
instruction = st.text_area("📝 Onboarding Instruction ", 
                           value="Onboard as Sales Executive starting July 1st")


if st.button("Generate Workflow"):
    if not name.strip() or not instruction.strip():
        st.warning("Please fill in both the name and instruction.")
    else:
        with st.spinner("Thinking with Granite..."):
            plan = planner.plan(name, instruction)

            emails = email_agent.generate_emails(plan["name"], plan["role"], plan["start_date"])
            checklist = checklist_agent.generate_checklist(plan["name"], plan["role"], plan["start_date"])

    
        st.subheader("Generated Emails")
        st.text_area("Welcome + IT Email", emails, height=250)

        st.subheader("Onboarding Checklist")
        st.text_area("Checklist", checklist, height=200)
