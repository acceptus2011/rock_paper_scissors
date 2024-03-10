from unittest import TestCase
from unittest.mock import patch
from game.models import Player
from game.settings import PLAYER_LIVES, MODE_NORMAL, MODE_HARD, PLAYER_LIVES_FOR_MODE_HARD, ALLOWED_ATTACKS
from game.exeptions import IncorrectMode, NegativeOrZeroScore, GameOver


class PlayerInitTest(TestCase):

    def test_init_normal(self):
        player = Player('test_name', MODE_NORMAL)
        self.accertEqual(player.name, 'test_name')
        self.assertEqual(player.lives, PLAYER_LIVES)

    def test_init_hard(self):
        player = Player('test_name', MODE_HARD)
        self.accertEqual(player.name, 'test_name')
        self.assertEqual(player.lives, PLAYER_LIVES_FOR_MODE_HARD)

    def test_init_incorrect_mode(self):
        with self.assertRaises(IncorrectMode):
            Player('test_name', MODE_HARD)
# !
class PlayerSelectAttackTest(TestCase):

    def setUp(self) -> None:
        self.player = Player('test_name', MODE_NORMAL)

    @patch('builtins.input', side_effect = ALLOWED_ATTACKS.keys())
    def test_valid(self, mock_input):
        for allowed_attack_value in ALLOWED_ATTACKS.values():
            self.assertEqual(self.player.select_attack(), allowed_attack_value)

    @patch('builtins.input', side_effect = ['bla', 'qwe', '123', '1'])
    def test_invalid(self, mock_input):
            self.player.select_attack()
            self.assertEqual(mock_input.call_count, 4)

class PlayerAddScoresTest(TestCase):    
        
    def setUp(self) -> None:
        self.player = Player('test_name', MODE_NORMAL)

    def test_valid(self):
        self.player.add_score(10)
        self.assertEqual(self.player.scores, 10)

    def test_negative(self):
        with self.asserRaises(NegativeOrZeroScore):
            self.player.add_score(-10)

        def test_zero(self):
            with self.asserRaises(NegativeOrZeroScore):
                self.player.add_score(0)

class PlayerDecreaseLivesTest(TestCase):    
        
    def setUp(self) -> None:
        self.player = Player('test_name', MODE_NORMAL)

    def test_one_decrease(self):
        self.player.decrease_lives()
        self.assertEqual(self.player.lives, PLAYER_LIVES - 1)

    def test_die(self):
        self.player.decrease_lives()
        self.player.decrease_lives()
        self.player.decrease_lives()
        self.player.decrease_lives()
        self.player.decrease_lives()
        with self.asserRaises(GameOver):
            self.player.add_score(-10)

        def test_zero(self):
            with self.asserRaises(NegativeOrZeroScore):
                self.player.decrease_lives()