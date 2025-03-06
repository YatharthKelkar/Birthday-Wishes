import random

def generate_birthday_wish(name="Friend", age=0, style="random"):
    heartfelt = [
        f"Happy {age}th Birthday, {name}! 🎉 May your day be filled with love, laughter, and all the happiness in the world!",
        f"Wishing you a fantastic year ahead, {name}! May your dreams come true and your smile never fade. 😊",
        f"{name}, welcome to {age}! May this special day bring you endless joy, success, and memories to cherish forever!"
    ]

    funny = [
        f"Happy {age}th Birthday, {name}! 🎂 You're officially a teenager—get ready for more homework and less sleep! 😆",
        f"{name}, now that you're {age}, remember: with great power comes... more responsibilities! Just kidding, enjoy your day!",
        f"Congrats, {name}! You’ve leveled up to {age}. Time to unlock new skills and enjoy extra cake! 🎮🎂"
    ]

    poetic = [
        f"Roses are red, violets are blue,\n{name} is {age}, and awesome too! 🎶",
        f"A day so bright, a heart so light,\nWishing {name} joy, from morning to night! ✨",
        f"Another year, a brand-new cheer,\n{name}, may your dreams shine crystal clear! 🌟"
    ]

    techy = [
        f"Happy {age}th Birthday, {name}! May your code compile without errors and your life be bug-free! 🖥️🎂",
        f"{name}, you're like an ever-updating program—now at version {age}.0! More features, more fun! 🚀",
        f"System Update: {name} has reached version {age}.0. Changelog: More awesomeness, better skills, and unlimited cake! 🎉"
    ]

    styles = {
        "heartfelt": heartfelt,
        "funny": funny,
        "poetic": poetic,
        "techy": techy,
        "random": heartfelt + funny + poetic + techy
    }

    return random.choice(styles.get(style, styles["random"]))

# Ask for the birthday person's name and age
friend_name = input("Enter the birthday person's name: ")
friend_age = input(f"How old is {friend_name} turning? ")

# Ensure age is a valid number
while not friend_age.isdigit():
    friend_age = input("Please enter a valid age: ")

friend_age = int(friend_age)  # Convert age to an integer

# Ask for the wish style
style_choice = input("Choose a style (heartfelt, funny, poetic, techy, random): ").lower()

# Print the personalized birthday wish
print("\nGenerated Birthday Wish: ")
print(generate_birthday_wish(friend_name, friend_age, style_choice))
