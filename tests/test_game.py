import unittest
from unittest.mock import patch

from pyrub.cube import Cube
from pyrub.face import Face
from pyrub.game import Game

class TestGame(unittest.TestCase):
    """
        Test Case Subclass for testing our Game methods (Ex. Initialization, Menu Creation, Cube Updates upon selecting menus)
    """ 
    #region Setup for Testing
    @classmethod
    def setUp(self) -> None:
        self.cube_game = Game()

    @classmethod
    def tearDown(self) -> None:
        self.cube_game = None
        del self.cube_game

    #endregion Setup for Testing

    #region Constructor Tests
    def test_game_created(self):

        actual_result = self.cube_game is not None and isinstance(self.cube_game, Game)
        expected_result = True

        self.assertEqual(expected_result, actual_result)
    
    #endregion Constructor Tests