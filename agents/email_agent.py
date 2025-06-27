class EmailAgent:
    def __init__(self, client):
        self.client = client

    def generate_emails(self, name, role, start_date):
        prompt = f"""
You are an HR assistant.

Generate two emails based on the info:
Name: {name}
Role: {role}
Start Date: {start_date}

1. Welcome Email
2. IT Email Request
Format as:
Welcome Email:
[text]
IT Email:
[text]
"""
        return self.client.generate(prompt)
