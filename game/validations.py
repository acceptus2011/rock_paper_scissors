from game.settings import MODES
from game.exeptions import IncorrectMode, NegativeOrZeroScore

def validate_mode(mode: str) -> None:
    if mode not in MODES.values():
        raise IncorrectMode
    
def validate_scores(scores: int) -> None:
    if scores <= 0:
        raise NegativeOrZeroScore