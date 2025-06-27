import json
import re

class PlannerAgent:
    def __init__(self, client):
        self.client = client

    def plan(self, user_name, instruction):
        prompt = f"""
From the following instruction, extract only the job role and start date. The person's name is already provided.

Instruction: "{instruction}"

Respond ONLY in this JSON format:
{{
  "role": "Job Role",
  "start_date": "Start Date"
}}
"""

        response = self.client.generate(prompt)

        # Extract JSON block
        matches = re.findall(r'\{[\s\S]*?\}', response.strip())
        if matches:
            try:
                parsed = json.loads(matches[-1])
                return {
                    "name": user_name,
                    "role": parsed.get("role", "Unknown"),
                    "start_date": parsed.get("start_date", "Unknown")
                }
            except Exception as e:
                print("Failed to parse JSON:", e)

        print("Fallback triggered. Raw response:\n", response)
        return {
            "name": user_name,
            "role": "Unknown",
            "start_date": "Unknown"
        }
