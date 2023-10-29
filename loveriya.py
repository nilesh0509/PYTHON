import time

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

def love_game():
    print_slow("Welcome to the Loveriya Game!")
    name = input("What's your name?: ")
    crush = input("What's your Crush  name?: ")
    print_slow(f"Hello, {name}! You're about to go on a virtual date.")
    time.sleep(1)

    print_slow(f"You're at a beautiful park with your date, {crush}.")
    print_slow("You can choose how you want to spend the day.")

    choices = ["1. Have a picnic by the lake.", "2. Take a romantic walk in the garden.", "3. Play a game of frisbee."]

    for choice in choices:
        print_slow(choice)
        time.sleep(0.5)

    decision = input("Enter the number of your choice (1/2/3): ")

    if decision == "1":
        print_slow(f"You and {crush} have a wonderful picnic by the lake.")
        print_slow("The date goes really well, and you feel a strong connection.")
    elif decision == "2":
        print_slow(f"You and {crush} take a romantic walk in the garden.")
        print_slow("You share your thoughts and feelings, and the connection deepens.")
    elif decision == "3":
        print_slow("You play a game of frisbee and have a lot of fun.")
        print_slow("You share a lot of laughter, and the date goes great.")

    time.sleep(1)
    print_slow("The sun sets, and it's time to say goodbye.")
    time.sleep(1)

    print_slow(f"{crush} says, 'I had a fantastic time with you, {name}!'")
    time.sleep(1)
    print_slow("What do you say?")
    response = input("Enter your response: ")

    if "love" in response.lower() or "I had a great time too" in response:
        print_slow(f"{crush} smiles and says, 'I love you too!'")
        print_slow("Congratulations, it's a happy ending! You're in love!")
    else:
        print_slow(f"{crush} smiles and says, 'I had a wonderful time as well.'")
        print_slow("It may not be love yet, but it's the start of something beautiful.")

    print_slow("Thanks for playing the Loveriya Game!")

if __name__ == "__main__":
    love_game()
