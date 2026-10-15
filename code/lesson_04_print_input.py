"""prompt_builder.py

A tiny tool for a digital agency: it asks for a user's name, their
business type and one problem the business faces, then builds a
ready-to-use AI prompt that can be pasted into any chat model.
"""

# Collect the three inputs. .strip() removes accidental spaces so the
# final prompt doesn't end up with ugly double spaces in the middle.
name = input("Your name: ").strip()
business = input("Business type: ").strip()
problem = input("Biggest problem: ").strip()

print(f"\nWelcome, {name}!")

# An f-string keeps the prompt template readable in one place, so the
# agency can tweak the wording later without touching the logic.
prompt = f"Suggest 3 AI solutions for a {business} that struggles with {problem}."

print("--- Your AI Prompt ---")
print(prompt)
