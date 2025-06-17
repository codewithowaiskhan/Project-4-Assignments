correct_affirmation = "I am  capable of doing anything. I put my mind too."

def main():
    print("Welcome to the Wholesome Machine")
    while True:
        user_input = input("Please type the following affirmation:" + correct_affirmation)
        if user_input == correct_affirmation:
            print("That\`s right!")
            break
        else:
            print("Oops! that was not the affirmation. Please Try Again!")

if __name__ == "__main__":
    main()