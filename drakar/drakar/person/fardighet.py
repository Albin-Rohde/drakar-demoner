import enum
from typing import Tuple, Optional

from pydantic.main import BaseModel

from drakar.drakar.person.grundegenskaper import Grundegenskaper


class FardighetCost(BaseModel):
    core: int
    yrke: int
    general: int


class FardighetSpec:
    cost: FardighetCost
    base: str


class Fardighet:
    namn: str = None
    level: int = None
    bas: str = None
    bas_level: int = None
    text: Optional[str] = None

    def __init__(self, ge: Grundegenskaper, level):
        self.level = level
        self.bas_level = ge.dict()[self.bas]

    def use_skill(self, dice_roll: int) -> bool:
        return dice_roll <= self.level


class Administration(Fardighet):
    namn = "Administration"
    bas = "intelligens"

    def use_skill(self, dice_roll: int) -> bool:
        return dice_roll <= self.bas_level


class Avvapna(Fardighet):
    namn = "Avväpna"
    bas = "smidighet"


class Magic(Fardighet):
    namn = "Magi / Besvärjelsekont"
    bas = "intelligens"


class Botanik(Fardighet):
    namn = "Botanik"
    bas = "intelligens"


class Dans(Fardighet):
    namn = "Dans"
    bas = "smidighet"


class Djurtraning(Fardighet):
    namn = "Djurträning"
    bas = "intelligens"


class DraVapen(Fardighet):
    namn = "Dra vapen"
    bas = "smidghet"


class DramatikEnemy(enum.Enum):
    OKAND = "OKÄND"
    HORT_OM = "HÖRT_OM"
    KANNER_TILL = "KÄNNER_TILL"
    KANNER_BRA = "KÄNNER_BRA"


class Dramatik(Fardighet):
    namn = "Dramatik"
    bas = "intelligens"

    def use_skill(
        self, dice_roll: int,
        enemy: DramatikEnemy = DramatikEnemy.OKAND
    ) -> bool:
        mod = 0
        







def get_fp_for_ge_skill(skill: int):
    if skill < 3:
        return 2
    if skill <= 5:
        return 3
    if skill <= 8:
        return 4
    if skill <= 10:
        return 5
    if skill <= 12:
        return 6
    if skill <= 14:
        return 7
    if skill <= 16:
        return 8
    if skill == 17:
        return 9
    if skill == 18:
        return 11
    if skill == 19:
        return 13
    if skill > 19:
        return 15


def calc_total_fp(ge: Grundegenskaper):
    acc_fp = 0
    for _, ge_skill in ge.dict().items():
        acc_fp += get_fp_for_ge_skill(ge_skill)

#def get_fv_level_cost(FardighetCost) -> int:
#    if skill_level <= 7:
#        return 1
