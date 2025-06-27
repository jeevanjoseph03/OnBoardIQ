from core.watsonx_client import WatsonXClient
from agents.planner_agent import PlannerAgent
from agents.email_agent import EmailAgent
from agents.checklist_agent import ChecklistAgent

from core.watsonx_client import WatsonXClient

client = WatsonXClient()  



planner = PlannerAgent(client)
email_agent = EmailAgent(client)
checklist_agent = ChecklistAgent(client)


user_name = "Jeevan George"
user_instruction = "Onboard as Sales Executive starting July 1st"
plan = planner.plan(user_name, user_instruction)


emails = email_agent.generate_emails(plan["name"], plan["role"], plan["start_date"])
checklist = checklist_agent.generate_checklist(plan["name"], plan["role"], plan["start_date"])


print("\nEMAILS\n")
print(emails)

print("\nCHECKLIST\n")
print(checklist)
