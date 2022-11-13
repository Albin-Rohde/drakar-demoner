import enum
from typing import Dict, Optional

from pydantic.main import BaseModel, Field

from drakar.drakar.person.dice import DICE_2T20, DICE_1T3, DICE_2T3, DICE_3T3 ,roll_dice, DiceRollDefintion


class Klass(enum.Enum):
    EGENDOMSLOS = "Egendomslös"
    LAGRE_UNDERKLASS = "Lägre underklass"
    HOGRE_UNDERKLASS = "Högre underklass"
    LAGRE_MEDELKLASS = "Lägre medelklass"
    HOGRE_MEDELKLASS = "Högre medelklass"
    LAGRE_OVERKLASS = "Lägre överklass"
    HOGRE_OVERKLASS = "Högre överklass"
    LAG_ADEL = "Lågadel"
    HOG_ADEL = "Högadel"


def get_random_klass() -> Klass:
    value = roll_dice(DICE_2T20)
    if value == 2:
        return Klass.EGENDOMSLOS
    if value <= 7:
        return Klass.LAGRE_UNDERKLASS
    if value <= 15:
        return Klass.HOGRE_UNDERKLASS
    if value <= 20:
        return Klass.LAGRE_MEDELKLASS
    if value <= 27:
        return Klass.HOGRE_MEDELKLASS
    if value <= 32:
        return Klass.LAGRE_OVERKLASS
    if value <= 36:
        return Klass.HOGRE_OVERKLASS
    if value <= 39:
        return Klass.LAG_ADEL
    if value == 30:
        return Klass.HOG_ADEL


class KlassCoinDefinition(BaseModel):
    dice: Optional[DiceRollDefintion] = Field(default=None)
    multiplier: int


def get_coins_from_klass(klass: Klass) -> int:
    klass_coin_definition: Dict[str, KlassCoinDefinition] = {
        Klass.EGENDOMSLOS.value: KlassCoinDefinition(dice=None, multiplier=50),
        Klass.LAGRE_UNDERKLASS.value: KlassCoinDefinition(dice=DICE_1T3, multiplier=50),
        Klass.HOGRE_UNDERKLASS.value: KlassCoinDefinition(dice=DICE_1T3, multiplier=100),
        Klass.LAGRE_MEDELKLASS.value: KlassCoinDefinition(dice=DICE_2T3, multiplier=100),
        Klass.HOGRE_MEDELKLASS.value: KlassCoinDefinition(dice=DICE_3T3, multiplier=100),
        Klass.LAGRE_OVERKLASS.value: KlassCoinDefinition(dice=DICE_3T3, multiplier=200),
        Klass.HOGRE_OVERKLASS.value: KlassCoinDefinition(dice=DICE_3T3, multiplier=300),
        Klass.LAG_ADEL.value: KlassCoinDefinition(dice=DICE_3T3, multiplier=600),
        Klass.HOG_ADEL.value: KlassCoinDefinition(dice=DICE_3T3, multiplier=1500),
    }
    coin_def: KlassCoinDefinition = klass_coin_definition[klass.value]
    if coin_def.dice is None:
        return coin_def.multiplier
    value = roll_dice(coin_def.dice)
    return value * coin_def.multiplier
