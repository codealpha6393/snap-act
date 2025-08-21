from portia.execution_hooks import ExecutionHooks

class SafetyHooks(ExecutionHooks):
    def before_tool_call(self, ctx):
        tool = (ctx.tool_name or "").lower()
        inputs = ctx.inputs or {}
        preview = {
            "action": "pause",
            "clarification": {
                "title": "Preview action",
                "message": f"About to run: {tool} with {inputs}. Proceed?",
                "options": ["Approve", "Reject"],
            },
        }
        if tool.startswith("gmail."):
            to = (inputs.get("to") or "")
            domain = to.split("@")[-1] if to else ""
            allowlist = {"gmail.com", "example.com"}
            if domain not in allowlist:
                preview["clarification"]["title"] = "Email outside allowlist"
                preview["clarification"]["message"] += f"\nRecipient: {to}"
        return preview
