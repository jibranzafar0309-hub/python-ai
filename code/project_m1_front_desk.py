"""
Sweet Crumbs Front Desk
Answers common bakery questions with rules, calculates price quotes,
and prepares AI-ready prompts for everything else.
Business: Sweet Crumbs bakery, Lahore.
"""

# Constants in UPPER_CASE because their values never change while the program runs
BOT_NAME = "Sweet Crumbs Desk"
DELIVERY_FEE = 200
FREE_DELIVERY_LIMIT = 3000
CLOUD_PRICE_PER_1K_TOKENS = 0.1  # example price in PKR
BULK_MIN_QUANTITY = 10
BULK_DISCOUNT_PERCENT = 10
LOCAL_MODEL = "gemma3:1b"
CLOUD_MODEL = "small cloud model (cheap)"

print("=" * 50)
print(f"   {BOT_NAME}: rules, quotes and AI-ready prompts")
print("=" * 50)
print("Ask anything, type /quote for a price, or bye to exit.")

# Ask the name only once, before the loop, so we can reuse it in every reply
customer_name = input(f"{BOT_NAME}: What is your name? ").strip().title()
print(f"{BOT_NAME}: Welcome, {customer_name}!")

# Counters live before the loop so they keep growing across the whole chat
messages = 0
answered_by_rules = 0
unanswered = 0
quotes = 0
quoted_value = 0
ai_cost = 0

while True:
    message = input(f"{customer_name}: ").strip().lower()

    if message == "":
        # Empty input is not a real message, so we just ask again and do not count it
        print(f"{BOT_NAME}: Please type your question.")
    else:
        messages += 1

        if message == "bye":
            answered_by_rules += 1
            print(f"{BOT_NAME}: Goodbye, {customer_name}!")
            break

        # Complaint rule is first so an unhappy customer always reaches a human
        elif "refund" in message or "complaint" in message or " late" in message or message.startswith("late"):
            answered_by_rules += 1
            print(f"{BOT_NAME}: Sorry about that. A manager will call you within 1 hour.")

        # Greeting uses == / startswith, not "in", because "hi" hides inside "which"
        elif message == "hi" or message.startswith("hello") or message.startswith("salam"):
            answered_by_rules += 1
            print(f"{BOT_NAME}: Hello! How can I help you?")

        elif "hours" in message or "open" in message or "timing" in message:
            answered_by_rules += 1
            print(f"{BOT_NAME}: We are open 9 am to 10 pm, every day.")

        elif "location" in message or "where" in message:
            answered_by_rules += 1
            print(f"{BOT_NAME}: We are in Gulberg, Lahore.")

        elif "fee" in message or "charge" in message or "delivery" in message:
            answered_by_rules += 1
            print(f"{BOT_NAME}: Delivery is {DELIVERY_FEE} PKR, free from {FREE_DELIVERY_LIMIT:,} PKR.")

        elif message == "/quote":
            item = input(f"{BOT_NAME}: Which item? ").strip().lower()
            quantity = int(input(f"{BOT_NAME}: How many? "))

            # Price is 0 for unknown items, so one check below can reject them politely
            if item == "cupcake":
                price = 250
            elif item == "brownie":
                price = 300
            elif item == "chocolate cake":
                price = 1500
            else:
                price = 0

            if price == 0:
                print(f"{BOT_NAME}: Sorry, {item} is not on our menu.")
            else:
                subtotal = price * quantity

                if quantity >= BULK_MIN_QUANTITY:
                    discount = subtotal * BULK_DISCOUNT_PERCENT // 100
                else:
                    discount = 0

                # Delivery is checked AFTER the discount, because the customer pays the discounted amount
                after_discount = subtotal - discount
                if after_discount >= FREE_DELIVERY_LIMIT:
                    delivery = 0
                else:
                    delivery = DELIVERY_FEE

                total = after_discount + delivery

                quotes += 1
                quoted_value += total

                print(f"{BOT_NAME}: {quantity} x {item} = {subtotal:,} PKR")
                print(f"     Discount: -{discount:,} PKR | Delivery: {delivery:,} PKR")
                print(f"     Total: {total:,} PKR")

        else:
            unanswered += 1

            # Slice to 150 characters so a very long question cannot make the AI call expensive
            question = message.capitalize()[:150]

            # Rough rule: 1 token is about 4 characters
            tokens = round(len(question) / 4)

            # Private details must never leave the shop, so they go to the local model
            if "phone" in message or "cnic" in message or "my address" in message:
                model_name = f"{LOCAL_MODEL} (local, private)"
                cost = 0
            else:
                model_name = CLOUD_MODEL
                cost = tokens / 1000 * CLOUD_PRICE_PER_1K_TOKENS

            ai_cost += cost

            prompt = f"""You are the assistant of Sweet Crumbs bakery.
Answer {customer_name} in 2 short lines. Question: {question}"""

            print(f"{BOT_NAME}: Good question! Routed to: {model_name} (~{tokens} tokens)")
            print(f"     Prompt: {prompt}")
            
# The report is outside the loop (no indent) so it prints once, after "bye" breaks the loop
print("=" * 50)
print("Session report")
print(f"Messages: {messages} | Answered by rules: {answered_by_rules} | Unanswered: {unanswered}")
print(f"Quotes: {quotes} | Quoted value: {quoted_value:,} PKR")
print(f"Estimated AI cost for unanswered questions: {ai_cost:.4f} PKR")
print("=" * 50)