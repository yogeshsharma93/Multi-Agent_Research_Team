import os
import requests

SERPER_API_KEY = os.getenv("SERPER_API_KEY")

def researcher_agent(state):
    subquestions = state['subquestions']
    claims = []
    for question in subquestions:
        response = requests.post(
            "https://google.serper.dev/search",
            headers={"X-API-KEY": SERPER_API_KEY},
            json={"q": question}
        )
        data = response.json()
        results = data.get("organic", [])
        for result in results[:3]:
            claims.append({
                'claim': question,
                'source_url': result.get('link'),
                'snippet': result.get('snippet', '')[:500]
            })
    return {'claims': claims, 'topic': state['topic']}