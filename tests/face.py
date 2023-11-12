import unittest
from unittest.mock import patch
from pyrub.face import Face

class TestFace(unittest.TestCase):
    """
    Test Case Subclass for testing our Face methods
    """ 

    def setUp(self) -> None:
        return super().setUp()

    #region Constructor Tests
    def test_face_side_length(self):
        face = Face('r', 3)
        self.assertEqual(face.side_length, 3, 'Incorrect side length')

    def test_face_side_color(self):
        face = Face('r', 3)
        self.assertEqual(face.color, 'r', 'Incorrect color')

    def test_face_array_filled_properly(self):
        face = Face('r', 3)
        faceList = [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']]
        self.assertListEqual(face, faceList, 'Face not initialized to color properly')

    #endregion Constructor Tests

    #region str tests
    def test_face_str(self):
        face = Face('r', 3)

        str_result = str(face)
        self.assertNotEqual(str_result, "")


    #endregion str tests

    #region repr tests
    def test_face_repr(self):
        face = Face('r', 3)

        repr_result = repr(face)
        self.assertNotEqual(repr_result, None)


    #endregion repr tests

    #region To String Tests
    def test_face_to_string(self):
        face = Face('r', 3)

        to_string_result = face.face_to_string()

        self.assertNotEqual(to_string_result, "")

    
    def test_flatten_face(self):
        face = Face('r', 3)

        expected_result = ["r", "r", "r", "r", "r", "r", "r", "r", "r"]
        self.assertListEqual(expected_result, face.list_view)


    #endregion To String Tests
    
    #region Face Completeness Tests
    def test_face_completeness(self):
        face = Face('r', 3)

        complete = face.validate_cell_uniformity()

        self.assertTrue(complete)

    def test_face_incomplete(self):
        face = Face('r', 3)

        face.cells[0][0] = "*"

        complete = face.validate_cell_uniformity()
        self.assertFalse(complete)


    #endregion Face Completeness Tests

    #region Get Methods
    def test_get_top_row(self):
        face = Face('r', 3)
        expected_row = ["r", "r", "r"]

        result = face.get_row(0)

        self.assertListEqual(result, expected_row)

    def test_get_middle_row(self):
        face = Face('r', 3)
        expected_row = ["r", "r", "r"]

        result = face.get_row(1)
        self.assertListEqual(result, expected_row)

    def test_get_bottom_row(self):
        face = Face('r', 3)
        expected_row = ["r", "r", "r"]

        result = face.get_row(2)
        self.assertListEqual(result, expected_row)

    def test_get_left_column(self):
        face = Face('r', 3)
        expected_column = ["r", "r", "r"]

        result = face.get_column(0)
        self.assertListEqual(result, expected_column)


    def test_get_middle_column(self):
        face = Face('r', 3)
        expected_column = ["r", "r", "r"]

        result = face.get_column(1)
        self.assertListEqual(result, expected_column)

    def test_get_right_column(self):
        face = Face('r', 3)
        expected_column = ["r", "r", "r"]

        result = face.get_column(2)
        self.assertListEqual(result, expected_column)     

    #endregion Get Methods

    #region Rotate Methods
    def test_rotate_CW(self):
        
        face = Face('r', 3)
        face.cells[0][0] = "*"
        face.cells[0][1] = "*"
        face.cells[0][2] = "*"
        
        face.rotate_CW()




    #endregion Rotate Methods

    #region Replace Methods

    #endregion Replace methods

    