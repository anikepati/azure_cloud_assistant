import schedule
import time
from agents.insights_agent import InsightsAgent
from agents.anomaly_detector import detect_anomaly
from utils.teams_notifier import notify_teams
from memory.vector_store import VectorStore
from genai_analyzer import GenAIAnalyzer

APP_ID = "<APP_INSIGHTS_ID>"
API_KEY = "<APP_INSIGHTS_API_KEY>"
TEAMS_WEBHOOK = "<TEAMS_WEBHOOK>"

vector_store = VectorStore()
llm_analyzer = GenAIAnalyzer()

previous_data = [100, 120, 110]

def job():
    insights = InsightsAgent(APP_ID, API_KEY)
    current_data = insights.get_metrics()
    current = current_data['value'][-1]['sum']

    # Store metrics in vector store
    text_doc = f"Metric: {current}"
    vector_store.add_document(str(time.time()), text_doc)

    # Check for anomaly
    if detect_anomaly(current, previous_data):
        # Use GenAI to explain the anomaly
        response = llm_analyzer.analyze("Explain why an anomaly occurred in application metrics")
        notify_teams(TEAMS_WEBHOOK, f"🚨 Anomaly Detected: {current}\nExplanation: {response}")

schedule.every(30).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)