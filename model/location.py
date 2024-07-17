from dataclasses import dataclass

@dataclass
class Location:
    Location: str
    Latitude: float
    Longitude: float


    #SEMPRE METTERE SIA STR CHE HASH
    def __str__(self):
        return f"{self.Location}"

    def __hash__(self):
        return hash(self.Location)


