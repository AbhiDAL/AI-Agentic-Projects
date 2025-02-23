📌 AI Research Assistant
🔍 An AI-powered research assistant that searches for information, summarizes key points, and provides intelligent responses using LLMs.

📖 Overview
The AI Research Assistant is an intelligent multi-agent system designed to:

Search the web for relevant information (DuckDuckGo API).
Summarize the retrieved data using Hugging Face’s Pegasus Model.
Store and retrieve data efficiently in ChromaDB.
Generate structured responses using OpenAI’s GPT-4o.

🏗️ Project Structure

📂 AI-Agentic-Projects
│── agentic_env/          # Virtual Environment
│── chroma_db/            # Persistent ChromaDB storage
│── ai_research_assistant.py  # Search Agent
│── summarization_agent.py    # Summarization Agent
│── storage_agent.py          # Storage Agent
│── response_agent.py         # AI Response Agent
│── search_results.json       # Stores retrieved search results
│── summary.txt               # Stores summarized content
│── requirements.txt          # Required dependencies
│── README.md                 # Project Documentation
🚀 Features
✅ Web Search: Uses DuckDuckGo API to fetch search results.
✅ Text Summarization: Uses Hugging Face Pegasus to summarize information.
✅ Vector Database: Uses ChromaDB to store and retrieve knowledge efficiently.
✅ AI Responses: Uses GPT-4o to provide intelligent answers based on stored knowledge.

🛠️ Installation & Setup
1️⃣ Clone the Repository

git clone https://github.com/your-github-username/AI-Research-Assistant.git
cd AI-Research-Assistant
2️⃣ Set Up Virtual Environment

python -m venv agentic_env
Activate the virtual environment:

Windows (PowerShell)

agentic_env\Scripts\activate
Mac/Linux

source agentic_env/bin/activate
3️⃣ Install Dependencies

pip install -r requirements.txt
4️⃣ Set Up API Keys
Create a .env file in the root directory and add:

env

OPENAI_API_KEY=your_openai_api_key_here

Alternatively, set it in your environment:

Windows (PowerShell)

$env:OPENAI_API_KEY="your_openai_api_key_here"
Mac/Linux

export OPENAI_API_KEY="your_openai_api_key_here"
🏃‍♂️ Running the Project
1️⃣ Run Search Agent

python ai_research_assistant.py
👉 This fetches search results and stores them in search_results.json

2️⃣ Run Summarization Agent

python summarization_agent.py
👉 This summarizes search results and saves them in summary.txt

3️⃣ Run Storage Agent

python storage_agent.py
👉 This stores the summary into ChromaDB for future retrieval.

4️⃣ Run AI Response Agent

python response_agent.py
👉 Enter a query, and the AI will generate a structured response.

📝 Example Usage

Enter your query: Explain AI Agents in simple terms

🔹 AI Response:

AI agents are software programs that can make decisions, learn from data, and automate tasks. They can range from simple rule-based bots to advanced machine learning models capable of complex reasoning.
🛠️ Troubleshooting
❌ Getting API Errors?

Ensure OPENAI_API_KEY is set correctly in .env or environment variables.
❌ Slow Summarization?

The first run downloads the Pegasus model (~2GB). Subsequent runs are faster.
❌ Missing Dependencies?

Run: pip install -r requirements.txt to reinstall missing packages.
🎯 Future Improvements
✅ Multi-source verification: Fetch and compare multiple sources before summarizing.
✅ Citation system: Link each response to its original source.
✅ Web UI: Build a simple Streamlit frontend.
🤝 Contributing
🚀 Want to improve this project? Contributions are welcome!

Fork the repository
Create a new branch (git checkout -b feature-branch)
Commit changes (git commit -m "Added a new feature")
Push to GitHub (git push origin feature-branch)
Create a Pull Request
