from game import settings
from random import randint
from game import exeptions
from game.validations import validate_mode, validate_scores

class Player:
    name: str
    lives: int
    scores: int = 0

    def __init__(self, user_name: str, mode: str) -> None:
        self.name = user_name
        validate_mode(mode)
        if mode == settings.MODE_NORMAL:
            self.lives = settings.PLAYER_LIVES
        else:
            self.lives = settings.PLAYER_LIVES_FOR_MODE_HARD

    def select_attack(self):
        while True:
            try:
                attack = input("Make a move: 1 - Paper or 2 - Stone or 3 - Scissors")
                return settings.ALLOWED_ATTACKS[attack]
            except KeyError:
                print("Incorrect move entered")

    def add_score(self, scores: int) -> None:
        validate_scores(scores)
        self.scores += scores
        
    def decrease_lives(self) -> None:
        self.lives -= 1
        if self.lives == 0:
            raise exeptions.GameOver
        

class Enemy:
    def __init__(self, enemy_level: int, mode: str) -> None:
        self.level = enemy_level
        validate_mode(mode)
        if mode == settings.MODE_NORMAL:
            self.lives = settings.ENEMY_LIVES + enemy_level
        else:
            self.lives = settings.ENEMY_LIVES_FOR_MODE_HARD + enemy_level

    def select_attack(self):
        return settings.ALLOWED_ATTACKS[str(randint(1, 3))]
    
    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise exeptions.EnemyDown