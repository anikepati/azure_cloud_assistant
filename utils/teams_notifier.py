import requests

def notify_teams(webhook_url, message):
    payload = {"text": message}
    requests.post(webhook_url, json=payload)