
import requests

class InsightsAgent:
    def __init__(self, app_id, api_key):
        self.app_id = app_id
        self.api_key = api_key

    def get_metrics(self):
        url = f"https://api.applicationinsights.io/v1/apps/{self.app_id}/metrics/requests/count"
        headers = {"x-api-key": self.api_key}
        response = requests.get(url, headers=headers)
        return response.json()