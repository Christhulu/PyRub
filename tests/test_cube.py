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

    def test_cube_methods_list_populated(self):

        self.cube.randomize_cube()

        expected_result = 26
        actual_result = len(self.cube.methods)

        self.assertEqual(expected_result, actual_result)

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
    def test_cube_complete(self):
        #Maybe test it based on initially
        #Then test it based on some rotations
        pass

    def test_cube_incomplete(self):
        pass

    #endregion Cube Completeness Tests

    #region Rotation Tests

    #region Row Operation Tests

    #region Top Row Rotation Tests
    def test_front_face_valid_after_top_row_rotates_left(self):

        self.cube.rotate_top_row_left()

        expected_result = [["b", "b", "b"],["o","o","o"],["o","o","o"]]
        actual_result = self.cube.front.cells

        self.assertListEqual(expected_result, actual_result)

    def test_back_face_valid_after_top_row_rotates_left(self):

        self.cube.rotate_top_row_left()

        expected_result = [["g", "g", "g"],["r","r","r"],["r","r","r"]]
        actual_result = self.cube.back.cells

        self.assertListEqual(expected_result, actual_result)

    def test_left_face_valid_after_top_row_rotates_left(self):
        self.cube.rotate_top_row_left()

        expected_result = [["o", "o", "o"],["g","g","g"],["g","g","g"]]
        actual_result = self.cube.left.cells

        self.assertListEqual(expected_result, actual_result)

    def test_top_face_valid_after_top_row_rotates_left(self):
        self.cube.rotate_top_row_left()

        expected_result = [["y", "y", "y"],["y","y","y"],["y","y","y"]]
        actual_result = self.cube.top.cells

        self.assertListEqual(expected_result, actual_result)

    def test_bottom_face_valid_after_top_row_rotates_left(self):
        self.cube.rotate_top_row_left()

        expected_result = [["w", "w", "w"],["w","w","w"],["w","w","w"]]
        actual_result = self.cube.bottom.cells

        self.assertListEqual(expected_result, actual_result)         

    def test_front_face_valid_after_top_row_rotates_right(self):
        self.cube.rotate_top_row_right()

        expected_result = [["g","g","g"], ["o","o","o"], ["o","o","o"]]

        actual_result = self.cube.front.cells
        self.assertListEqual(expected_result, actual_result)   

    def test_back_face_valid_after_top_row_rotates_right(self):
        self.cube.rotate_top_row_right()
        expected_result = [["b","b","b"], ["r","r","r"], ["r","r","r"]]

        actual_result = self.cube.back.cells
        self.assertListEqual(expected_result, actual_result)     

    def test_left_face_valid_after_top_row_rotates_right(self):
        self.cube.rotate_top_row_right()
        expected_result = [["r","r","r"], ["g","g","g"], ["g","g","g"]]

        actual_result = self.cube.left.cells
        self.assertListEqual(expected_result, actual_result)   

    def test_right_face_valid_after_top_row_rotates_right(self):
        self.cube.rotate_top_row_right()
        expected_result = [["o","o","o"], ["b","b","b"], ["b","b","b"]]

        actual_result = self.cube.right.cells
        self.assertListEqual(expected_result, actual_result)    

    def test_top_face_valid_after_top_row_rotates_right(self):
        self.cube.rotate_top_row_right()
        expected_result = [["y","y","y"], ["y","y","y"], ["y","y","y"]]

        actual_result = self.cube.top.cells
        self.assertListEqual(expected_result, actual_result)      

    def test_bottom_face_valid_after_top_row_rotates_right(self):
        self.cube.rotate_top_row_right()
        expected_result = [["w","w","w"], ["w","w","w"], ["w","w","w"]]

        actual_result = self.cube.bottom.cells
        self.assertListEqual(expected_result, actual_result)          

    #endregion Top Row Rotation Tests

    #region Middle Row Rotation Tests

    def test_front_face_valid_after_middle_row_rotates_left(self):

        self.cube.rotate_middle_row_left()

        expected_result = [["o", "o", "o"],["b","b","b"],["o","o","o"]]
        actual_result = self.cube.front.cells

        self.assertListEqual(expected_result, actual_result)

    def test_back_face_valid_after_middle_row_rotates_left(self):

        self.cube.rotate_middle_row_left()

        expected_result = [["r", "r", "r"],["g","g","g"],["r","r","r"]]
        actual_result = self.cube.back.cells

        self.assertListEqual(expected_result, actual_result)

    def test_left_face_valid_after_middle_row_rotates_left(self):

        self.cube.rotate_middle_row_left()

        expected_result = [["g", "g", "g"],["o","o","o"],["g","g","g"]]
        actual_result = self.cube.left.cells

        self.assertListEqual(expected_result, actual_result)

    def test_right_face_valid_after_middle_row_rotates_left(self):

        self.cube.rotate_middle_row_left()

        expected_result = [["b", "b", "b"],["r","r","r"],["b","b","b"]]
        actual_result = self.cube.right.cells

        self.assertListEqual(expected_result, actual_result)        

    def test_top_face_valid_after_middle_row_rotates_left(self):

        self.cube.rotate_middle_row_left()

        expected_result = [["y", "y", "y"],["y","y","y"],["y","y","y"]]
        actual_result = self.cube.top.cells

        self.assertListEqual(expected_result, actual_result)

    def test_bottom_face_valid_after_middle_row_rotates_left(self):

        self.cube.rotate_middle_row_left()

        expected_result = [["w", "w", "w"],["w","w","w"],["w","w","w"]]
        actual_result = self.cube.bottom.cells

        self.assertListEqual(expected_result, actual_result)


    def test_front_face_valid_after_middle_row_rotates_right(self):

        self.cube.rotate_middle_row_right()

        expected_result = [["o", "o", "o"],["g","g","g"],["o","o","o"]]
        actual_result = self.cube.front.cells

        self.assertListEqual(expected_result, actual_result)

    def test_back_face_valid_after_middle_row_rotates_right(self):

        self.cube.rotate_middle_row_right()

        expected_result = [["r", "r", "r"],["b","b","b"],["r","r","r"]]
        actual_result = self.cube.back.cells

        self.assertListEqual(expected_result, actual_result)        

    def test_left_face_valid_after_middle_row_rotates_right(self):

        self.cube.rotate_middle_row_right()

        expected_result = [["g", "g", "g"],["r","r","r"],["g","g","g"]]
        actual_result = self.cube.left.cells

        self.assertListEqual(expected_result, actual_result)

    def test_right_face_valid_after_middle_row_rotates_right(self):

        self.cube.rotate_middle_row_right()

        expected_result = [["b", "b", "b"],["o","o","o"],["b","b","b"]]
        actual_result = self.cube.right.cells

        self.assertListEqual(expected_result, actual_result)

    def test_top_face_valid_after_middle_row_rotates_right(self):

        self.cube.rotate_middle_row_right()

        expected_result = [["y", "y", "y"],["y","y","y"],["y","y","y"]]
        actual_result = self.cube.top.cells

        self.assertListEqual(expected_result, actual_result)

    def test_bottom_face_valid_after_middle_row_rotates_right(self):

        self.cube.rotate_middle_row_right()

        expected_result = [["w", "w", "w"],["w","w","w"],["w","w","w"]]
        actual_result = self.cube.bottom.cells

        self.assertListEqual(expected_result, actual_result)

    #endregion Middle Row Rotation Tests

    #region Bottom Row Rotation Tests
    def test_front_face_valid_after_bottom_row_rotates_left(self):

        self.cube.rotate_bottom_row_left()

        expected_result = [["o", "o", "o"],["o","o","o"],["b","b","b"]]
        actual_result = self.cube.front.cells

        self.assertListEqual(expected_result, actual_result)

    def test_back_face_valid_after_bottom_row_rotates_left(self):

        self.cube.rotate_bottom_row_left()

        expected_result = [["r", "r", "r"],["r","r","r"],["g","g","g"]]
        actual_result = self.cube.back.cells

        self.assertListEqual(expected_result, actual_result)

    def test_left_face_valid_after_bottom_row_rotates_left(self):

        self.cube.rotate_bottom_row_left()

        expected_result = [["g", "g", "g"],["g","g","g"],["o","o","o"]]
        actual_result = self.cube.left.cells

        self.assertListEqual(expected_result, actual_result)    

    def test_right_face_valid_after_bottom_row_rotates_left(self):

        self.cube.rotate_bottom_row_left()

        expected_result = [["b", "b", "b"],["b","b","b"],["r","r","r"]]
        actual_result = self.cube.right.cells

        self.assertListEqual(expected_result, actual_result)            

    def test_top_face_valid_after_bottom_row_rotates_left(self):

        self.cube.rotate_bottom_row_left()

        expected_result = [["y", "y", "y"],["y","y","y"],["y","y","y"]]
        actual_result = self.cube.top.cells

        self.assertListEqual(expected_result, actual_result)

    def test_bottom_face_valid_after_bottom_row_rotates_left(self):

        self.cube.rotate_bottom_row_left()

        expected_result = [["w", "w", "w"],["w","w","w"],["w","w","w"]]
        actual_result = self.cube.bottom.cells

        self.assertListEqual(expected_result, actual_result)                   

    def test_front_face_valid_after_bottom_row_rotates_right(self):

        self.cube.rotate_bottom_row_right()

        expected_result = [["o", "o", "o"],["o","o","o"],["g","g","g"]]
        actual_result = self.cube.front.cells

        self.assertListEqual(expected_result, actual_result)

    def test_back_face_valid_after_bottom_row_rotates_right(self):

        self.cube.rotate_bottom_row_right()

        expected_result = [["r", "r", "r"],["r","r","r"],["b","b","b"]]
        actual_result = self.cube.back.cells

        self.assertListEqual(expected_result, actual_result)

    def test_left_face_valid_after_bottom_row_rotates_right(self):

        self.cube.rotate_bottom_row_right()

        expected_result = [["g", "g", "g"],["g","g","g"],["r","r","r"]]
        actual_result = self.cube.left.cells

        self.assertListEqual(expected_result, actual_result)

    def test_right_face_valid_after_bottom_row_rotates_right(self):

        self.cube.rotate_bottom_row_right()

        expected_result = [["b", "b", "b"],["b","b","b"],["o","o","o"]]
        actual_result = self.cube.right.cells

        self.assertListEqual(expected_result, actual_result)

    def test_top_face_valid_after_bottom_row_rotates_right(self):

        self.cube.rotate_bottom_row_right()

        expected_result = [["y", "y", "y"],["y","y","y"],["y","y","y"]]
        actual_result = self.cube.top.cells

        self.assertListEqual(expected_result, actual_result)

    def test_bottom_face_valid_after_bottom_row_rotates_right(self):

        self.cube.rotate_bottom_row_right()

        expected_result = [["w", "w", "w"],["w","w","w"],["w","w","w"]]
        actual_result = self.cube.bottom.cells

        self.assertListEqual(expected_result, actual_result)

    #endregion Bottom Row Rotation Tests

    #endregion Row Operation Tests

    #region Column Operation Tests

    #region Left Column Rotation Tests

    def test_front_face_valid_after_left_column_rotates_up(self):

        self.cube.rotate_left_column_up()

        expected_result = [["w", "o", "o"],["w","o","o"],["w","o","o"]]
        actual_result = self.cube.front.cells

        self.assertListEqual(expected_result, actual_result)

    def test_back_face_valid_after_left_column_rotates_up(self):

        self.cube.rotate_left_column_up()

        expected_result = [["r", "r", "y"],["r","r","y"],["r","r","y"]]
        actual_result = self.cube.back.cells

        self.assertListEqual(expected_result, actual_result)

    def test_left_face_valid_after_left_column_rotates_up(self):

        self.cube.rotate_left_column_up()

        expected_result = [["g", "g", "g"],["g","g","g"],["g","g","g"]]
        actual_result = self.cube.left.cells

        self.assertListEqual(expected_result, actual_result)

    def test_right_face_valid_after_left_column_rotates_up(self):

        self.cube.rotate_left_column_up()

        expected_result = [["b", "b", "b"],["b","b","b"],["b","b","b"]]
        actual_result = self.cube.right.cells

        self.assertListEqual(expected_result, actual_result)

    def test_top_face_valid_after_left_column_rotates_up(self):

        self.cube.rotate_left_column_up()

        expected_result = [["o", "y", "y"],["o","y","y"],["o","y","y"]]
        actual_result = self.cube.top.cells

        self.assertListEqual(expected_result, actual_result)

    def test_bottom_face_valid_after_left_column_rotates_up(self):

        self.cube.rotate_left_column_up()

        expected_result = [["r", "w", "w"],["r","w","w"],["r","w","w"]]
        actual_result = self.cube.bottom.cells

        self.assertListEqual(expected_result, actual_result)

    def test_front_face_valid_after_left_column_rotates_down(self):

        self.cube.rotate_left_column_down()

        expected_result = [["y", "o", "o"],["y","o","o"],["y","o","o"]]
        actual_result = self.cube.front.cells

        self.assertListEqual(expected_result, actual_result)

    def test_back_face_valid_after_left_column_rotates_down(self):

        self.cube.rotate_left_column_down()

        expected_result = [["r", "r", "w"],["r","r","w"],["r","r","w"]]
        actual_result = self.cube.back.cells

        self.assertListEqual(expected_result, actual_result)

    def test_left_face_valid_after_left_column_rotates_down(self):

        self.cube.rotate_left_column_down()

        expected_result = [["g", "g", "g"],["g","g","g"],["g","g","g"]]
        actual_result = self.cube.left.cells

        self.assertListEqual(expected_result, actual_result)

    def test_right_face_valid_after_left_column_rotates_down(self):

        self.cube.rotate_left_column_down()

        expected_result = [["b", "b", "b"],["b","b","b"],["b","b","b"]]
        actual_result = self.cube.right.cells

        self.assertListEqual(expected_result, actual_result)

    def test_top_face_valid_after_left_column_rotates_down(self):

        self.cube.rotate_left_column_down()

        expected_result = [["r", "y", "y"],["r","y","y"],["r","y","y"]]
        actual_result = self.cube.top.cells

        self.assertListEqual(expected_result, actual_result)

    def test_bottom_face_valid_after_left_column_rotates_down(self):

        self.cube.rotate_left_column_down()

        expected_result = [["o", "w", "w"],["o","w","w"],["o","w","w"]]
        actual_result = self.cube.bottom.cells

        self.assertListEqual(expected_result, actual_result)

    #endregion Left Column Rotation Tests

    #region Middle Column Rotation Tests
    def test_front_face_valid_after_middle_column_rotates_up(self):

        self.cube.rotate_middle_column_up()

        expected_result = [["o","w","o"],["o","w","o"],["o","w","o"]]
        actual_result = self.cube.front.cells

        self.assertListEqual(expected_result, actual_result)

    def test_back_face_valid_after_middle_column_rotates_up(self):

        self.cube.rotate_middle_column_up()

        expected_result = [["r","y","r"],["r","y","r"],["r","y","r"]]
        actual_result = self.cube.back.cells

        self.assertListEqual(expected_result, actual_result)


    def test_left_face_valid_after_middle_column_rotates_up(self):
        self.cube.rotate_middle_column_up()

        expected_result = [["g","g","g"],["g","g","g"],["g","g","g"]]
        actual_result = self.cube.left.cells

        self.assertListEqual(expected_result, actual_result)

    def test_right_face_valid_after_middle_column_rotates_up(self):
        self.cube.rotate_middle_column_up()

        expected_result = [["b","b","b"],["b","b","b"],["b","b","b"]]
        actual_result = self.cube.right.cells

        self.assertListEqual(expected_result, actual_result)

    def test_top_face_valid_after_middle_column_rotates_up(self):
        self.cube.rotate_middle_column_up()

        expected_result = [["y","o","y"],["y","o","y"],["y","o","y"]]
        actual_result = self.cube.top.cells

        self.assertListEqual(expected_result, actual_result)

    def test_bottom_face_valid_after_middle_column_rotates_up(self):
        self.cube.rotate_middle_column_up()

        expected_result = [["w","r","w"],["w","r","w"],["w","r","w"]]
        actual_result = self.cube.bottom.cells

        self.assertListEqual(expected_result, actual_result)

    def test_front_face_valid_after_middle_column_rotates_down(self):
        self.cube.rotate_middle_column_down()

        expected_result = [["o", "y", "o"],["o", "y", "o"],["o", "y", "o"]]
        actual_result = self.cube.front.cells
        
        self.assertListEqual(expected_result, actual_result)

    def test_back_face_valid_after_middle_column_rotates_down(self):
        self.cube.rotate_middle_column_down()

        expected_result = [["r", "w", "r"],["r", "w", "r"],["r", "w", "r"]]
        actual_result = self.cube.back.cells
        
        self.assertListEqual(expected_result, actual_result)

    def test_left_face_valid_after_middle_column_rotates_down(self):
        self.cube.rotate_middle_column_down()
        
        expected_result = [["g","g","g"],["g","g","g"],["g","g","g"]]
        actual_result = self.cube.left.cells

        self.assertListEqual(expected_result, actual_result)

    def test_right_face_valid_after_middle_column_rotates_down(self):
        self.cube.rotate_middle_column_down()

        expected_result = [["b","b","b"],["b","b","b"],["b","b","b"]]
        actual_result = self.cube.right.cells

        self.assertListEqual(expected_result, actual_result)

    def test_top_face_valid_after_middle_column_rotates_down(self):
        self.cube.rotate_middle_column_down()

        expected_result = [["y","r","y"],["y","r","y"],["y","r","y"]]
        actual_result = self.cube.top.cells

        self.assertListEqual(expected_result, actual_result)        

    def test_bottom_face_valid_after_middle_column_rotates_down(self):
        self.cube.rotate_middle_column_down()

        expected_result = [["w","o","w"],["w","o","w"],["w","o","w"]]
        actual_result = self.cube.bottom.cells

        self.assertListEqual(expected_result, actual_result)    

    #endregion Middle Column Rotation Tests

    #region Right Column Rotation Tests
    def test_front_face_valid_after_right_column_rotates_up(self):
        self.cube.rotate_right_column_up()

        expected_result = [["o","o","w"],["o","o","w"],["o","o","w"]]
        actual_result = self.cube.front.cells

        self.assertListEqual(expected_result, actual_result)    

    def test_back_face_valid_after_right_column_rotates_up(self):
        self.cube.rotate_right_column_up()

        expected_result = [["y","r","r"],["y","r","r"],["y","r","r"]]
        actual_result = self.cube.back.cells

        self.assertListEqual(expected_result, actual_result) 

    def test_left_face_valid_after_right_column_rotates_up(self):
        self.cube.rotate_right_column_up()

        expected_result = [["g","g","g"],["g","g","g"],["g","g","g"]]
        actual_result = self.cube.left.cells

        self.assertListEqual(expected_result, actual_result) 

    def test_right_face_valid_after_right_column_rotates_up(self):
        self.cube.rotate_right_column_up()

        expected_result = [["b","b","b"],["b","b","b"],["b","b","b"]]
        actual_result = self.cube.right.cells

        self.assertListEqual(expected_result, actual_result) 

    def test_top_face_valid_after_right_column_rotates_up(self):
        self.cube.rotate_right_column_up()

        expected_result = [["y","y","o"],["y","y","o"],["y","y","o"]]
        actual_result = self.cube.top.cells

        self.assertListEqual(expected_result, actual_result) 

    def test_bottom_face_valid_after_right_column_rotates_up(self):
        self.cube.rotate_right_column_up()

        expected_result = [["w","w","r"],["w","w","r"],["w","w","r"]]
        actual_result = self.cube.bottom.cells

        self.assertListEqual(expected_result, actual_result) 

    def test_front_face_valid_after_right_column_rotates_down(self):
        self.cube.rotate_right_column_down()

        expected_result = [["o","o","y"],["o","o","y"],["o","o","y"]]
        actual_result = self.cube.front.cells

        self.assertListEqual(expected_result, actual_result)         

    def test_back_face_valid_after_right_column_rotates_down(self):
        self.cube.rotate_right_column_down()

        expected_result = [["w","r","r"],["w","r","r"],["w","r","r"]]
        actual_result = self.cube.back.cells

        self.assertListEqual(expected_result, actual_result)  

    def test_left_face_valid_after_right_column_rotates_down(self):
        self.cube.rotate_right_column_down()

        expected_result = [["g","g","g"],["g","g","g"],["g","g","g"]]
        actual_result = self.cube.left.cells

        self.assertListEqual(expected_result, actual_result)  

    def test_right_face_valid_after_right_column_rotates_down(self):
        self.cube.rotate_right_column_down()

        expected_result = [["b","b","b"],["b","b","b"],["b","b","b"]]
        actual_result = self.cube.right.cells

        self.assertListEqual(expected_result, actual_result)  

    def test_top_face_valid_after_right_column_rotates_down(self):
        self.cube.rotate_right_column_down()

        expected_result = [["y","y","r"],["y","y","r"],["y","y","r"]]
        actual_result = self.cube.top.cells

        self.assertListEqual(expected_result, actual_result) 

    def test_bottom_face_valid_after_right_column_rotates_down(self):
        self.cube.rotate_right_column_down()

        expected_result = [["w","w","o"],["w","w","o"],["w","w","o"]]
        actual_result = self.cube.bottom.cells

        self.assertListEqual(expected_result, actual_result) 

    #endregion Right Column Rotation Tests

    #endregion Column Operation Tests

    #region Face Operation Tests
    
    #region Front Face Rotation Tests
    def test_front_face_valid_after_front_face_rotates_counter_clockwise(self):

        self.cube.rotate_front_face_CCW()

        expected_result = [["o","o","o"],["o","o","o"],["o","o","o"]]
        actual_result = self.cube.front.cells

        self.assertListEqual(expected_result, actual_result)

    def test_back_face_valid_after_front_face_rotates_counter_clockwise(self):
        self.cube.rotate_front_face_CCW()
        
        expected_result = [["r","r","r"],["r","r","r"],["r","r","r"]]
        actual_result = self.cube.back.cells

        self.assertListEqual(expected_result, actual_result)

    def test_left_face_valid_after_front_face_rotates_counter_clockwise(self):

        self.cube.rotate_front_face_CCW()
        
        expected_result = [["g","g","y"],["g","g","y"],["g","g","y"]]
        actual_result = self.cube.left.cells

        self.assertListEqual(expected_result, actual_result)

    def test_right_face_valid_after_front_face_rotates_counter_clockwise(self):

        self.cube.rotate_front_face_CCW()
        
        expected_result = [["w","b","b"],["w","b","b"],["w","b","b"]]
        actual_result = self.cube.right.cells

        self.assertListEqual(expected_result, actual_result)

    def test_top_face_valid_after_front_face_rotates_counter_clockwise(self):

        self.cube.rotate_front_face_CCW()
        
        expected_result = [["y","y","y"],["y","y","y"],["b","b","b"]]
        actual_result = self.cube.top.cells

        self.assertListEqual(expected_result, actual_result)

    def test_bottom_face_valid_after_front_face_rotates_counter_clockwise(self):
        self.cube.rotate_front_face_CCW()
        
        expected_result = [["g","g","g"],["w","w","w"],["w","w","w"]]
        actual_result = self.cube.bottom.cells

        self.assertListEqual(expected_result, actual_result)

    def test_front_face_valid_after_front_face_rotates_clockwise(self):
        self.cube.rotate_front_face_CW()
        
        expected_result = [["o","o","o"],["o","o","o"],["o","o","o"]]
        actual_result = self.cube.front.cells

        self.assertListEqual(expected_result, actual_result)

    def test_back_face_valid_after_front_face_rotates_clockwise(self):
        self.cube.rotate_front_face_CW()
        
        expected_result = [["r","r","r"],["r","r","r"],["r","r","r"]]
        actual_result = self.cube.back.cells

        self.assertListEqual(expected_result, actual_result)

    def test_left_face_valid_after_front_face_rotates_clockwise(self):
        self.cube.rotate_front_face_CW()
        
        expected_result = [["g","g","w"],["g","g","w"],["g","g","w"]]
        actual_result = self.cube.left.cells

        self.assertListEqual(expected_result, actual_result)

    def test_right_face_valid_after_front_face_rotates_clockwise(self):

        self.cube.rotate_front_face_CW()
        
        expected_result = [["y","b","b"],["y","b","b"],["y","b","b"]]
        actual_result = self.cube.right.cells

        self.assertListEqual(expected_result, actual_result)

    def test_top_face_valid_after_front_face_rotates_clockwise(self):
        self.cube.rotate_front_face_CW()
        
        expected_result = [["y","y","y"],["y","y","y"],["g","g","g"]]
        actual_result = self.cube.top.cells

        self.assertListEqual(expected_result, actual_result)

    def test_bottom_face_valid_after_front_face_rotates_clockwise(self):

        self.cube.rotate_front_face_CW()
        
        expected_result = [["b","b","b"],["w","w","w"],["w","w","w"]]
        actual_result = self.cube.bottom.cells

        self.assertListEqual(expected_result, actual_result)

    #endregion Front Face Rotation Tests

    #region Back Face Rotation Tests
    def test_front_face_valid_after_back_face_rotates_counter_clockwise(self):
        self.cube.rotate_back_face_CCW()
        
        expected_result = [["o","o","o"],["o","o","o"],["o","o","o"]]
        actual_result = self.cube.front.cells

        self.assertListEqual(expected_result, actual_result)

    def test_back_face_valid_after_back_face_rotates_counter_clockwise(self):
        self.cube.rotate_back_face_CCW()
        
        expected_result = [["r","r","r"],["r","r","r"],["r","r","r"]]
        actual_result = self.cube.back.cells

        self.assertListEqual(expected_result, actual_result)

    def test_left_face_valid_after_back_face_rotates_counter_clockwise(self):
        self.cube.rotate_back_face_CCW()
        
        expected_result = [["w","g","g"],["w","g","g"],["w","g","g"]]
        actual_result = self.cube.left.cells

        self.assertListEqual(expected_result, actual_result)

    def test_right_face_valid_after_back_face_rotates_counter_clockwise(self):
        self.cube.rotate_back_face_CCW()
        
        expected_result = [["b","b","y"],["b","b","y"],["b","b","y"]]
        actual_result = self.cube.right.cells

        self.assertListEqual(expected_result, actual_result)

    def test_top_face_valid_after_back_face_rotates_counter_clockwise(self):
        self.cube.rotate_back_face_CCW()
        
        expected_result = [["g","g","g"],["y","y","y"],["y","y","y"]]
        actual_result = self.cube.top.cells

        self.assertListEqual(expected_result, actual_result)

    def test_bottom_face_valid_after_back_face_rotates_counter_clockwise(self):
        self.cube.rotate_back_face_CCW()
        
        expected_result = [["w","w","w"],["w","w","w"],["b","b","b"]]
        actual_result = self.cube.bottom.cells

        self.assertListEqual(expected_result, actual_result)

    def test_front_face_valid_after_back_face_rotates_clockwise(self):

        self.cube.rotate_back_face_CW()
        
        expected_result = [["o","o","o"],["o","o","o"],["o","o","o"]]
        actual_result = self.cube.front.cells

        self.assertListEqual(expected_result, actual_result)

    def test_back_face_valid_after_back_face_rotates_clockwise(self):

        self.cube.rotate_back_face_CW()
        
        expected_result = [["r","r","r"],["r","r","r"],["r","r","r"]]
        actual_result = self.cube.back.cells

        self.assertListEqual(expected_result, actual_result)

    def test_left_face_valid_after_back_face_rotates_clockwise(self):
        self.cube.rotate_back_face_CW()
        
        expected_result = [["y","g","g"],["y","g","g"],["y","g","g"]]
        actual_result = self.cube.left.cells

        self.assertListEqual(expected_result, actual_result)

    def test_right_face_valid_after_back_face_rotates_clockwise(self):

        self.cube.rotate_back_face_CW()
        
        expected_result = [["b","b","w"],["b","b","w"],["b","b","w"]]
        actual_result = self.cube.right.cells

        self.assertListEqual(expected_result, actual_result)

    def test_top_face_valid_after_back_face_rotates_clockwise(self):

        self.cube.rotate_back_face_CW()
        
        expected_result = [["b","b","b"],["y","y","y"],["y","y","y"]]
        actual_result = self.cube.top.cells

        self.assertListEqual(expected_result, actual_result)

    def test_bottom_face_valid_after_back_face_rotates_clockwise(self):
        self.cube.rotate_back_face_CW()
        
        expected_result = [["w","w","w"],["w","w","w"],["g","g","g"]]
        actual_result = self.cube.bottom.cells

        self.assertListEqual(expected_result, actual_result)


    #endregion Back Face Rotation Tests

    #region Left Face Rotation Tests
    def test_front_face_valid_after_left_face_rotates_counter_clockwise(self):

        self.cube.rotate_left_face_CCW()

        expected_result = [["w","o","o"], ["w","o","o"], ["w","o","o"]]
        actual_result = self.cube.front.cells

        self.assertListEqual(expected_result, actual_result)

    def test_back_face_valid_after_left_face_rotates_counter_clockwise(self):
        self.cube.rotate_left_face_CCW()

        expected_result = [["r","r","y"], ["r","r","y"], ["r","r","y"]]
        actual_result = self.cube.back.cells

        self.assertListEqual(expected_result, actual_result)

    def test_left_face_valid_after_left_face_rotates_counter_clockwise(self):
        self.cube.rotate_left_face_CCW()

        expected_result = [["g","g","g"], ["g","g","g"], ["g","g","g"]]
        actual_result = self.cube.left.cells

        self.assertListEqual(expected_result, actual_result)

    def test_right_face_valid_after_left_face_rotates_counter_clockwise(self):
        self.cube.rotate_left_face_CCW()

        expected_result = [["b","b","b"], ["b","b","b"], ["b","b","b"]]
        actual_result = self.cube.right.cells

        self.assertListEqual(expected_result, actual_result)

    def test_top_face_valid_after_left_face_rotates_counter_clockwise(self):
        self.cube.rotate_left_face_CCW()

        expected_result = [["o","y","y"], ["o","y","y"], ["o","y","y"]]
        actual_result = self.cube.top.cells

        self.assertListEqual(expected_result, actual_result)

    def test_bottom_face_valid_after_left_face_rotates_counter_clockwise(self):
        self.cube.rotate_left_face_CCW()

        expected_result = [["r","w","w"], ["r","w","w"], ["r","w","w"]]
        actual_result = self.cube.bottom.cells

        self.assertListEqual(expected_result, actual_result)

    def test_front_face_valid_after_left_face_rotates_clockwise(self):
        self.cube.rotate_left_face_CW()

        expected_result = [["y","o","o"], ["y","o","o"], ["y","o","o"]]
        actual_result = self.cube.front.cells

        self.assertListEqual(expected_result, actual_result)

    def test_back_face_valid_after_left_face_rotates_clockwise(self):
        self.cube.rotate_left_face_CW()

        expected_result = [["r","r","w"], ["r","r","w"], ["r","r","w"]]
        actual_result = self.cube.back.cells

        self.assertListEqual(expected_result, actual_result)

    def test_left_face_valid_after_left_face_rotates_clockwise(self):
        self.cube.rotate_left_face_CW()

        expected_result = [["g","g","g"], ["g","g","g"], ["g","g","g"]]
        actual_result = self.cube.left.cells

        self.assertListEqual(expected_result, actual_result)

    def test_right_face_valid_after_left_face_rotates_clockwise(self):
        self.cube.rotate_left_face_CW()

        expected_result = [["b","b","b"], ["b","b","b"], ["b","b","b"]]
        actual_result = self.cube.right.cells

        self.assertListEqual(expected_result, actual_result)

    def test_top_face_valid_after_left_face_rotates_clockwise(self):
        self.cube.rotate_left_face_CW()

        expected_result = [["r","y","y"], ["r","y","y"], ["r","y","y"]]
        actual_result = self.cube.top.cells

        self.assertListEqual(expected_result, actual_result)

    def test_bottom_face_valid_after_left_face_rotates_clockwise(self):
        self.cube.rotate_left_face_CW()

        expected_result = [["o","w","w"], ["o","w","w"], ["o","w","w"]]
        actual_result = self.cube.bottom.cells

        self.assertListEqual(expected_result, actual_result)
  


    #endregion Left Face Rotation Tests

    #region Right Face Rotation Tests
    def test_front_face_valid_after_right_face_rotates_counter_clockwise(self):

        self.cube.rotate_right_face_CCW()

        expected_result = [["o","o","y"],["o","o","y"],["o","o","y"]]
        actual_result = self.cube.front.cells

        self.assertListEqual(expected_result, actual_result)

    def test_back_face_valid_after_right_face_rotates_counter_clockwise(self):

        self.cube.rotate_right_face_CCW()

        expected_result = [["w","r","r"],["w","r","r"],["w","r","r"]]
        actual_result = self.cube.back.cells

        self.assertListEqual(expected_result, actual_result)

    def test_left_face_valid_after_right_face_rotates_counter_clockwise(self):

        self.cube.rotate_right_face_CCW()
        expected_result = [["g","g","g"],["g","g","g"],["g","g","g"]]
        actual_result = self.cube.left.cells

        self.assertListEqual(expected_result, actual_result)

    def test_right_face_valid_after_right_face_rotates_counter_clockwise(self):

        self.cube.rotate_right_face_CCW()

        expected_result = [["b","b","b"],["b","b","b"],["b","b","b"]]
        actual_result = self.cube.right.cells

        self.assertListEqual(expected_result, actual_result)

    def test_top_face_valid_after_right_face_rotates_counter_clockwise(self):

        self.cube.rotate_right_face_CCW()

        expected_result = [["y","y","r"],["y","y","r"],["y","y","r"]]
        actual_result = self.cube.top.cells

        self.assertListEqual(expected_result, actual_result)

    def test_bottom_face_valid_after_right_face_rotates_counter_clockwise(self):

        self.cube.rotate_right_face_CCW()

        expected_result = [["w","w","o"],["w","w","o"],["w","w","o"]]
        actual_result = self.cube.bottom.cells

        self.assertListEqual(expected_result, actual_result)

    def test_front_face_valid_after_right_face_rotates_clockwise(self):

        self.cube.rotate_right_face_CW()

        expected_result = [["o","o","w"],["o","o","w"],["o","o","w"]]
        actual_result = self.cube.front.cells

        self.assertListEqual(expected_result, actual_result)

    def test_back_face_valid_after_right_face_rotates_clockwise(self):

        self.cube.rotate_right_face_CW()

        expected_result = [["y","r","r"],["y","r","r"],["y","r","r"]]
        actual_result = self.cube.back.cells

        self.assertListEqual(expected_result, actual_result)

    def test_left_face_valid_after_right_face_rotates_clockwise(self):

        self.cube.rotate_right_face_CW()

        expected_result = [["g","g","g"],["g","g","g"],["g","g","g"]]
        actual_result = self.cube.left.cells

        self.assertListEqual(expected_result, actual_result)

    def test_right_face_valid_after_right_face_rotates_clockwise(self):
    
        self.cube.rotate_right_face_CW()

        expected_result = [["b","b","b"],["b","b","b"],["b","b","b"]]
        actual_result = self.cube.right.cells

        self.assertListEqual(expected_result, actual_result)

    def test_top_face_valid_after_right_face_rotates_clockwise(self):

        self.cube.rotate_right_face_CW()

        expected_result = [["y","y","o"],["y","y","o"],["y","y","o"]]
        actual_result = self.cube.top.cells

        self.assertListEqual(expected_result, actual_result)

    def test_bottom_face_valid_after_right_face_rotates_clockwise(self):

        self.cube.rotate_right_face_CW()

        expected_result = [["w","w","r"],["w","w","r"],["w","w","r"]]
        actual_result = self.cube.bottom.cells

        self.assertListEqual(expected_result, actual_result)


    #endregion Right Face Rotation Tests

    #region Top Face Rotation Tests
    def test_front_face_valid_after_top_face_rotates_counter_clockwise(self):

        self.cube.rotate_top_face_CCW()

        expected_result = [["g","g","g"],["o","o","o"],["o","o","o"]]
        actual_result = self.cube.front.cells

        self.assertListEqual(expected_result, actual_result)

    def test_back_face_valid_after_top_face_rotates_counter_clockwise(self):

        self.cube.rotate_top_face_CCW()

        expected_result = [["b","b","b"],["r","r","r"],["r","r","r"]]
        actual_result = self.cube.back.cells

        self.assertListEqual(expected_result, actual_result)

    def test_left_face_valid_after_top_face_rotates_counter_clockwise(self):\
    
        self.cube.rotate_top_face_CCW()

        expected_result = [["r","r","r"],["g","g","g"],["g","g","g"]]
        actual_result = self.cube.left.cells

        self.assertListEqual(expected_result, actual_result)

    def test_right_face_valid_after_top_face_rotates_counter_clockwise(self):

        self.cube.rotate_top_face_CCW()

        expected_result = [["o","o","o"],["b","b","b"],["b","b","b"]]
        actual_result = self.cube.right.cells

        self.assertListEqual(expected_result, actual_result)

    def test_top_face_valid_after_top_face_rotates_counter_clockwise(self):

        self.cube.rotate_top_face_CCW()

        expected_result = [["y","y","y"],["y","y","y"],["y","y","y"]]
        actual_result = self.cube.top.cells

        self.assertListEqual(expected_result, actual_result)

    def test_bottom_face_valid_after_top_face_rotates_counter_clockwise(self):

        self.cube.rotate_top_face_CCW()

        expected_result = [["w","w","w"],["w","w","w"],["w","w","w"]]
        actual_result = self.cube.bottom.cells

        self.assertListEqual(expected_result, actual_result)

    def test_front_face_valid_after_top_face_rotates_clockwise(self):

        self.cube.rotate_top_face_CW()

        expected_result = [["b","b","b"],["o","o","o"],["o","o","o"]]
        actual_result = self.cube.front.cells

        self.assertListEqual(expected_result, actual_result)

    def test_back_face_valid_after_top_face_rotates_clockwise(self):

        self.cube.rotate_top_face_CW()

        expected_result = [["g","g","g"],["r","r","r"],["r","r","r"]]
        actual_result = self.cube.back.cells

        self.assertListEqual(expected_result, actual_result)

    def test_left_face_valid_after_top_face_rotates_clockwise(self):

        self.cube.rotate_top_face_CW()

        expected_result = [["o","o","o"],["g","g","g"],["g","g","g"]]
        actual_result = self.cube.left.cells

        self.assertListEqual(expected_result, actual_result)

    def test_right_face_valid_after_top_face_rotates_clockwise(self):

        self.cube.rotate_top_face_CW()

        expected_result = [["r","r","r"],["b","b","b"],["b","b","b"]]
        actual_result = self.cube.right.cells

        self.assertListEqual(expected_result, actual_result)

    def test_top_face_valid_after_top_face_rotates_clockwise(self):

        self.cube.rotate_top_face_CW()

        expected_result = [["y","y","y"],["y","y","y"],["y","y","y"]]
        actual_result = self.cube.top.cells

        self.assertListEqual(expected_result, actual_result)

    def test_bottom_face_valid_after_top_face_rotates_clockwise(self):

        self.cube.rotate_top_face_CW()

        expected_result = [["w","w","w"],["w","w","w"],["w","w","w"]]
        actual_result = self.cube.bottom.cells

        self.assertListEqual(expected_result, actual_result)


    #endregion Top Face Rotation Tests

    #region Bottom Face Rotation Tests
    def test_front_face_valid_after_bottom_face_rotates_counter_clockwise(self):

        self.cube.rotate_bottom_face_CCW()

        expected_result = [["o","o","o"],["o","o","o"],["b","b","b"]]
        actual_result = self.cube.front.cells

        self.assertListEqual(expected_result, actual_result)

    def test_back_face_valid_after_bottom_face_rotates_counter_clockwise(self):

        self.cube.rotate_bottom_face_CCW()

        expected_result = [["r","r","r"],["r","r","r"],["g","g","g"]]
        actual_result = self.cube.back.cells

        self.assertListEqual(expected_result, actual_result)

    def test_left_face_valid_after_bottom_face_rotates_counter_clockwise(self):

        self.cube.rotate_bottom_face_CCW()

        expected_result = [["g","g","g"],["g","g","g"],["o","o","o"]]
        actual_result = self.cube.left.cells

        self.assertListEqual(expected_result, actual_result)

    def test_right_face_valid_after_bottom_face_rotates_counter_clockwise(self):

        self.cube.rotate_bottom_face_CCW()

        expected_result = [["b","b","b"],["b","b","b"],["r","r","r"]]
        actual_result = self.cube.right.cells

        self.assertListEqual(expected_result, actual_result)

    def test_top_face_valid_after_bottom_face_rotates_counter_clockwise(self):

        self.cube.rotate_bottom_face_CCW()

        expected_result = [["y","y","y"],["y","y","y"],["y","y","y"]]
        actual_result = self.cube.top.cells

        self.assertListEqual(expected_result, actual_result)

    def test_bottom_face_valid_after_bottom_face_rotates_counter_clockwise(self):

        self.cube.rotate_bottom_face_CCW()

        expected_result = [["w","w","w"],["w","w","w"],["w","w","w"]]
        actual_result = self.cube.bottom.cells

        self.assertListEqual(expected_result, actual_result)

    def test_front_face_valid_after_bottom_face_rotates_clockwise(self):

        self.cube.rotate_bottom_face_CW()

        expected_result = [["o","o","o"],["o","o","o"],["g","g","g"]]
        actual_result = self.cube.front.cells

        self.assertListEqual(expected_result, actual_result)

    def test_back_face_valid_after_bottom_face_rotates_clockwise(self):

        self.cube.rotate_bottom_face_CW()

        expected_result = [["r","r","r"],["r","r","r"],["b","b","b"]]
        actual_result = self.cube.back.cells

        self.assertListEqual(expected_result, actual_result)

    def test_left_face_valid_after_bottom_face_rotates_clockwise(self):

        self.cube.rotate_bottom_face_CW()

        expected_result = [["g","g","g"],["g","g","g"],["r","r","r"]]
        actual_result = self.cube.left.cells

        self.assertListEqual(expected_result, actual_result)

    def test_right_face_valid_after_bottom_face_rotates_clockwise(self):

        self.cube.rotate_bottom_face_CW()

        expected_result = [["b","b","b"],["b","b","b"],["o","o","o"]]
        actual_result = self.cube.right.cells

        self.assertListEqual(expected_result, actual_result)

    def test_top_face_valid_after_bottom_face_rotates_clockwise(self):

        self.cube.rotate_bottom_face_CW()

        expected_result = [["y","y","y"],["y","y","y"],["y","y","y"]]
        actual_result = self.cube.top.cells

        self.assertListEqual(expected_result, actual_result)

    def test_bottom_face_valid_after_bottom_face_rotates_clockwise(self):

        self.cube.rotate_bottom_face_CW()

        expected_result = [["w","w","w"],["w","w","w"],["w","w","w"]]
        actual_result = self.cube.bottom.cells

        self.assertListEqual(expected_result, actual_result)

    #endregion Bottom Face Rotation Tests

    #region Middle Face Rotation Tests
    def test_front_face_valid_after_middle_face_rotates_counter_clockwise(self):

        self.cube.rotate_middle_face_CCW()

        expected_result = [["o","o","o"],["o","o","o"],["o","o","o"]]
        actual_result = self.cube.front.cells

        self.assertListEqual(expected_result, actual_result)

    def test_back_face_valid_after_middle_face_rotates_counter_clockwise(self):

        self.cube.rotate_middle_face_CCW()

        expected_result = [["r","r","r"],["r","r","r"],["r","r","r"]]
        actual_result = self.cube.back.cells

        self.assertListEqual(expected_result, actual_result)

    def test_left_face_valid_after_middle_face_rotates_counter_clockwise(self):

        self.cube.rotate_middle_face_CCW()

        expected_result = [["g","y","g"],["g","y","g"],["g","y","g"]]
        actual_result = self.cube.left.cells

        self.assertListEqual(expected_result, actual_result)

    def test_right_face_valid_after_middle_face_rotates_counter_clockwise(self):

        self.cube.rotate_middle_face_CCW()

        expected_result = [["b","w","b"],["b","w","b"],["b","w","b"]]
        actual_result = self.cube.right.cells

        self.assertListEqual(expected_result, actual_result)

    def test_top_face_valid_after_middle_face_rotates_counter_clockwise(self):

        self.cube.rotate_middle_face_CCW()

        expected_result = [["y","y","y"],["b","b","b"],["y","y","y"]]
        actual_result = self.cube.top.cells

        self.assertListEqual(expected_result, actual_result)

    def test_bottom_face_valid_after_middle_face_rotates_counter_clockwise(self):

        self.cube.rotate_middle_face_CCW()

        expected_result = [["w","w","w"],["g","g","g"],["w","w","w"]]
        actual_result = self.cube.bottom.cells

        self.assertListEqual(expected_result, actual_result)

    def test_front_face_valid_after_middle_face_rotates_clockwise(self):

        self.cube.rotate_middle_face_CW()

        expected_result = [["o","o","o"],["o","o","o"],["o","o","o"]]
        actual_result = self.cube.front.cells

        self.assertListEqual(expected_result, actual_result)

    def test_back_face_valid_after_middle_face_rotates_clockwise(self):

        self.cube.rotate_middle_face_CW()

        expected_result = [["r","r","r"], ["r","r","r"], ["r","r","r"]]
        actual_result = self.cube.back.cells

        self.assertListEqual(expected_result, actual_result)

    def test_left_face_valid_after_middle_face_rotates_clockwise(self):

        self.cube.rotate_middle_face_CW()

        expected_result = [["g","w","g"], ["g","w","g"], ["g","w","g"]]
        actual_result = self.cube.left.cells

        self.assertListEqual(expected_result, actual_result)

    def test_right_face_valid_after_middle_face_rotates_clockwise(self):

        self.cube.rotate_middle_face_CW()

        expected_result = [["b","y","b"],["b","y","b"],["b","y","b"]]
        actual_result = self.cube.right.cells

        self.assertListEqual(expected_result, actual_result)

    def test_top_face_valid_after_middle_face_rotates_clockwise(self):

        self.cube.rotate_middle_face_CW()

        expected_result = [["y","y","y"],["g","g","g"],["y","y","y"]]
        actual_result = self.cube.top.cells

        self.assertListEqual(expected_result, actual_result)

    def test_bottom_face_valid_after_middle_face_rotates_clockwise(self):

        self.cube.rotate_middle_face_CW()

        expected_result = [["w","w","w"],["b","b","b"],["w","w","w"]]
        actual_result = self.cube.bottom.cells

        self.assertListEqual(expected_result, actual_result)

    #endregion Middle Face Rotation Tests

    #endregion Face Operation Tests

    #endregion Rotation Tests

    #region Cube Helper Method Tests
    #I'm not sure how to test a random method, will return here later
    #TODO How do you test something like randomizing the cube?

    #endregion Cube Helper Method Tests

    #region Cube Orientation Shift Tests


    #region Tests for Setting the Left Face as the new Front

    def test_front_face_valid_after_setting_left_face_to_front(self):
        pass

    def test_back_face_valid_after_setting_left_face_to_front(self):
        pass

    def test_left_face_valid_after_setting_left_face_to_front(self):
        pass

    def test_right_face_valid_after_setting_left_face_to_front(self):
        pass    

    def test_top_face_valid_after_setting_left_face_to_front(self):
        pass

    def test_bottom_face_valid_after_setting_left_face_to_front(self):
        pass    
    
    #endregion Tests for Setting the Left Face as the new Front

    #region Tests for Setting the Back Face as the new Front

    def test_front_face_valid_after_setting_back_face_to_front(self):
        pass

    def test_back_face_valid_after_setting_back_face_to_front(self):
        pass

    def test_left_face_valid_after_setting_back_face_to_front(self):
        pass

    def test_right_face_valid_after_setting_back_face_to_front(self):
        pass

    def test_top_face_valid_after_setting_back_face_to_front(self):
        pass

    def test_bottom_face_valid_after_setting_back_face_to_front(self):
        pass

    #endregion Tests for Setting the Back Face as the new Front

    
    #region Tests for Setting the Right Face as the new Front

    def test_front_face_valid_after_setting_right_face_to_front(self):
        pass

    def test_back_face_valid_after_setting_right_face_to_front(self):
        pass

    def test_left_face_valid_after_setting_right_face_to_front(self):
        pass

    def test_right_face_valid_after_setting_right_face_to_front(self):
        pass

    def test_top_face_valid_after_setting_right_face_to_front(self):
        pass

    def test_bottom_face_valid_after_setting_right_face_to_front(self):
        pass

    #endregion Tests for Setting the Right Face as the new Front


    #region Tests for Setting the Top Face as the new Front

    def test_front_face_valid_after_setting_top_face_to_front(self):
        pass

    def test_back_face_valid_after_setting_top_face_to_front(self):
        pass

    def test_left_face_valid_after_setting_top_face_to_front(self):
        pass

    def test_right_face_valid_after_setting_top_face_to_front(self):
        pass

    def test_top_face_valid_after_setting_top_face_to_front(self):
        pass

    def test_bottom_face_valid_after_setting_top_face_to_front(self):
        pass

    #endregion Tests for Setting the Top Face as the new Front


    #region Tests for Setting the Bottom Face as the new Front
    def test_front_face_valid_after_setting_bottom_face_to_front(self):
        pass

    def test_back_face_valid_after_setting_bottom_face_to_front(self):
        pass

    def test_left_face_valid_after_setting_bottom_face_to_front(self):
        pass

    def test_right_face_valid_after_setting_bottom_face_to_front(self):
        pass

    def test_top_face_valid_after_setting_bottom_face_to_front(self):
        pass

    def test_bottom_face_valid_after_setting_bottom_face_to_front(self):
        pass

    #endregion Tests for Setting the Bottom Face as the new Front

    #endregion Cube Orientation Shift Tests