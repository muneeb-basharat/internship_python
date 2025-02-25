import random

def flip_coin():
    return random.choice(["Heads", "Tails"])

while True:
    input("Press Enter to flip the coin... ")
    result = flip_coin()
    print(f"The coin landed on: {result}")

    play_again = input("Flip again? (y/n): ").strip().lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break