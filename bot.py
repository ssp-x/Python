name = input("Hello! What is your name? ").strip()
print(f"Nice to meet you, {name}!")

age_input = input("How old are you? ").strip()
if age_input.isdigit():
    age = int(age_input)
else:
    print("That doesn’t look like a number, I’ll assume you’re 0.")
    age = 0

bot_age = 3
if age > bot_age:
    print(f"You are {age - bot_age} years older than me. I'm only {bot_age} years old!")
elif age < bot_age:
    print(f"I'm {bot_age - age} years older than you. I'm {bot_age} years old!")
else:
    print(f"No way—we’re both {bot_age} years old!")

color = input("What's your favorite color? ").strip()
print(f"Oh, {color.capitalize()} is a beautiful color!")
