import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from prompts.templates import critic_prompt

load_dotenv()  

llm = ChatGroq(model_name="llama3-70b-8192", temperature=0.3, api_key=os.getenv("GROQ_API_KEY"))

def critic_agent(state):
    validated_claims = []
    retry_claims = []
    for item in state['claims']:
        prompt = critic_prompt.format(claim=item['claim'], snippet=item['snippet'])
        result = llm.invoke(prompt).content.strip()
        if result.startswith("PASS"):
            validated_claims.append(item)
        else:
            retry_claims.append(item)
    return {
        'validated_claims': validated_claims,
        'retry_claims': retry_claims,
        'topic': state['topic']
    }
