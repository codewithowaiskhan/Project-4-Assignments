def count_numbers():
    count_dict = {}
    
    while True:
        user_input = input("Enter a number (or 'Exit' to quit): ").strip()
        
        if user_input.lower() == "exit":
            break
            
        if user_input.isdigit():
            num = int(user_input)
            count_dict[num] = count_dict.get(num, 0) + 1
        else:
            print("Invalid input. Please enter a number or 'Exit'.")
            
    return count_dict
    
def display_counts(count_dict):
    print("\nNumber Counts:")
    for key, value in count_dict.items():
        print(f"{key} appears {value} time(s)")
            
if __name__ == "__main__":
    counts = count_numbers()
    display_counts(counts)