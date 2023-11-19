import unittest
from unittest.mock import patch
from pyrub.face import Face

class TestFace(unittest.TestCase):
    """
    Test Case Subclass for testing our Face methods
    """ 
    @classmethod
    def setUp(self) -> None:
        self.face = Face('r', 3)

    @classmethod
    def tearDown(self) -> None:
        self.face = None

    #region Constructor Tests
    def test_face_side_length(self):
        self.assertEqual(self.face.side_length, 3, 'Incorrect side length')

    def test_face_side_color(self):
        self.assertEqual(self.face.color, 'r', 'Incorrect color')

    def test_face_array_filled_properly(self):
        faceList = [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']]
        self.assertListEqual(self.face.cells, faceList, 'Face not initialized to color properly')

    #endregion Constructor Tests

    #region str tests
    def test_face_str_populated(self):

        actual_result = str(self.face)
        isEmpty = (actual_result == "")

        self.assertFalse(isEmpty)


    #endregion str tests

    #region repr tests
    def test_face_repr_populated(self):

        actual_result = repr(self.face)
        isEmpty = (actual_result == "")

        self.assertFalse(isEmpty)


    #endregion repr tests

    #region To String Tests
    def test_face_to_string_populated(self):
        
        actual_result = self.face.face_to_string()
        isEmpty = (actual_result == "")

        self.assertFalse(isEmpty)

    def test_face_to_string_valid(self):
        
        actual_result = self.face.face_to_string()
        expected_result = "r\tr\tr\nr\tr\tr\nr\tr\tr\n\n"

        self.assertEqual(expected_result, actual_result)

    
    def test_flatten_face(self):

        expected_result = ["r", "r", "r", "r", "r", "r", "r", "r", "r"]
        actual_result = self.face.list_view

        self.assertListEqual(expected_result, actual_result)


    #endregion To String Tests
    
    #region Face Completeness Tests
    def test_face_completeness(self):
        complete = self.face.validate_cell_uniformity()
        self.assertTrue(complete)

    def test_face_incomplete(self):

        self.face.cells[0][0] = "*"

        complete = self.face.validate_cell_uniformity()
        self.assertFalse(complete)


    #endregion Face Completeness Tests

    #region Get Methods
    def test_get_top_row(self):
        
        expected_result = ["r", "r", "r"]
        actual_result = self.face.get_row(0)

        self.assertListEqual(expected_result, actual_result)

    def test_get_middle_row(self):

        expected_result = ["r", "r", "r"]
        actual_result = self.face.get_row(1)

        self.assertListEqual(expected_result, actual_result)

    def test_get_bottom_row(self):

        expected_result = ["r", "r", "r"]
        actual_result = self.face.get_row(2)

        self.assertListEqual(expected_result, actual_result)

    def test_get_left_column(self):

        expected_result = ["r", "r", "r"]
        actual_result = self.face.get_column(0)

        self.assertListEqual(expected_result, actual_result)


    def test_get_middle_column(self):

        expected_result = ["r", "r", "r"]
        actual_result = self.face.get_column(1)

        self.assertListEqual(expected_result, actual_result)

    def test_get_right_column(self):

        expected_result = ["r", "r", "r"]
        actual_result = self.face.get_column(2)

        self.assertListEqual(expected_result, actual_result)     

    #endregion Get Methods

    #region Rotate Methods
    def test_rotate_CW_row_updated(self):
        
        self.face.cells[0][0] = "*"
        self.face.cells[0][1] = "*"
        self.face.cells[0][2] = "*"
        
        self.face.rotate_CW()

        expected_result = [['r', 'r', '*'], ['r', 'r', '*'], ['r', 'r', '*']]
        actual_result = self.face.cells

        self.assertListEqual(expected_result, actual_result)

  

    def test_rotate_CCW(self):

        self.face.cells[0][0] = "*"
        self.face.cells[0][1] = "*"
        self.face.cells[0][2] = "*"

        self.face.rotate_CCW()

        expected_result= [['*', 'r', 'r'], ['*', 'r', 'r'], ['*', 'r', 'r']]
        actual_result = self.face.cells


        self.assertListEqual(expected_result, actual_result)


    #endregion Rotate Methods

    #region Replace Methods
    def test_replace_top_row_with_row(self):

        replacement_row = ["1", "2", "3"]
        self.face.replace_row_with_row(replacement_row, 0, True)

        expected_result = ["1", "2", "3"]
        actual_result = self.face.get_row(0)

        self.assertListEqual(expected_result, actual_result)


    def test_replace_middle_row_with_row(self):

        replacement_row = ["1", "2", "3"]
        self.face.replace_row_with_row(replacement_row, 1, True)

        expected_result = ["1", "2", "3"]
        actual_result = self.face.get_row(1)

        self.assertListEqual(expected_result, actual_result)

    def test_replace_bottom_row_with_row(self):

        replacement_row = ["1", "2", "3"]
        self.face.replace_row_with_row(replacement_row, 2, True)

        expected_result = ["1", "2", "3"]
        actual_result = self.face.get_row(2)

        self.assertListEqual(expected_result, actual_result)


    def test_replace_top_row_with_row_descending(self):
        replacement_row = ["1", "2", "3"]
        self.face.replace_row_with_row(replacement_row, 0, False)


        expected_result = ["3", "2", "1"]
        actual_result = self.face.get_row(0)

        self.assertListEqual(expected_result, actual_result)


    def test_replace_middle_row_with_row_descending(self):
        replacement_row = ["1", "2", "3"]
        self.face.replace_row_with_row(replacement_row, 1, False)

        expected_result = ["3", "2", "1"]
        actual_result = self.face.get_row(1)

        self.assertListEqual(expected_result, actual_result)


    def test_replace_bottom_row_with_row_descending(self):
        replacement_row = ["1", "2", "3"]
        self.face.replace_row_with_row(replacement_row, 2, False)

        expected_result = ["3", "2", "1"]
        actual_result = self.face.get_row(2)

        self.assertListEqual(expected_result, actual_result)


    def test_replace_top_row_with_col(self):
        replacement_column = ["1", "2", "3"]
        self.face.replace_row_with_col(replacement_column, 0, True)


        expected_result = ["1", "2", "3"]
        actual_result = self.face.get_row(0)

        self.assertListEqual(expected_result, actual_result)


    def test_replace_middle_row_with_col(self):
        replacement_column = ["1", "2", "3"]
        self.face.replace_row_with_col(replacement_column, 1, True)


        expected_result = ["1", "2", "3"]
        actual_result = self.face.get_row(1)

        self.assertListEqual(expected_result, actual_result)


    def test_replace_bottom_row_with_col(self):
        replacement_column = ["1", "2", "3"]
        self.face.replace_row_with_col(replacement_column, 2, True)


        expected_result = ["1", "2", "3"]
        actual_result = self.face.get_row(2)

        self.assertListEqual(expected_result, actual_result)


    def test_replace_row_with_col_descending(self):
        replacement_column = ["1", "2", "3"]
        self.face.replace_row_with_col(replacement_column, 0, False)

        expected_result = ["3", "2", "1"]
        actual_result = self.face.get_row(0)

        self.assertListEqual(expected_result, actual_result)

    def test_replace_middle_row_with_col_descending(self):
        replacement_column = ["1", "2", "3"]
        self.face.replace_row_with_col(replacement_column, 1, False)

        expected_result = ["3", "2", "1"]
        actual_result = self.face.get_row(1)

        self.assertListEqual(expected_result, actual_result)

    def test_replace_bottom_row_with_col_descending(self):
        replacement_column = ["1", "2", "3"]
        self.face.replace_row_with_col(replacement_column, 2, False)

        expected_result = ["3", "2", "1"]
        actual_result = self.face.get_row(2)

        self.assertListEqual(expected_result, actual_result)


    def test_replace_left_col_with_col(self):
        replacement_column = ["1", "2", "3"]
        self.face.replace_col_with_col(replacement_column, 0, True)

        expected_result = ["1","2","3"]
        actual_result = self.face.get_column(0)

        self.assertListEqual(expected_result, actual_result)

    def test_replace_middle_col_with_col(self):
        replacement_column = ["1", "2", "3"]
        self.face.replace_col_with_col(replacement_column, 1, True)

        expected_result = ["1","2","3"]
        actual_result = self.face.get_column(1)

        self.assertListEqual(expected_result, actual_result)

    def test_replace_right_col_with_col(self):
        replacement_column = ["1", "2", "3"]
        self.face.replace_col_with_col(replacement_column, 2, True)

        expected_result = ["1","2","3"]
        actual_result = self.face.get_column(2)

        self.assertListEqual(expected_result, actual_result)

    def test_replace_left_col_with_col_descending(self):
        replacement_column = ["1", "2", "3"]
        self.face.replace_col_with_col(replacement_column, 0, False)

        expected_result = ["3","2","1"]
        actual_result = self.face.get_column(0)

        self.assertListEqual(expected_result, actual_result)

    def test_replace_middle_col_with_col_descending(self):
        replacement_column = ["1", "2", "3"]
        self.face.replace_col_with_col(replacement_column, 1, False)

        expected_result = ["3","2","1"]
        actual_result = self.face.get_column(1)

        self.assertListEqual(expected_result, actual_result)


    def test_replace_right_col_with_col_descending(self):
        replacement_column = ["1", "2", "3"]
        self.face.replace_col_with_col(replacement_column, 2, False)

        expected_result = ["3","2","1"]
        actual_result = self.face.get_column(2)

        self.assertListEqual(expected_result, actual_result)


    def test_replace_left_col_with_row(self):
        replacement_row = ["1", "2", "3"]
        self.face.replace_col_with_row(replacement_row, 0, True)

        expected_result = ["1", "2", "3"]
        actual_result = self.face.get_column(0)
        self.assertListEqual(expected_result, actual_result)

    def test_replace_middle_col_with_row(self):
        replacement_row = ["1", "2", "3"]
        self.face.replace_col_with_row(replacement_row, 1, True)

        expected_result = ["1", "2", "3"]
        actual_result = self.face.get_column(1)
        self.assertListEqual(expected_result, actual_result)

    def test_replace_right_col_with_row(self):
        replacement_row = ["1", "2", "3"]
        self.face.replace_col_with_row(replacement_row, 2, True)

        expected_result = ["1", "2", "3"]
        actual_result = self.face.get_column(2)
        self.assertListEqual(expected_result, actual_result)

    def test_replace_left_col_with_row_descending(self):
        replacement_row = ["1", "2", "3"]
        self.face.replace_col_with_row(replacement_row, 0, False)

        expected_result = ["3", "2", "1"]
        actual_result = self.face.get_column(0)
        self.assertListEqual(expected_result, actual_result)

    def test_replace_middle_col_with_row_descending(self):
        replacement_row = ["1", "2", "3"]
        self.face.replace_col_with_row(replacement_row, 1, False)

        expected_result = ["3", "2", "1"]
        actual_result = self.face.get_column(1)
        self.assertListEqual(expected_result, actual_result)

    def test_replace_right_col_with_row_descending(self):
        replacement_row = ["1", "2", "3"]
        self.face.replace_col_with_row(replacement_row, 2, False)

        expected_result = ["3", "2", "1"]
        actual_result = self.face.get_column(2)
        self.assertListEqual(expected_result, actual_result)      

    #endregion Replace methods

    