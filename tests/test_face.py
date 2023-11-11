import unittest
from unittest.mock import patch
from pyrub.face import Face

class TestFace(unittest.TestCase):
    """
    Subclass for testing our methods
    """ 
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

    #endregion str tests

    #region repr tests

    #endregion repr tests

    #region To String Tests

    #endregion To String Tests
    
    #region Face Completeness Tests


    #endregion Face Completeness Tests

    #region Get Methods

    #endregion Get Methods

    #region Rotate Methods

    #endregion Rotate Methods

    #region Replace Methods

    #endregion Replace methods

    