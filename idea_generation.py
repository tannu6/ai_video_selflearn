import random

topics = [
    "How volcanoes erupt",
    "How rainbows form",
    "Why do we dream",
    "How octopus change color",
    "What happens inside a black hole",
    "How chameleons change color",
    "How magnets work",
    "How snowflakes form",
    "How lightning forms",
    "How tsunamis form",
    "How DNA is structured",
    "How planets orbit the sun",
    "Why bubbles are round"
]

def get_topic():
    return random.choice(topics)