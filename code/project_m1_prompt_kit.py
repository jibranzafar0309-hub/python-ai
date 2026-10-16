"""
AI Prompt Kit
-------------
Author: Jibran

Ye tool aik local business owner (bakery, clinic, salon, shop etc.) se
5 sawal poochta hai aur phir professional AI prompts print karta hai
(Marketing, Customer Service, Growth, aur bonus WhatsApp reply).
Ye prompts Ollama, Claude ya ChatGPT mein paste kiye ja saktay hain.

Kis ke liye: chotay business owners jinhe AI use karna hai
lekin pata nahi kya type karna hai.
"""

# Why: input() hamesha text (string) deta hai, is liye pehle 4 answers text hi rakhte hain
business_name = input("Business name: ")
business_type = input("Business type (e.g. bakery): ")
city = input("City: ")
customers = input("Main customers (e.g. students, families): ")

# Why: budget number hai, int() text ko number mein convert karta hai
# taake hum usay f-string mein sahi tarah use kar saken
budget = int(input("Monthly budget (PKR): "))

# Why: separator line aik dafa bana lete hain taake bar bar na likhni paray
line = "=" * 45

# Header
print()
print(line)
print(f"   AI Prompt Kit for {business_name}")
print(line)

# Why: har prompt mein role, task, audience aur tone/number hai,
# kyun ke specific prompts se AI ke jawab behtar aate hain
prompt1 = (
    f"You are a social media expert. Write a short Instagram post for "
    f"{business_name}, a {business_type} in {city}. "
    f"Target audience: {customers}. "
    f"Use a friendly tone and include 1 call to action."
)

prompt2 = (
    f"You are the manager of {business_name}, a {business_type} in {city}. "
    f"Write a polite reply to a customer whose order arrived late. "
    f"Apologise sincerely and offer a small discount. Keep it under 80 words."
)

prompt3 = (
    f"You are a business advisor. Suggest 3 low-cost AI tools or ideas that "
    f"a {business_type} in {city} can use to attract {customers}. "
    f"The budget is {budget} PKR per month. "
    f"For each idea, give a short reason and an estimated cost."
)


# Prompts print karna
print()
print("[1] Marketing")
print(prompt1)
print()
print("[2] Customer Service")
print(prompt2)
print()
print("[3] Growth")
print(prompt3)
print()
print(line)