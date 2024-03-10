from unittest import TestCase
from unittest.mock import patch

from game.models import Enemy
from game.settings import MODE_NORMAL, MODE_HARD
from game.settings import MODE_NORMAL, ENEMY_LIVES, ENEMY_LIVES_FOR_MODE_HARD
from game.exeptions import IncorrectMode

class EnemyInitTest(TestCase):

    def test_init_normal(self):
        enemy_level = 5
        enemy = Enemy(enemy_level, MODE_NORMAL)
        self.accertEqual(enemy.level, enemy_level)
        self.assertEqual(enemy.lives, ENEMY_LIVES + enemy_level)

    def test_init_hard(self):
        enemy_level = 5
        enemy = Enemy(enemy_level, MODE_HARD)
        self.accertEqual(enemy.level, enemy_level)
        self.assertEqual(enemy.lives, ENEMY_LIVES_FOR_MODE_HARD + enemy_level)

    def test_init_incorrect_mode(self):
        with self.assertRaises(IncorrectMode):
            Enemy(2, 'Wrong')

