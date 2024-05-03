import random

def roll_dice():

    dice_drawing = {
        1: (
            "-----",
            "|   |",
            "| o |",
            "|   |",
            "_____",
        ),
        2: (
           "_____",
           "|o  |",
           "|   |",
           "|  o|",
           "_____",
        ),
        3: (
           "_____",
           "|o  |",
           "| o |",
           "|  o|",
           "_____",
        ),
        4: (
           "_____",
           "|o o|",
           "|   |",
           "|o o|",
           "_____",
        ),
        5: (
           "_____",
           "|o o|",
           "| o |",
           "|o o|",
           "_____",
        ),
        6: (
           "_____",
           "|o o|",
           "|o o|",
           "|o o|",
           "_____",
        ),

    }
    roll = input("Roll the dice? (Yes/No) : ")
    while roll.lower() == "Yes". lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print("dice rolled: {} and {}". format(dice1, dice2))
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))

        roll = input("Roll again? (Yes/No): ")
roll_dice()