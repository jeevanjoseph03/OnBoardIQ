# OnboardIQ - AI-Powered Onboarding Assistant

**OnboardIQ** is an intelligent multi-agent HR assistant that automates employee onboarding using IBM's Granite LLM and the watsonx.ai platform. The system converts a simple HR instruction into a comprehensive onboarding package including a personalized welcome email, IT setup request, and a structured checklist.

Built for the **IBM AI & Automation Hackathon - June 2025**, this project demonstrates the capabilities of agentic AI combined with enterprise-ready large language models.

---

## Features

OnboardIQ provides the following capabilities:

- **Automated Content Generation**: Leverages IBM's `granite-3-3-8b-instruct` model to generate contextually appropriate onboarding materials
- **Multi-Agent Architecture**: Employs three specialized AI agents working in coordination:
  - PlannerAgent: Extracts and structures key information from user instructions
  - EmailAgent: Generates personalized welcome and IT setup emails
  - ChecklistAgent: Creates role-specific task lists with appropriate deadlines
- **User-Friendly Interface**: Built with Streamlit for straightforward interaction
- **Comprehensive Output**: Generates all essential onboarding documents:
  - Personalized welcome email
  - IT setup request with relevant details
  - Role-specific checklist with realistic timelines
- **Simple Configuration**: Environment-based configuration for easy deployment

---

## Architecture

The system employs a multi-agent workflow to process onboarding requests:

```
User Input: "Onboard Alex as Software Engineer starting July 15th"
                              ↓
                    PlannerAgent extracts:
                    • Role: Software Engineer  
                    • Start date: July 15th
                              ↓
         ┌─────────────────────┬─────────────────────┐
         ↓                     ↓                     ↓
    EmailAgent            EmailAgent         ChecklistAgent
   (Welcome email)        (IT setup)         (Task list)
```

Each agent is specialized for its task, ensuring high-quality, contextually appropriate output.

---

## Installation

### Prerequisites
- Python 3.7 or higher
- IBM Cloud account with watsonx.ai access
- IBM API key and project ID

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/onboardiq.git
cd onboardiq
```

### Step 2: Configure Environment Variables
Create a `.env` file in the project root directory with the following configuration:

```env
IBM_API_KEY=your_ibm_cloud_api_key_here
PROJECT_ID=your_watsonx_project_id
MODEL_ID=ibm/granite-3-3-8b-instruct
ENDPOINT=https://us-south.ml.cloud.ibm.com
```

**Note**: Replace `your_ibm_cloud_api_key_here` and `your_watsonx_project_id` with your actual IBM Cloud API key and watsonx.ai project ID. You can obtain these from your IBM Cloud account.

**Important**: Do not commit the `.env` file to version control. It contains sensitive credentials.

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
streamlit run streamlit_app.py
```

The application will be accessible at `http://localhost:8501` in your web browser.

---

## Usage

### Input Format

The application requires two inputs:

1. **Employee Name**: The full name of the new hire
2. **Onboarding Instruction**: A natural language instruction describing the role and start date

### Example

**Input:**
- Name: `Jeevan George`
- Instruction: `Onboard as Sales Executive starting July 1st`

**Output:**

The system generates three artifacts:

1. **Welcome Email**: A personalized welcome message appropriate to the role
2. **IT Setup Request**: Detailed requirements for IT provisioning
3. **Onboarding Checklist**: A structured task list with deadlines

---

## Technology Stack

| Component | Technology |
|-----------|------------|
| Language Model | IBM Granite 3.3 8B Instruct |
| AI Platform | IBM watsonx.ai |
| Agent Framework | Custom multi-agent implementation |
| Web Framework | Streamlit |
| Configuration | Python-dotenv |
| HTTP Client | Requests |

---

## Project Structure

```
OnboardIQ/
├── agents/               # AI agent implementations
│   ├── planner_agent.py
│   ├── email_agent.py
│   └── checklist_agent.py
├── core/                 # Core functionality
│   └── watsonx_client.py
├── streamlit_app.py      # Main application entry point
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## License

This project was developed for the IBM AI & Automation Hackathon - June 2025.
