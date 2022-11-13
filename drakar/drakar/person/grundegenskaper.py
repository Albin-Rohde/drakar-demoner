from pydantic import BaseModel, Field

from drakar.drakar.person.dice import best_of_set, DICE_3T6, DICE_2T6


class Grundegenskaper(BaseModel):
    styrka: int = Field(default=0)
    fysik: int = Field(default=0)
    smidighet: int = Field(default=0)
    storlek: int = Field(default=0)
    intelligens: int = Field(default=0)
    perception: int = Field(default=0)
    spiritius: int = Field(default=0)
    psyke: int = Field(default=0)
    karisma: int = Field(default=0)


def generate_ge():
    return Grundegenskaper(
        styrka=best_of_set(DICE_3T6, 2),
        fysik=best_of_set(DICE_3T6, 2),
        smidighet=best_of_set(DICE_3T6, 2),
        storlek=best_of_set(DICE_2T6, 2),
        intelligens=best_of_set(DICE_3T6, 2),
        perception=best_of_set(DICE_3T6, 2),
        spiritius=best_of_set(DICE_3T6, 2),
        psyke=best_of_set(DICE_3T6, 2),
        karisma=best_of_set(DICE_3T6, 2),
    )