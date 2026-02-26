from groq import Groq
import re

client = Groq(api_key="your api key")


def clean_prompt(line: str) -> str | None:
    """
    Remove numbering, bullets, titles, and keep valid prompt text.
    """
    line = line.strip()

    # remove numbering like "1. ", "2) ", "- "
    line = re.sub(r"^[\-\*\d\.\)\s]+", "", line)


    if len(line) < 3:
        return None
    if "prompt" in line.lower():
        return None
    if "here are" in line.lower():
        return None

    return line


def generate_image_prompts(script_text: str):
    """
    Use Groq LLM to convert script into clean visual prompts.
    """

    instruction = """
You generate image prompts for an animation.
Rules:
- max 10 words
- concrete visual objects
- no numbering
- no titles
- one prompt per line
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": instruction},
            {"role": "user", "content": script_text},
        ],
        temperature=0.4,
    )

    raw = response.choices[0].message.content

    lines = raw.split("\n")

    prompts = []
    for l in lines:
        p = clean_prompt(l)
        if p:
            prompts.append(p)
    return prompts[:4]