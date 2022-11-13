import enum
from typing import List

from drakar.drakar.rollspelare.grundegenskaper import Grundegenskaper
from pydantic import BaseModel


class Ras(enum.Enum):
    MANNISKA = "MANNISKA"
    ALV = "ALV"
    DVARG = "DVARG"
    HALVLANGSMAN = "HALVLANGSMAN"
    HALVALV = "HALVALV"
    TROLL = "TROLL"
    HALVTROLL = "HALVTROLL"
    ANKA = "ANKA"
    KENTAUR = "KENTAUR"


class AldersTyp(enum.Enum):
    UNG = "UNG"
    MOGEN = "MOGEN"
    VUXEN = "VUXEN"
    MEDELALDERS = "MEDELÅLDERS"
    GAMMAL = "GAMMAL"


class AlderRange(BaseModel):
    typ: AldersTyp
    alder_from: int
    alder_to: int


class RasMod(BaseModel):
    ge_mod: Grundegenskaper
    alder_range: List[AlderRange]


RAS_MOD = {
    Ras.MANNISKA.value: RasMod(
        ge_mod=Grundegenskaper(
            storlek=6,
        ),
        alder_range=[
            AlderRange(typ=AldersTyp.UNG, alder_from=13, alder_to=18),
            AlderRange(typ=AldersTyp.MOGEN, alder_from=19, alder_to=25),
            AlderRange(typ=AldersTyp.VUXEN, alder_from=26, alder_to=40),
            AlderRange(typ=AldersTyp.MEDELALDERS, alder_from=41, alder_to=60),
            AlderRange(typ=AldersTyp.GAMMAL, alder_from=61, alder_to=100),
        ]
    ),
    Ras.ALV.value: RasMod(
        ge_mod=Grundegenskaper(
            storlek=4,
            styrka=1,
            smidighet=-3,
            perception=1,
            spiritius=1,
            karisma=1,
        ),
        alder_range=[
            AlderRange(typ=AldersTyp.UNG, alder_from=13, alder_to=60),
            AlderRange(typ=AldersTyp.MOGEN, alder_from=61, alder_to=100),
            AlderRange(typ=AldersTyp.VUXEN, alder_from=101, alder_to=150),
            AlderRange(typ=AldersTyp.MEDELALDERS, alder_from=151, alder_to=210),
            AlderRange(typ=AldersTyp.GAMMAL, alder_from=211, alder_to=300),
        ]
    ),
    Ras.DVARG.value: RasMod(
        ge_mod=Grundegenskaper(
            styrka=1,
            fysik=4,
            smidighet=-3,
            storlek=1,
            psyke=1,
        ),
        alder_range=[
            AlderRange(typ=AldersTyp.UNG, alder_from=13, alder_to=50),
            AlderRange(typ=AldersTyp.MOGEN, alder_from=51, alder_to=80),
            AlderRange(typ=AldersTyp.VUXEN, alder_from=81, alder_to=125),
            AlderRange(typ=AldersTyp.MEDELALDERS, alder_from=126, alder_to=175),
            AlderRange(typ=AldersTyp.GAMMAL, alder_from=176, alder_to=250),
        ]
    )

}

ALDER_MOD = {
    AldersTyp.UNG.value: Grundegenskaper(
        styrka=-2,
        fysik=-1,
        storlek=-1,
        psyke=-1,
        karisma=-1,
    ),
    AldersTyp.MOGEN.value: Grundegenskaper(),
    AldersTyp.VUXEN.value: Grundegenskaper(),
    AldersTyp.MEDELALDERS: Grundegenskaper(
        styrka=-2,
        fysik=-1,
        smidighet=-1,
        perception=-1,
    ),
    AldersTyp.GAMMAL: Grundegenskaper(
        styrka=-5,
        fysik=-4,
        storlek=-1,
        smidighet=-4,
        perception=-3,
    ),
}


def get_alders_mod_from_ras_and_age(age: int, ras: Ras) -> Grundegenskaper:
    alder_range = RAS_MOD[ras.value].alder_range
    alders_typ = match_adlers_typ(age, alder_range)
    return ALDER_MOD[alders_typ.value]


def match_adlers_typ(age: int, alder_range: List[AlderRange]) -> AldersTyp:
    for a_rng in alder_range:
        if a_rng.alder_from < age < a_rng.alder_to:
            return a_rng.typ
