from dataclasses import dataclass

@dataclass
class Airport:
    IATA_code: str
    Name: str
    City: str
    State: str
    Delay: bool
    Temperature: int
