# app.py
def main():
    print("Welcome to Working Copy Test!")
    name = input("What is your name? ")
    print(f"Hello, {name}! This is running from your iPhone using Git!")

    # Basic logic test
    mood = input("How are you feeling today? (good/bad) ").strip().lower()
    if mood == "good":
        print("That's awesome! Keep it up!")
    elif mood == "bad":
        print("I'm sorry to hear that. Tomorrow is a new day!")
    else:
        print("Interesting mood choice!")

if __name__ == "__main__":
    main()