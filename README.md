# azure_cloud_assistant
Autonomous Azure Cloud Assistant (Python, Streamlit, OpenAI Function Calling, ChromaDB, Azure RBAC + App Insights)

# 🚀 CloudCopilot – Azure IAM & App Insights Assistant

CloudCopilot is an agentic GenAI assistant that automates Azure Identity & Access tasks and analyzes Application Insights metrics. It uses OpenAI Function Calling to route user questions to intelligent agents.

---

## 🧩 Features

- 🔐 Azure IAM agent to assign/revoke roles between users/apps.
- 📊 Application Insights agent to detect anomalies and metric drops.
- 🧠 RAG-based memory (ChromaDB) for contextual Q&A.
- 🧠 OpenAI Function Calling for robust agent routing.
- 💬 Streamlit UI with full question-response chat history.

---

## ⚙️ Quick Setup (using [`uv`](https://github.com/astral-sh/uv))

```bash


# 1. Create virtualenv & install dependencies
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -r requirements.txt

# 2. Copy and update .env file
cp .env.example .env
# Fill in the following in .env:
# OPENAI_API_KEY=
# AZURE_CLIENT_ID=
# AZURE_TENANT_ID=
# AZURE_CLIENT_SECRET=
# AZURE_SUBSCRIPTION_ID=
# APP_INSIGHTS_APP_ID=
# APP_INSIGHTS_API_KEY=

# 3. Launch the app
streamlit run app.py

```
## ⚙️ Example queries
• "Assign Reader role from user1 to user2"
• "Is the application slower since last deployment?"

## 📂 Folder Structure
.
├── app.py                   # Streamlit UI
├── .env                     # environment variables
├── agents/
│   ├── iam_agent.py
│   └── insights_agent.py
├── core/
│   ├── agent_router.py
│   └── rag_memory.py
├── utils/
│   └── function_schema.py
├── requirements.txt
└── README.md
