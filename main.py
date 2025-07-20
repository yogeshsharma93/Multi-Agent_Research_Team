from graph.langgraph import build_graph
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    topic = input("Enter your research topic: ")
    graph = build_graph()
    result = graph.invoke({"topic": topic})
    report = result['report']

    with open("outputs/final_report.md", "w") as f:
        f.write(report)
    print("\n✅ Final report saved to outputs/final_report.md")

if __name__ == "__main__":
    main()