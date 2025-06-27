#  OnboardIQ - Your Smart Onboarding Buddy

Ever spent hours crafting welcome emails and onboarding checklists for new hires? Yeah, me too. That's why I built **OnboardIQ** — an AI assistant that does all the tedious onboarding stuff so you don't have to.

Just tell it "Onboard Sarah as a Marketing Manager starting Monday" and boom — you get a personalized welcome email, IT setup request, and a complete checklist. All powered by IBM's Granite AI model.

I'm entering this in the **IBM AI & Automation Hackathon (June 2025)** because, honestly, onboarding shouldn't be this painful in 2025. OnboardIQ - AI-Powered Onboarding Assistant

**OnboardIQ** is an intelligent multi-agent HR assistant that automates employee onboarding using IBM’s Granite LLM and watsonx.ai platform. It converts a simple HR instruction into a personalized welcome email, IT setup request, and a structured checklist — instantly.

Built for the **IBM AI & Automation Hackathon - June 2025**, it showcases the power of **agentic AI** combined with enterprise-ready LLMs.

---

## 🚀 What it actually does

- Uses IBM's `granite-3-3-8b-instruct` model (because it's surprisingly good)
- Three AI agents work together: one plans, one writes emails, one makes checklists
- Clean Streamlit interface (no fancy CSS needed)
- Generates everything you need:
  - A proper welcome email that doesn't sound robotic
  - IT setup email with actual details
  - Role-specific checklist with realistic deadlines
- Simple `.env` setup — no wrestling with IBM tokens
- Actually works (tested it myself multiple times)

---

## 🤖 How it works

Here's the magic behind the scenes:

```
You type: "Onboard Alex as Software Engineer starting July 15th"
                              ↓
                    PlannerAgent figures out:
                    • Role: Software Engineer  
                    • Start date: July 15th
                              ↓
         ┌─────────────────────┬─────────────────────┐
         ↓                     ↓                     ↓
    EmailAgent            EmailAgent         ChecklistAgent
   (Welcome email)        (IT setup)         (Task list)
```

Three agents, one goal: make onboarding easier.

---

## 🛠️ Getting it running

### Step 1: Grab the code
```bash
git clone https://github.com/yourusername/onboardiq.git
cd onboardiq
```

### Step 2: Set up your secrets
Create a `.env` file in the main folder:
```env
IBM_API_KEY=your_ibm_cloud_api_key_here
PROJECT_ID=a9338afa-9c99-4030-80fd-a7b3ff20bbc7
MODEL_ID=ibm/granite-3-3-8b-instruct
ENDPOINT=https://us-south.ml.cloud.ibm.com
```
*(Obviously don't commit this to GitHub — learned that the hard way)*

### Step 3: Install the stuff
```bash
pip install -r requirements.txt
```

### Step 4: Fire it up
```bash
streamlit run streamlit_app.py
```

## 🖥 See it in action

**What you type:**
> Name: Jeevan George  
> Instruction: Onboard as Sales Executive starting July 1st

**What you get:**
- A warm welcome email (not the usual corporate template)
- Detailed IT setup request 
- Complete checklist with realistic deadlines

## 📦 What's under the hood

| Thing | What I used |
|-------|-------------|
| Brain | IBM Granite 3.3 8B Instruct |
| API | WatsonX (with auto token handling) |
| Agents | Custom multi-agent setup |
| Frontend | Streamlit (keeps it simple) |
| Config | `.env` file |

---

*Built during a weekend because manual onboarding is soul-crushing. If this helps even one HR person save an hour, it was worth it.*