import unittest
from unittest.mock import patch

from pyrub.cube import Cube
from pyrub.face import Face
from pyrub.game import Game

class TestGame(unittest.TestCase):
    """
        Test Case Subclass for testing our Game methods (Ex. Initialization, Menu Creation, Cube Updates upon selecting menus)
    """ 