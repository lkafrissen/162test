#!//usr/bin/python3

def randomizer():
    user_choice = input("Choose a number: 1 - 3: ")

    if user_choice == 1:
        print("Red")
    elif user_choice == 2:
        print("Blue")
    elif user_choice == 3:
        print("Green")

if __name__ == "__main__":
    randomizer()
