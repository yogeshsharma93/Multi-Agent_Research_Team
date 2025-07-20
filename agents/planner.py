import os
import json
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from prompts.templates import planner_prompt

load_dotenv() 

llm = ChatGroq(model_name="llama3-70b-8192", temperature=0.3, api_key=os.getenv("GROQ_API_KEY"))

def planner_agent(state):
    topic = state['topic']
    prompt = planner_prompt.format(topic=topic)
    response = llm.invoke([HumanMessage(content=prompt)])
    try:
        subquestions = json.loads(response.content)
    except json.JSONDecodeError:
        print("Failed to parse planner output:", response.content)
        subquestions = []

    return {'subquestions': subquestions, 'claims': [], 'topic': topic}


