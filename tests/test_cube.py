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

        actual_result = self.cube is not None and isinstance(self.cube, Cube)
        expected_result = True

        self.assertEqual(expected_result, actual_result)

    def test_cube_dimensions(self):
        actual_result = self.cube.side_length
        expected_result = 3

        self.assertEqual(expected_result, actual_result)

    def test_cube_opposites_populated(self):

        actual_result = len(self.cube.opposites) > 0
        expected_result = True
        
        self.assertEqual(expected_result, actual_result)

    def test_cube_front_initialized(self):
        #Tests that the front's face is created
        actual_result = self.cube.front is not None and isinstance(self.cube.front, Face)
        expected_result = True
        
        self.assertEqual(expected_result, actual_result)
    
    def test_cube_front_populated(self):
        #Tests that the front face's cells are correctly set
        actual_result = self.cube.front.cells
        expected_result = [["", "", ""], ["", "", ""], ["", "", ""]]
        
        self.assertListEqual(actual_result, expected_result)

    def test_cube_back_initialized(self):
        pass

    def test_cube_back_populated(self):
        actual_result = self.cube.front.cells
        expected_result = [["", "", ""], ["", "", ""], ["", "", ""]]
        
        self.assertListEqual(actual_result, expected_result)

    def test_cube_left_initialized(self):
        pass

    def test_cube_left_populated(self):
        actual_result = self.cube.front.cells
        expected_result = [["", "", ""], ["", "", ""], ["", "", ""]]
        
        self.assertListEqual(actual_result, expected_result)   

    def test_cube_right_initialized(self):
        pass

    def test_cube_right_populated(self):
        actual_result = self.cube.right.cells
        expected_result = [["", "", ""], ["", "", ""], ["", "", ""]]
        
        self.assertListEqual(actual_result, expected_result)  

    def test_cube_top_initialized(self):
        pass

    def test_cube_top_populated(self):
        actual_result = self.cube.top.cells
        expected_result = [["", "", ""], ["", "", ""], ["", "", ""]]
        
        self.assertListEqual(actual_result, expected_result)

    def test_cube_bottom_initialized(self):
        pass

    def test_cube_bottom_populated(self):
        actual_result = self.cube.bottom.cells
        expected_result = [["", "", ""], ["", "", ""], ["", "", ""]]
        
        self.assertListEqual(actual_result, expected_result) 

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