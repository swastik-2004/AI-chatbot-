from groq import Groq
from backend.config import GROQ_API_KEY


SYSTEM_PROMPT = """
You are a professional career advisor AI.

Provide structured, supportive, and actionable career advice.

Focus only on:
- Career growth
- Skill development
- Interview preparation
- Job search strategies
- Professional development

If the query is not career-related, politely redirect to career topics.
"""


class LLMClient:
    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)

    def generate_response(self, messages: list) -> str:
        response = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",  # 🔥 Very powerful free model
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                *[
                    {"role": msg["role"], "content": msg["parts"][0]}
                    for msg in messages
                ],
            ],
            temperature=0.7,
            max_tokens=400,
        )

        return response.choices[0].message.content