# OnboardIQ: AI-Powered Onboarding Assistant

**OnboardIQ** is an intelligent multi-agent HR assistant that automates employee onboarding using IBM's Granite LLM and the watsonx.ai platform. The system transforms simple HR instructions into comprehensive onboarding packages, including personalized welcome emails, IT setup requests, and structured checklists.

Developed for the **IBM AI & Automation Hackathon - June 2025**, this project demonstrates the capabilities of agentic AI combined with enterprise-ready large language models to streamline and enhance the employee onboarding process.

---

## Key Features

- Utilizes IBM's `granite-3-3-8b-instruct` model for natural language processing
- Multi-agent architecture with specialized agents for planning, email composition, and checklist generation
- Streamlit-based user interface for easy interaction
- Automated generation of onboarding materials:
  - Personalized welcome emails
  - IT setup request emails with relevant technical details
  - Role-specific checklists with appropriate timelines
- Environment-based configuration using `.env` files for secure credential management
- Integration with IBM watsonx.ai platform

---

## Architecture

The system employs a coordinated multi-agent approach to process onboarding requests:

```
User Input: "Onboard Alex as Software Engineer starting July 15th"
                              ↓
                    PlannerAgent analyzes:
                    • Role: Software Engineer  
                    • Start date: July 15th
                              ↓
         ┌─────────────────────┬─────────────────────┐
         ↓                     ↓                     ↓
    EmailAgent            EmailAgent         ChecklistAgent
   (Welcome email)        (IT setup)         (Task list)
```

The three specialized agents work in coordination to ensure comprehensive onboarding coverage.

---

## Installation and Setup

### Clone the Repository
```bash
git clone https://github.com/yourusername/onboardiq.git
cd onboardiq
```

### Configure Environment Variables
Create a `.env` file in the project root directory with the following configuration:
```env
IBM_API_KEY=your_ibm_cloud_api_key_here
PROJECT_ID=your_project_id_here
MODEL_ID=ibm/granite-3-3-8b-instruct
ENDPOINT=https://us-south.ml.cloud.ibm.com
```
**Note:** Ensure the `.env` file is included in `.gitignore` to prevent credential exposure.

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the Application
```bash
streamlit run streamlit_app.py
```

## Usage

**Example Input:**
> Name: Jeevan George  
> Instruction: Onboard as Sales Executive starting July 1st

**Generated Output:**
- Personalized welcome email with role-specific content
- Comprehensive IT setup request email
- Structured onboarding checklist with milestone dates

## Technical Stack

| Component | Technology |
|-----------|------------|
| Language Model | IBM Granite 3.3 8B Instruct |
| AI Platform | IBM watsonx.ai |
| Architecture | Multi-agent system |
| User Interface | Streamlit |
| Configuration | Environment variables (.env) |

---
