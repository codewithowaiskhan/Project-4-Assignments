def mad_libs():
    print("Let\'s play Mad Libs! fill in the blanks with your own words.")
    
    name = input("Give me a name:")
    place = input("Give me a place:")
    funny_adj = input("Give me a funny adjective:")
    random_object = input("Give me a random object:")
    animal = input("Give me an animal:")
    action_verb = input("Give me an action verb:")
    funny_exclamation = input("Give me a funny exclamation:")
    
    story = f'''
    Once upon a time, there was a person named {name} who lived in {place}.
    One day, they found a {funny_adj} {random_object} that belonged to a {animal}.
    The {animal} was very upset and started to {action_verb} arround.
    {name} couldn't help but laugh and shouted "{funny_exclamation}!".'''
    
    print("\n Here is your Mad Libs story:")
    print(story)
if __name__ == "__main__":
    print(mad_libs())