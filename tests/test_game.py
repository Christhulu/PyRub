import unittest
from unittest.mock import patch

from pyrub import cube
from cube import Cube

from pyrub import face
from face import Face

from pyrub import game
from game import Game
class TestGame(unittest.TestCase):
    """
        Test Case Subclass for testing our Game methods (Ex. Initialization, Menu Creation, Cube Updates upon selecting menus)
    """ 