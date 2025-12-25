# import requests
# import re

# # === CONFIG ===
# API_KEY = "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"
# MODEL = "gpt-3.5-mini"
# ENDPOINT = "https://openrouter.ai/api/v1/chat/completions"

# HEADERS = {
#     "Authorization": f"Bearer {API_KEY}",
#     "Content-Type": "application/json"
# }

# def evaluate_task_level(task: str) -> int:
#     """
#     Sends a task to the model and returns a numeric difficulty level.
#     """
#     prompt = f"""
#         You are a task difficulty evaluator.
#         Respond only in this exact format: difficulty_level:<integer>

#         Here are examples:
#         Task: Blink LED using Arduino
#         difficulty_level:10

#         Task: Python networking (3 hours)
#         difficulty_level:50

#         Task: Learning quantum computing
#         difficulty_level:300

#         Task: Design distributed operating system
#         difficulty_level:150

#         Task: Understand pointers in C
#         difficulty_level:50

#         Now evaluate this new task:

# Task: {task}
# """

#     body = {
#         "model": MODEL,
#         "messages": [{"role": "user", "content": prompt}],
#         "max_tokens": 25,
#         "temperature": 0.3
#     }

#     response = requests.post(ENDPOINT, headers=HEADERS, json=body)
#     data = response.json()

#     # Correct extraction from OpenRouter response
#     try:
#         text = data["choices"][0]["message"]["content"].strip()
#     except (KeyError, IndexError) as e:
#         raise ValueError(f"Unexpected API response structure: {data}")

#     # Extract integer
#     match = re.search(r"difficulty_level:(\d+)", text)
#     if match:
#         return int(match.group(1))
#     else:
#         raise ValueError(f"Invalid output from model: {text}")

# # === Test Tasks ===
# tasks = [
#     "Python networking (estimated time 3 hours)",
#     "Learning quantum computing",
#     "Blink LED using Arduino",
#     "Design distributed operating system",
#     "Understand pointers in C"
# ]

# for t in tasks:
#     try:
#         level = evaluate_task_level(t)
#     except Exception as e:
#         level = str(e)
#     print(f"{t} → Level: {level}")



import ollama
import re

MODEL_NAME = "gemma2:9b"

def evaluate_task_level(task: str) -> int:
    prompt = f"""
You are a task difficulty evaluator.

Rules:
- Return ONLY one line
- Difficulty level : for low difficulty starts from 1 and highest level its 1000
- Format exactly: difficulty_level:<number>
- No explanation

Task: {task}
"""

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    text = response["message"]["content"].strip()
    # print("RAW:", text)

    match = re.search(r"difficulty_level\s*:\s*(\d+)", text)
    if match:
        return int(match.group(1))
    else:
        raise ValueError(f"Invalid output: {text}")

# ---------------- TEST ---------------- #

tasks = [
    "Python networking (estimated time 3 hours)",
    "Learning quantum computing",
    "Blink LED using Arduino",
    "Design distributed operating system",
    "Understand pointers in C"
]

for task in tasks:
    try:
        level = evaluate_task_level(task)
        print(f"{task} → Level: {level}")
    except Exception as e:
        print(task, "→ ERROR:", e)
