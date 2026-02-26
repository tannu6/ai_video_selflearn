from groq import Groq

client = Groq(api_key="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")

models = client.models.list()

for m in models.data:
    print(m.id)