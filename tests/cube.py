#tests/cube.py

import unittest
from unittest.mock import patch
from pyrub.cube import Cube
from pyrub.face import Face

class TestCube(unittest.TestCase):
    """
        Test Case Subclass for testing our Cube methods (Ex. Initialization, Cube and Face Creation, Cube Updates upon calling functions)
    """
