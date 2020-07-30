import random


class Dice:
    def roll(self):
        fist_roll = random.randint(1, 6)
        second_roll = random.randint(1, 6)

        return fist_roll, second_roll


dice = Dice()
print(f'Dice rolled: {dice.roll()}')
