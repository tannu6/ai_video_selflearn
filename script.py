
from groq import Groq

client = Groq(api_key="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")

def generate_script(topic: str) -> str:
    prompt = f"""
    Create a short 4-scene educational script for a 3D animation.
    Topic: {topic}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content