#tests/cube.py

import unittest
from unittest.mock import patch

from pyrub.face import Face
from pyrub.cube import Cube

class TestCube(unittest.TestCase):
    """
        Test Case Subclass for testing our Cube methods (Ex. Initialization, Cube and Face Creation, Cube Updates upon calling functions)
    """

    #region Setup for Testing
    @classmethod
    def setUp(self) -> None:
        self.cube = Cube()

    @classmethod
    def tearDown(self) -> None:
        self.cube = None
        del self.cube

    #endregion Setup for Testing


    #region Constructor Tests
    def test_cube_created(self):
        pass

    def test_cube_dimensions(self):
        pass

    def test_cube_opposites_set(self):
        pass

    def test_cube_front_set(self):
        pass

    def test_cube_back_set(self):
        pass

    def test_cube_left_set(self):
        pass

    def test_cube_right_set(self):
        pass

    def test_cube_top_set(self):
        pass

    def test_cube_bottom_set(self):
        pass

    def test_cube_front_back_opposites(self):
        pass

    def test_cube_left_right_opposites(self):
        pass


    #endregion Constructor Tests

    #region Cube Display Method Tests

    #endregion Cube Display Method Tests

    #region Cube Completeness Tests


    #endregion Cube Completeness Tests

    #region Rotation Tests

    #region Row Operation Tests

    #region Top Row Rotation Tests

    #endregion Top Row Rotation Tests

    #region Middle Row Rotation Tests
    #endregion Middle Row Rotation Tests

    #region Bottom Row Rotation Tests

    #endregion Bottom Row Rotation Tests

    #endregion Row Operation Tests

    #region Column Operation Tests

    #region Left Column Rotation Tests

    #endregion Left Column Rotation Tests

    #region Middle Column Rotation Tests

    #endregion Middle Column Rotation Tests

    #region Right Column Rotation Tests
    #endregion Right Column Rotation Tests

    #endregion Column Operation Tests

    #region Face Operation Tests

    #region Top Face Rotation Tests

    #endregion Top Face Rotation Tests

    #region Left Face Rotation Tests
    
    #endregion Left Face Rotation Tests

    #region Right Face Rotation Tests

    #endregion Right Face Rotation Tests

    #region Top Face Rotation Tests

    #endregion Top Face Rotation Tests

    #region Bottom Face Rotation Tests

    #endregion Bottom Face Rotation Tests

    #region Middle Face Rotation Tests

    #endregion Middle Face Rotation Tests

    #region Back Face Rotation Tests

    #endregion Face Operation Tests

    #endregion Face Operation Tests

    #endregion Rotation Tests

    #region Cube Helper Method Tests

    #endregion Cube Helper Method Tests

    #region Cube Orientation Shift Tests

    #endregion Cube Orientation Shift Tests