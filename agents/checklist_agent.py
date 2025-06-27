class ChecklistAgent:
    def __init__(self, client):
        self.client = client

    def generate_checklist(self, name, role, start_date):
        prompt = f"""
Generate an onboarding checklist for a new hire.

Name: {name}
Role: {role}
Start Date: {start_date}

List at least 5 tasks with deadlines.
Format:
- [Task] - [Due Date]
"""
        return self.client.generate(prompt)
