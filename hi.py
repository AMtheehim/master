print("Hello partner!")

name = input("What's your name? ").strip()
print(f"How are you doing today, {name}?")

valid_responses = ['good', 'amazing', 'okay', 'alright', 'bad', 'terrible']

while True:
    feeling = input("Are you feeling good, amazing, okay, alright, bad, or terrible today? ").strip().lower()
    
    if feeling in valid_responses:
        break
    else:
        print(f"ait pall just say how your feeling")

# Check the feeling and respond accordingly
if feeling in ['good', 'amazing']:
    print(f"That's good to hear, {name}!")
elif feeling in ['okay', 'alright']:
    print(f"That's good to hear, {name}!")
elif feeling in ['bad', 'terrible']:
    print(f"Hope you get better soon, {name}.")