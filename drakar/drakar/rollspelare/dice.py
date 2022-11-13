from random import randint

from pydantic import BaseModel, Field


class DiceRollDefintion(BaseModel):
    sides: int
    throws: int
    bonus: int = Field(default=0)


def best_of_set(roll_def: DiceRollDefintion, sets_to_roll):
    results = []
    for _ in range(sets_to_roll):
        results.append(roll_dice(roll_def))
    results.sort(reverse=True)
    return results[0]


def roll_dice(roll_def: DiceRollDefintion) -> int:
    acc = 0
    for _ in range(roll_def.throws):
        acc += randint(1, roll_def.sides)
    return acc + roll_def.bonus


DICE_1T6 = DiceRollDefintion(throws=1, sides=6)
DICE_2T6 = DiceRollDefintion(throws=2, sides=6)
DICE_3T6 = DiceRollDefintion(throws=3, sides=6)
DICE_1T8 = DiceRollDefintion(throws=1, sides=8)
DICE_2T8 = DiceRollDefintion(throws=2, sides=8)
DICE_1T18 = DiceRollDefintion(throws=1, sides=18)
DICE_1T20 = DiceRollDefintion(throws=1, sides=20)
DICE_2T20 = DiceRollDefintion(throws=2, sides=20)
