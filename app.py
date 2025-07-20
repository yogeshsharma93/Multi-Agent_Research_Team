import streamlit as st
from graph.langgraph import build_graph
from dotenv import load_dotenv
import os

load_dotenv()
os.makedirs("outputs", exist_ok=True)

st.set_page_config(page_title="Multi-Agent Research Team")
st.title("🔎 Self-Correcting Research Assistant")

user_topic = st.text_input("Enter your research topic:")

if st.button("Generate Report") and user_topic.strip():
    graph = build_graph()
    with st.spinner("Researching..."):
        result = graph.invoke({"topic": user_topic})
        report = result['report']
        with open("outputs/final_report.md", "w") as f:
            f.write(report)
        st.success("Done!")
        st.markdown(report, unsafe_allow_html=True)
        st.success("Report saved to outputs/final_report.md")
