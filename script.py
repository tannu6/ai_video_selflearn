
from groq import Groq

client = Groq(api_key="your api key")

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