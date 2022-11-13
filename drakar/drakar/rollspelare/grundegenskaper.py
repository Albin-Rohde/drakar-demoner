from pydantic import BaseModel, Field


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
