"""Clean a customer's messy question, measure it, and build a safe AI prompt.

Steps: ask -> clean -> measure -> check for "python" -> build the prompt.
"""

# Demo price only (dollars per 1,000 tokens). Replace it with your model's real price.
PRICE_PER_1K_TOKENS = 5.00

# 1. Ask the user
raw_name = input("Your name: ")
raw_question = input("Your question: ")

# 2. Clean
# Why: customers type extra spaces and random capitals, so we fix the text
# BEFORE it goes to an AI. Messy input wastes tokens and confuses the model.
name = raw_name.strip().title()
question = raw_question.strip().capitalize()

# Stretch: replace a bad word before building the prompt
question = question.replace("stupid", "***")

# 3. Measure
characters = len(question)
# Why: AI models charge by tokens, not characters. Roughly 4 characters = 1 token,
# so this gives a cheap estimate without any special library.
tokens = round(characters / 4)
cost = tokens / 1000 * PRICE_PER_1K_TOKENS

# 4. Python check
# Why: .lower() first, so "PYTHON", "Python" and "python" all match.
mentions_python = "python" in question.lower()

print("=" * 40)
print(f"Cleaned question: {question}")
print(f"Characters: {characters}, about {tokens} tokens")
print(f"Mentions Python: {mentions_python}")
print(f"Estimated cost: ${cost:.2f}")
print("=" * 40)

# 5. Build the prompt
# Why: [:150] slicing stops a very long question from creating a huge,
# expensive prompt. That is the "safely sized" part.
prompt = f"""You are a friendly Python tutor.
Greet {name} by name and answer in 3 short lines.
Question: {question[:150]}
"""

print(prompt)