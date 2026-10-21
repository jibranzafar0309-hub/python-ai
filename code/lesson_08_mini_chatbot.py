"""Lesson 08: mini chatbot for Sweet Crumbs Bakery.

Answers common questions (hours, price, order, delivery), hands complaints
to a human, and counts the questions it could not answer.
"""

message_count = 0
unanswered = 0
complaints = 0

print("Sweet Crumbs Bot: Hi! Ask about hours, prices, orders or delivery. Type 'bye' to exit.")

# Why: ask the name ONCE, before the loop. Inside the loop it would repeat every message.
name = input("Sweet Crumbs Bot: What is your name? ").strip().title()

while True:
    # Why: .strip().lower() fixes extra spaces and capitals, so "  HOURS " still matches "hours".
    message = input(f"{name}: ").strip().lower()

    if message == "":
        print("Sweet Crumbs Bot: Please type a question.")
    else:
        message_count = message_count + 1

        # Why: complaint rule is FIRST, so an unhappy customer always reaches
        # a person, even if the message also has a word like "order".
        if "late" in message or "wrong" in message or "cold" in message or "refund" in message or "complaint" in message or "problem" in message:
            complaints = complaints + 1
            print("Sweet Crumbs Bot: Sorry about that. The manager will call you today.")
        elif "agent" in message or "human" in message:
            print("Sweet Crumbs Bot: Connecting you to a human...")
            break
        elif message == "bye":
            print(f"Sweet Crumbs Bot: Take care, {name}!")
            break
        # Why: "hi" is a short word hidden inside "which" and "this", so we
        # check it with == and .startswith(), not with `in`.
        elif message == "hi" or message.startswith("hello") or message.startswith("salam"):
            print(f"Sweet Crumbs Bot: Hi {name}! Ask about hours, prices, orders or delivery.")
        elif "hours" in message or "time" in message or "timing" in message or "open" in message or "close" in message:
            print("Sweet Crumbs Bot: We are open 9 am to 9 pm, every day.")
        elif "price" in message or "cost" in message or "how much" in message:
            print("Sweet Crumbs Bot: Cakes start from 1,500 PKR per pound.")
        elif "order" in message or "whatsapp" in message:
            print(f"Sweet Crumbs Bot: Please send flavour, weight and date, {name}. We need 1 day notice.")
        elif "deliver" in message:
            print("Sweet Crumbs Bot: We deliver within 5 km. Delivery charge is 200 PKR.")
        else:
            unanswered = unanswered + 1
            print(f"Sweet Crumbs Bot: I am not sure yet. In Module 2, an AI will answer: You are the friendly assistant of Sweet Crumbs Bakery. Answer in 2 lines: {message}")

print("=" * 40)
print(f"Chat summary: {message_count} messages, {unanswered} unanswered.")
print(f"Complaints received: {complaints}")