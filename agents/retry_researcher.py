import os
import requests
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()  

SERPER_API_KEY = os.getenv("SERPER_API_KEY")
llm = ChatGroq(model_name="llama3-70b-8192", temperature=0.3, api_key=os.getenv("GROQ_API_KEY"))

def retry_researcher(state):
    retry_claims = state.get('retry_claims', [])
    new_validated = []
    for item in retry_claims:
        response = requests.post(
            "https://google.serper.dev/search",
            headers={"X-API-KEY": SERPER_API_KEY},
            json={"q": item['claim']}
        )
        data = response.json()
        results = data.get("organic", [])
        for result in results[:2]:
            new_claim = {
                'claim': item['claim'],
                'source_url': result.get('link'),
                'snippet': result.get('snippet', '')[:500]
            }
            prompt = f"CLAIM: {new_claim['claim']}\n\nSOURCE: {new_claim['snippet']}\n\nPASS or FAIL?"
            result_text = llm.invoke(prompt).content.strip()
            if result_text.startswith("PASS"):
                new_validated.append(new_claim)
                break
    return {
        'validated_claims': state['validated_claims'] + new_validated,
        'topic': state['topic']
    }
