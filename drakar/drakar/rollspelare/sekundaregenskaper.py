import enum

from pydantic import Field, BaseModel

from drakar.drakar.rollspelare.dice import DiceRollDefintion
from drakar.drakar.rollspelare.grundegenskaper import Grundegenskaper
from drakar.drakar.rollspelare.ras import Ras


class SynTyp(enum.Enum):
    NORMALSYN = "NORMALSYN"
    NATTSYN = "NATTSYN"
    MORKERSYN = "MÖRKERSYN"


RAS_SYN = {
    Ras.MANNISKA.value: SynTyp.NORMALSYN,
    Ras.ALV.value: SynTyp.NATTSYN,
    Ras.DVARG.value: SynTyp.MORKERSYN,
}


class SekundarEgenskaper(BaseModel):
    sb: DiceRollDefintion
    carry: int
    flytta: int
    clb: int = Field(default=0)
    syn: SynTyp = Field(SynTyp.NORMALSYN)
    # im baseras på smidighet
    # ref stritsrunda s. 71
    im: int = Field(default=0)
    # kpmod används vid ökning av kp
    kpmod: int = Field(default=1) # Beräknat fält?
    # om man bär mycket blir man sämre på att röra sig.
    flytta_mod: int = Field(default=1) # Beräknat fält?

    def __init__(self, ge: Grundegenskaper = None, ras: Ras = None, **kwargs):
        if ge:
            kwargs.update(self.se_from_ge(ge))
        if ras:
            kwargs["syn"] = RAS_SYN[ras.value]
        super().__init__(**kwargs)

    def se_from_ge(self, ge: Grundegenskaper) -> dict:
        se_data = {
            "sb": self.get_sb(ge.styrka),
            "carry": ge.styrka,
            "flytta": (ge.smidighet + ge.storlek) / 2,
        }
        if ge.spiritius >= 13:
            se_data["clb"] = int((ge.intelligens + ge.spiritius) / 2)
        return se_data

    def get_sb(self, sty_to: int) -> DiceRollDefintion:
        if sty_to > 90:
            return DiceRollDefintion(throws=7, sides=6)
        if sty_to > 81:
            return DiceRollDefintion(throws=6, sides=6)
        if sty_to > 71:
            return DiceRollDefintion(throws=5, sides=6)
        if sty_to > 61:
            return DiceRollDefintion(throws=4, sides=6)
        if sty_to > 51:
            return DiceRollDefintion(throws=3, sides=6)
        if sty_to > 41:
            return DiceRollDefintion(throws=2, sides=6)
        if sty_to > 31:
            return DiceRollDefintion(throws=1, sides=6)
        if sty_to > 26:
            return DiceRollDefintion(throws=1, sides=3)
        return DiceRollDefintion(throws=0, sides=0)


