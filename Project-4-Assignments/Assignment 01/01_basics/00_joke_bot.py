PROMPT: str = "What do you want?"
JOKE: str = "Why don't skeletons fight each other?Because they don't have the guts for it!And even if they did, it just be a bone of contention!😆"
SORRY: str = "Sorry i only tell jokes."

def main():
    user_input = input(PROMPT)
    user_input = user_input.strip().lower()
    
    if "joke" in user_input:
        print(JOKE)
    else:
        print(SORRY)

if __name__ == "__main__":
    main()