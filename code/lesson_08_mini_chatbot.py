"""Lesson 08: mini chatbot for Sweet Crumbs Bakery.

Answers common questions (hours, price, order, delivery), hands complaints
to a human, and counts the questions it could not answer.
"""

BUSINESS = "Sweet Crumbs Bakery"
BOT = "Sweet Crumbs Bot"
COMPLAINT_WORDS = ["late", "wrong", "cold", "refund", "complaint", "delayed", "bad", "problem"]

message_count = 0
unanswered = 0
complaints = 0

print(f"{BOT}: Hi! Ask about hours, prices, orders or delivery. Type 'bye' to exit.")

# Why: ask the name ONCE, before the loop. Inside the loop it would repeat every message.
name = input(f"{BOT}: What is your name? ").strip().title()

while True:
    message = input(f"{name}: ").strip().lower()

    # Why: an empty message is not a real question, so we ask again
    # and do NOT count it in the summary.
    if message == "":
        print(f"{BOT}: Please type a question.")
        continue

    message_count += 1

    # Why: remove punctuation and split into words, so "late?" matches "late"
    # and "chocolate" does NOT match "late" (we compare whole words, not pieces).
    clean = message
    for mark in "?!.,":
        clean = clean.replace(mark, "")
    words = clean.split()

    # Why: complaint and human rules come FIRST. An angry customer must reach
    # a person, even if their message also contains a word like "order".
    if "agent" in words or "human" in words:
        print(f"{BOT}: Connecting you to a human...")
        break
    elif any(word in words for word in COMPLAINT_WORDS):
        complaints += 1
        print(f"{BOT}: Sorry about that. The manager will call you today.")
    elif clean == "bye":
        print(f"{BOT}: Take care, {name}!")
        break
    # Why: short words like "hi" are checked with == / startswith, not `in`,
    # because "hi" is hidden inside "which" and "this".
    elif clean == "hi" or clean.startswith("hi ") or clean.startswith("hello") or clean.startswith("salam"):
        print(f"{BOT}: Hi {name}! Ask about hours, prices, orders or delivery.")
    elif any(word in words for word in ["hours", "hour", "time", "timing", "timings", "open", "close"]):
        print(f"{BOT}: We are open 9 am to 9 pm, every day.")
    elif "price" in words or "cost" in words or "how much" in clean:
        print(f"{BOT}: Cakes start from 1,500 PKR per pound.")
    elif "order" in words or "whatsapp" in words:
        print(f"{BOT}: Please send flavour, weight and date, {name}. We need 1 day notice.")
    elif "delivery" in words or "deliver" in words:
        print(f"{BOT}: We deliver within 5 km. Delivery charge is 200 PKR.")
    else:
        unanswered += 1
        print(
            f"{BOT}: I am not sure yet. In Module 2, an AI will answer: "
            f"You are the friendly assistant of {BUSINESS}. Answer in 2 lines: {message}"
        )

print("=" * 40)
print(f"Chat summary: {message_count} messages, {unanswered} unanswered.")
print(f"Complaints received: {complaints}")