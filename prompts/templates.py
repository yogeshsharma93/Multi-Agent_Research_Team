planner_prompt = """
You are a planner. Break down the topic below into 3-5 researchable sub-questions.

Topic: "{topic}"

Respond only with a JSON list of strings, like:
[
  "Question 1",
  "Question 2",
  "Question 3"
]
"""

critic_prompt = """
You are a fact-checking agent. Determine if the CLAIM is directly supported by the SOURCE.

CLAIM: {claim}

SOURCE:
{snippet}

Respond with "PASS" if supported or "FAIL" and a reason.
"""