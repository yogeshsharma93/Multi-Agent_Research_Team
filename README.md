# Multi-Agent_Research_Team

This project implements an autonomous team of AI agents that can research any given topic and produce a final report with **verifiable citations**, using a **LangGraph-based workflow**. The system is self-correcting—claims are validated, and only verified information is included in the final report.

---

## 📌 Key Features

- **Planner Agent**: Breaks down the topic into sub-questions.
- **Web Researcher Agent**: Uses the web to gather answers and generate claims.
- **Critic Agent**: Validates claims by matching them against actual source content.
- **Retry Agent**: Re-researches invalid claims.
- **Writer Agent**: Generates a clean report with clickable citations.
- **Final Report Output**:
  - Displayed directly in **Streamlit**
  - Also saved at: `outputs/final_report.md`

---

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/multi-agent-research.git
cd multi-agent-research
```

### 2. Install Required Packages

Make sure you have Python 3.9+, then install dependencies:
```bash
pip install -r requirements.txt
```


### 3. Set API Keys
Add your API keys in .env file:

```bash
GROQ_API_KEY=your-groq-api-key
SERPER_API_KEY=your-serper-api-key
```

---

## ▶️ How to Run
Run via Streamlit (Recommended)

```bash
streamlit run app.py
```

- Enter your research topic in the input field.
- Click "Generate Report".

The final report will be:
- Displayed in the browser
- Saved to outputs/final_report.md
  
---

## 📚 Tech Stack

- **LangGraph** – multi-agent orchestration
- **LangChain** – agent and memory logic
- **GROQ (LLaMA3)** – LLM used for all agent responses
- **Serper.dev** – Google search API integration
- **Streamlit** – frontend for user interaction


