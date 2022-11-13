# hur en karaktär skapas

# rollforumulär
# grundegenskaper

# Styrka
# Fysik
# Smidi
# Storlek
# Intelligens
# Psykisk kraft
# Smidighet
# Karisma



# Rulla T18


from pydantic import BaseModel



class Grundegenskaper():
    styrka: int
    fysik: int
    smidighet: int
    storlek: int
    intelligens: int
    perception: int
    psyke: int
    spiritius: int
    karisma: int




class Rollspelare(BaseModel):
    grundegenskaper: Grundegenskaper


