"""Lesson 07: route an AI request to the right model and estimate its cost.

Private data -> local model (free), code -> strong model, everything else -> cheap model.
"""

# Example prices only (PKR per 1,000 tokens). Replace them with real prices later.
CODE_PRICE = 0.80
CHAT_PRICE = 0.10

# 1. Ask and clean
# Why: users type " Code " or "PRIVATE" with extra spaces and capitals.
# .strip().lower() makes them all match our if/elif checks.
task = input("Task (code / private / chat): ").strip().lower()
tokens = int(input("Estimated tokens: "))  # int() because input() always gives text

# 2. Choose the model
if task == "code":
    model = "claude (cloud, strong at code)"
    price = CODE_PRICE
elif task == "private":
    model = "llama3.2 (local, Ollama)"
    # Why: a local model runs on our own machine, so private data never leaves
    # it and there is no per-token bill.
    price = 0
else:
    model = "haiku (cloud, cheap)"
    price = CHAT_PRICE

# 3. Cost
cost = tokens / 1000 * price

# 4. Length check
# Why: very long requests cost the most, so we warn the user before sending.
if tokens > 4000:
    print("Warning: long request, consider shortening it.")
else:
    print("Length is fine.")

print(f"Chosen model: {model}")
print(f"Estimated cost: {cost:.2f} PKR")

# Stretch: free users cannot send long requests
paid = input("Is this a paid user? (yes/no): ").strip().lower()
if paid == "no" and tokens > 2000:
    print("Upgrade to send long requests.")