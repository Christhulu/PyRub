from cube import Cube
from face import Face

from consolemenu import *
from consolemenu.items import *

class Game(object):

    def __init__(self):
        self.cube:list[Cube] = []
        #index of current cube
        self.current_cube_index = 0



    #Cube Display (This is the visual display for the cube)
    # Print Current Cube (if Applicable)
    def display_current_cube(self):
        pass


    #Home/Operations Menu
    # Start a New Cube
    # Print Current Cube (if Applicable)
    # Rotate a row, column, or face
    # Randomize Cube
    # Instantly "Solve" Cube
    # Exit
    def show_home(self):
        pass

    #Rotate Menu
    # 0. Rotate Row
    # 1. Rotate Column
    # 2. Rotate Face
    def show_rotation_menu(self):
        pass

    # Rotate Row Menu
    # Which row would you like to rotate?
    # 0. Row 0 (Top Row)
    # 1. Row 1 (Middle Row)
    # 2. Row 2 (Bottom Row)
    def show_row_rotation_menu(self):
        pass

    # Rotate Row Direction
    # Which direction would you like to rotate the row?
    # 0. Left
    # 1. Right
    def show_row_rotation_direction_menu(self):
        pass

    # Rotate Column Menu
    # Which column would you like to rotate?
    # 0. Column 0 (Top Row)
    # 1. Column 1 (Middle Row)
    # 2. Column 2 (Bottom Row)
    def show_column_rotation_menu(self):
        pass

    # Rotate Column Direction
    # Which direction would you like to rotate the column?
    # 0. Up
    # 1. Down
    def show_rotate_column_direction_menu(self):
        pass

    # Rotate Face Menu
    # 0. Front
    # 1. Middle
    # 2. Back
    def show_rotate_face_menu(self):
        pass

    # Rotate Face Direction
    # Subtitle: *Face*
    # 0 - Clockwise
    # 1 - Counter Clockwise
    def show_rotate_face_direction_menu(self):
        pass

    # Choose a new Front relative to the current front of the cube:
    # 0 - Front
    # 1 - Right
    # 2 - Back
    # 3 - Left
    # 4 - Top
    # 5 - Bottom
    def show_reorient_menu(self):
        pass