from typing import Optional

from pydantic import BaseModel, Field

from drakar.drakar.person.egenskaper import VapenHand
from drakar.drakar.person.grundegenskaper import Grundegenskaper
from drakar.drakar.person.klass import Klass
from drakar.drakar.person.ras import Ras


# Steg för att skapa en ny Person:
# 1. Slå fram grundegenskaper
# 2. Bestäm ras och lägg till / dra bort från ge
# 3. Bestäm ålder och lägg till / dra bort från ge
# 4. Vapenhand
# 5. Socialt stånd
# 6. Yrke
# 7. Bakgrund historia personlighet
# 8. Kropspoäng
# 9. Stridskapacitet
# 10. Sk-grund
# 14. Färdighetspoäng
# 15. Färdigheter utifrån yrke/bakgrund
# 16.


class Person(BaseModel):
    ge: Optional[Grundegenskaper] = Field(default=None)
    ras: Optional[Ras] = Field(default=None)
    alder: Optional[int] = Field(default=None)
    klass: Optional[Klass] = Field(default=None)
    sm: Optional[int] = Field(default=0)

