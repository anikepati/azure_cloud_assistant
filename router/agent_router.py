from openai import OpenAI
from agents.iam_agent import IAMAgent
from agents.insights_agent import InsightsAgent
from utils.function_schema import function_schema
import os

class AgentRouter:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = "gpt-4-0613"

    def route(self, user_input: str):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": user_input}],
            functions=function_schema,
            function_call="auto",
        )

        message = response.choices[0].message

        if message.get("function_call"):
            func_name = message.function_call.name
            args = message.function_call.arguments
            # Safely parse JSON string arguments
            import json
            params = json.loads(args)

            if func_name == "assign_iam_role":
                iam_agent = IAMAgent()
                return iam_agent.assign_role(**params)

            elif func_name == "check_app_insights":
                insights_agent = InsightsAgent(
                    app_id=params["app_id"], api_key=params["api_key"]
                )
                return insights_agent.get_metrics()

        return "Sorry, I couldn't understand your request."
