import random

def roll_dice():
    die1:int = random.randint(1, 6)
    die2:int = random.randint(1, 6)
    total:int = int(die1 + die2)
    print("First die:", + die1)
    print("Second die:", + die2)
    print(f"totsl of tow dies:{total}")
if __name__ == "__main__":
    roll_dice()
    