from game import settings

class PlayerRecord:

    def __init__(self, name: str, mode: str, score: int) -> None:
        self.name = name
        self.mode = mode
        self.score = score

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.mode == other.mode
    
    def __gt__(self, other) -> bool:
        return self.score > other.score
    
    def __str__(self) -> str:
        return f"{self.name} {self.mode} {self.score}"