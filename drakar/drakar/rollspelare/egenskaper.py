import enum

from pydantic import BaseModel

from drakar.drakar.rollspelare.dice import DICE_1T20, roll_dice
from drakar.drakar.rollspelare.grundegenskaper import Grundegenskaper


class VapenHand(enum.Enum):
    HOGER = "HÖGER"
    VANSTER = "VÄNSTER"
    DUBBEL = "DUBBEL"
    AMBIDEXTER = "AMIDEXTER"


def set_random_vapenhand() -> VapenHand:
    val = roll_dice(DICE_1T20)
    if val < 15:
        return VapenHand.HOGER
    if val < 19:
        return VapenHand.VANSTER
    if val == 19:
        return VapenHand.DUBBEL
    if val == 20:
        return VapenHand.AMBIDEXTER


class Social(enum.Enum):
    FATTIG = "FATTIG"
    L_UNDERKLASS = "L_UNDERKLASS"
    H_UNDERKLASS = "H_UNDERKLASS"
    L_MEDELKLASS = "L_MEDELKLASS"
    L_OVERKLASS = "L_OVERKLASS"
    H_OVERKLASS = "H_OVERKLASS"
    L_ADEL = "L_ADEL"
    ADEL = "ADEL"
    H_ADEL = "H_ADEL"


class Yrke(enum.Enum):
    KRIGARE = "KRIGARE"
    HELIG_KRIGARE = "HELIG_KRIGARE"
    BESVARJARE = "BESVARJARE"
    PRAST = "PRAST"
    TJUV = "TJUV"
    JAGARE = "JAGARE"
    HANTVERKARE = "HANTVERKARE"
    HANDELSMAN = "HANDELSMAN"
    UTBILDAD = "UTBILDAD"
    BARD = "BARD"


class Kp(BaseModel):
    total: int # (fys + sto + psy) / 2
    h_ben: int # höger ben tot/3
    v_ben: int # vänster ben tot/3
    mage: int # mage tot/3
    torso: int # bröstet tot/2
    huvud: int # huvud tot/4
    h_arm: int # höger arm tot/4
    v_arm: int # vänster arm tot/4


def get_kp(ge: Grundegenskaper) -> Kp:
    total = (ge.fysik + ge.storlek + ge.styrka) / 2
    # fys sto psy, för varje kategori över 15 får spelare +1 kp, vid ökning
    return Kp(
        total=total,
        h_ben=total/3,
        v_ben=total/3,
        mage=total/3,
        torso=total/2,
        huvud=total/4,
        h_arm=total/4,
        v_arm=total/4,
    )
