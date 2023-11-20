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
        expected_result = [["o", "o", "o"], ["o", "o", "o"], ["o", "o", "o"]]
        
        self.assertListEqual(actual_result, expected_result)

    def test_cube_back_initialized(self):
        #Tests that the back's face is created
        actual_result = self.cube.back is not None and isinstance(self.cube.back, Face)
        expected_result = True
        
        self.assertEqual(expected_result, actual_result)

    def test_cube_back_populated(self):
        actual_result = self.cube.back.cells
        expected_result = [["r", "r", "r"], ["r", "r", "r"], ["r", "r", "r"]]
        
        self.assertListEqual(actual_result, expected_result)

    def test_cube_left_initialized(self):
        #Tests that the left's face is created
        actual_result = self.cube.left is not None and isinstance(self.cube.left, Face)
        expected_result = True
        
        self.assertEqual(expected_result, actual_result)

    def test_cube_left_populated(self):
        actual_result = self.cube.left.cells
        expected_result = [["g", "g", "g"], ["g", "g", "g"], ["g", "g", "g"]]
        
        self.assertListEqual(actual_result, expected_result)   

    def test_cube_right_initialized(self):
        #Tests that the right's face is created
        actual_result = self.cube.right is not None and isinstance(self.cube.right, Face)
        expected_result = True
        
        self.assertEqual(expected_result, actual_result)

    def test_cube_right_populated(  self):
        actual_result = self.cube.right.cells
        expected_result = [["b", "b", "b"], ["b", "b", "b"], ["b", "b", "b"]]
        
        self.assertListEqual(actual_result, expected_result)  

    def test_cube_top_initialized(self):
        #Tests that the top's face is created
        actual_result = self.cube.top is not None and isinstance(self.cube.top, Face)
        expected_result = True
        
        self.assertEqual(expected_result, actual_result)

    def test_cube_top_populated(self):
        actual_result = self.cube.top.cells
        expected_result = [["y", "y", "y"], ["y", "y", "y"], ["y", "y", "y"]]
        
        self.assertListEqual(actual_result, expected_result)

    def test_cube_bottom_initialized(self):
        #Tests that the bottom's face is created
        actual_result = self.cube.bottom is not None and isinstance(self.cube.bottom, Face)
        expected_result = True
        
        self.assertEqual(expected_result, actual_result)

    def test_cube_bottom_populated(self):
        actual_result = self.cube.bottom.cells
        expected_result = [["w", "w", "w"], ["w", "w", "w"], ["w", "w", "w"]]
        
        self.assertListEqual(actual_result, expected_result) 

    def test_cube_front_back_opposites(self):
        front_color = set(self.cube.front.list_view).pop()
        back_color = set(self.cube.back.list_view).pop()
        
        front_opposite = self.cube.opposites[front_color]
        back_opposite = self.cube.opposites[back_color]

        opposites = front_opposite == back_color and back_opposite == front_color

        self.assertTrue(opposites)

    def test_cube_left_right_opposites(self):
        left_color = set(self.cube.left.list_view).pop()
        right_color = set(self.cube.right.list_view).pop()
        
        left_opposite = self.cube.opposites[left_color]
        right_opposite = self.cube.opposites[right_color]

        opposites = (left_opposite == right_color) and (right_opposite == left_color)

        self.assertTrue(opposites)

    def test_cube_top_bottom_opposites(self):
        top_color = set(self.cube.top.list_view).pop()
        bottom_color = set(self.cube.bottom.list_view).pop()
        
        top_opposite = self.cube.opposites[top_color]
        bottom_opposite = self.cube.opposites[bottom_color]

        opposites = (top_opposite == bottom_color) and (bottom_opposite == top_color)

        self.assertTrue(opposites)

    #endregion Constructor Tests

    #region Cube Display Method Tests

    def test_cube_string_initialized(self):
        actual_result = self.cube.cube_to_string()

        isEmpty = actual_result == ""

        self.assertFalse(isEmpty)


    def test_cube_string_populated(self):

        actual_result = self.cube.cube_to_string()

        expected_result = "Front:\n"
        front = self.cube.front.face_to_string()
        expected_result += front
        expected_result += "\n"

        expected_result += "Back:\n"
        back = self.cube.back.face_to_string()
        expected_result += back
        expected_result += "\n"

        expected_result += "Left:\n"
        left = self.cube.left.face_to_string()
        expected_result += left
        expected_result += "\n"

        expected_result += "Right:\n"
        right = self.cube.right.face_to_string()
        expected_result += right
        expected_result += "\n"

        expected_result += "Top:\n"
        top = self.cube.top.face_to_string()
        expected_result += top
        expected_result += "\n"

        expected_result += "Bottom:\n"
        bottom = self.cube.bottom.face_to_string()
        expected_result += bottom
        expected_result += "\n"

        self.assertEqual(expected_result, actual_result)

    def test_cube_front_to_string(self):

        actual_result = self.cube.face_to_string(0)
        expected_result = self.cube.front.face_to_string()

        self.assertEqual(expected_result, actual_result)

    def test_cube_back_to_string(self):

        actual_result = self.cube.face_to_string(1)
        expected_result = self.cube.back.face_to_string()
        
        self.assertEqual(expected_result, actual_result)

    def test_cube_left_to_string(self):
        
        actual_result = self.cube.face_to_string(2)
        expected_result = self.cube.left.face_to_string()
    
        self.assertEqual(expected_result, actual_result)

    def test_cube_right_to_string(self):

        actual_result = self.cube.face_to_string(3)
        expected_result = self.cube.right.face_to_string()
    
        self.assertEqual(expected_result, actual_result)

    def test_cube_top_to_string(self):

        actual_result = self.cube.face_to_string(4)
        expected_result = self.cube.top.face_to_string()

        self.assertEqual(expected_result, actual_result)

    def test_cube_bottom_to_string(self):

        actual_result = self.cube.face_to_string(5)
        expected_result = self.cube.bottom.face_to_string()

        self.assertEqual(expected_result, actual_result)

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