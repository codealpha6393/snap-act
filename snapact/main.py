from dotenv import load_dotenv
from portia_sdk import Config, Portia, DefaultToolRegistry
from hooks import SafetyHooks

load_dotenv(override=True)
config = Config.from_default()
portia = Portia(config=config, tools=DefaultToolRegistry(config=config), execution_hooks=SafetyHooks())

raw = "INVITE: AI Meetup on 22 Aug, 4:30–6:00 PM, Room 204. Reply to alice@example.com"

task = f"""
You are Snap→Act. Parse the input and identify type: invite | bill | tasklist | receipt | other.
Propose a short, safe plan with steps and clarifications.
Input:\n{raw}
"""
print(portia.run(task))
