"""AI Model Profile Card.

Client ko dikhata hai ke chosen AI model kaun sa hai aur
ek chat ki estimated cost PKR mein kitni banegi.
"""

# Model profile: har value ki type alag hai (str, int, float, bool)
model_name = "gemma3:1b"
context_window = 32768
price_per_1k_tokens = 0.8  # example price, real price nahi
runs_locally = True

print("--- AI Model Profile Card ---")
print(f"Model: {model_name} {type(model_name)}")
print(f"Context window: {context_window} tokens {type(context_window)}")
print(f"Price per 1K tokens: {price_per_1k_tokens} PKR {type(price_per_1k_tokens)}")
print(f"Runs locally: {runs_locally} {type(runs_locally)}")

# Why: input() hamesha str deta hai, math ke liye int chahiye
tokens_per_chat = int(input("Tokens per chat: "))
print(f"Tokens per chat: {tokens_per_chat}")

# Why: price 1000 tokens ki hai, isliye pehle tokens ko 1000 se divide karte hain
estimated_cost = round((tokens_per_chat / 1000) * price_per_1k_tokens, 2)
print(f"Estimated cost: {estimated_cost} PKR")

# Stretch: monthly cost (30 din)
chats_per_day = int(input("Chats per day: "))
# Why: round() sirf aakhir mein karte hain taake chhoti errors jama na hon
monthly_cost = round((tokens_per_chat / 1000) * price_per_1k_tokens * chats_per_day * 30, 2)
print(f"Estimated monthly cost: {monthly_cost} PKR")