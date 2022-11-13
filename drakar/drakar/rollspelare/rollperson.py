from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from drakar.drakar.rollspelare.dice import best_of_set, DiceRollDefintion, roll_dice, \
    DICE_1T20
from drakar.drakar.rollspelare.egenskaper import (
    VapenHand,
    Social,
    Kp,
)
from drakar.drakar.rollspelare.grundegenskaper import Grundegenskaper
from drakar.drakar.rollspelare.ras import Ras, RAS_MOD, get_alders_mod_from_ras_and_age
from drakar.drakar.rollspelare.sekundaregenskaper import (
    SekundarEgenskaper,
)


class RollspelareConfig(BaseModel):
    ras: Optional[Ras] = Field(default=None)
    alder: Optional[int] = Field(default=None)
    ge: Optional[Grundegenskaper] = Field(default=None)


# Steg för att skapa en ny RollPerson
# 1. Slå fram grundegenskaper
# 2. Bestäm ras och lägg till / dra bort från ge
# 3. Bestäm ålder och lägg till / dra bort från ge


class RollPerson:
    _ras: Ras = None
    ge: Grundegenskaper = None
    se: SekundarEgenskaper = None
    _alder: int = 0
    vapen_hand: VapenHand = None
    social: Social = None
    kp: Kp = None

    def __init__(self, config: RollspelareConfig = RollspelareConfig()):
        if not config.ge:
            self._generate_ge()
        if config.ras:
            self._ras = config.ras
            self._apply_ras_mod()
        if config.alder:
            self._alder = config.alder
            self._apply_age_mod()

        self._set_se()
        self.set_random_vapenhand()

    def __repr__(self):
        #noqa
        return f"Rollspelare<{self.ge} {self.se} vapen_hand={self.vapen_hand} alder={self.alder}>"

    def _generate_ge(self):
        t6_3 = DiceRollDefintion(sides=6, throws=3)
        t6_2 = DiceRollDefintion(sides=6, throws=2)
        self.ge = Grundegenskaper(
            styrka=best_of_set(t6_3, 2),
            fysik=best_of_set(t6_3, 2),
            smidighet=best_of_set(t6_3, 2),
            storlek=best_of_set(t6_2, 2),
            intelligens=best_of_set(t6_3, 2),
            perception=best_of_set(t6_3, 2),
            spiritius=best_of_set(t6_3, 2),
            psyke=best_of_set(t6_3, 2),
            karisma=best_of_set(t6_3, 2),
        )

    def set_random_vapenhand(self):
        val = roll_dice(DICE_1T20)
        if val < 15:
            self.vapen_hand = VapenHand.HOGER
        if val < 19:
            self.vapen_hand = VapenHand.VANSTER
        if val == 19:
            self.vapen_hand = VapenHand.DUBBEL
        if val == 20:
            self.vapen_hand = VapenHand.AMBIDEXTER

    def _apply_ras_mod(self):
        ras_mod = RAS_MOD[self.ras.value]
        self._add_to_ge(ras_mod.ge_mod)

    def _remove_ras_mod(self):
        ras_mod = RAS_MOD[self.ras.value]
        self._remove_from_ge(ras_mod.ge_mod)

    def _apply_age_mod(self):
        alders_mod = get_alders_mod_from_ras_and_age(self.alder, self.ras)
        self._add_to_ge(alders_mod)

    def _remove_age_mod(self):
        alders_mod = get_alders_mod_from_ras_and_age(self.alder, self.ras)
        self._remove_from_ge(alders_mod)

    def _add_to_ge(self, ge: Grundegenskaper):
        self.ge.styrka += ge.styrka
        self.ge.fysik += ge.fysik
        self.ge.smidighet += ge.smidighet
        self.ge.storlek += ge.storlek
        self.ge.intelligens += ge.intelligens
        self.ge.perception += ge.perception
        self.ge.spiritius += ge.spiritius
        self.ge.psyke += ge.psyke
        self.ge.karisma += ge.karisma

    def _remove_from_ge(self, ge: Grundegenskaper):
        self.ge.styrka -= ge.styrka
        self.ge.fysik -= ge.fysik
        self.ge.smidighet -= ge.smidighet
        self.ge.storlek -= ge.storlek
        self.ge.intelligens -= ge.intelligens
        self.ge.perception -= ge.perception
        self.ge.spiritius -= ge.spiritius
        self.ge.psyke -= ge.psyke
        self.ge.karisma -= ge.karisma

    def _set_se(self):
        self.se = SekundarEgenskaper(ge=self.ge, ras=self._ras)

    @property
    def ras(self):
        return self._ras or None

    @ras.setter
    def ras(self, ras: Ras):
        if self._ras:
            self._remove_ras_mod()
        self._ras = ras
        self._apply_ras_mod()

    @property
    def alder(self) -> int | None:
        return self._alder or None

    @alder.setter
    def alder(self, alder: int):
        if self._alder:
            self._remove_ras_mod()
        self._alder = alder
        self._apply_age_mod()
