from cube import Cube
from face import Face

from consolemenu import *
from consolemenu.items import *
from consolemenu.format import *
import sys

class Game(object):

    def __init__(self):
        self.cubes:list[Cube] = []
        #index of current cube
        self.current_cube_index = 0
        self.home_menu = ConsoleMenu("PyRub", "A Console Application for solving Rubik's Cubes")
        self.home_options_menu = SelectionMenu(["Play", "Help"], subtitle="Options", prologue_text="Select an option.", show_exit_option=True, clear_screen=True)
        
        self.menu_format = MenuFormatBuilder().set_border_style_type(MenuBorderStyleType.HEAVY_BORDER) \
        .set_prompt("SELECT>") \
        .set_title_align('center') \
        .set_subtitle_align('center') \
        .set_left_margin(4) \
        .set_right_margin(4) \
        .show_header_bottom_border(True)

    
    def play(self):
        self.show_home_menu()

        

    #Show home menu
    def show_home_menu(self):
        self.home_menu.show()

    #Cube Management

    #Add a new cube
    def add_new_cube(self):
        new_cube = Cube()
        self.cubes.append(new_cube)

    def update_current_cube(self, index: int):
        if index > 0 and index < len(self.cubes):
            self.current_cube_index = index
        else:
            #Display error message
            self.show_error_menu()

    #Cube Display (This is the visual display for the cube)
    # Print Current Cube (if Applicable)
    def display_current_cube(self):
        self.cubes[0].print_cube()


    def append_operations_menu(self):
        #Create operations selection menu
        operations_menu = SelectionMenu(
                            title="Operations",
                            strings=["Start a New Cube", "Print Current Cube (if Applicable)",
                            "Rotate a row, column, or face","Randomize Cube"],
                            show_exit_option=True,
                            exit_option_text="Back",
                            clear_screen=True
                        )
        



    #Operations Menu
    # Start a New Cube
    # Print Current Cube (if Applicable)
    # Rotate a row, column, or face
    # Randomize Cube
    # Instantly "Solve" Cube
    # Exit
    def show_operations_menu(self):
        pass

    def close_operations_menu(self):
        pass


    #__ Add rotation menu to game menu __
    # _Rotate Menu_
    # Rotate Row
    # Rotate Column
    # Rotate Face
    def append_rotation_menu(self):
        #Create rotation selection menu
        rotation_menu = SelectionMenu(
                            title="Rotation Types",
                            strings=["Rotate Row","Rotate Column","Rotate Face"],
                            show_exit_option=True,
                            exit_option_text="Back",
                            clear_screen=True
                        )
        
    #__ Show rotation menu __
    # _Rotate Menu_
    # 0. Rotate Row
    # 1. Rotate Column
    # 2. Rotate Face
    def show_rotation_menu(self):
        pass
    
    #__ Add row rotation menu to rotation menu __
    # _Row Rotation Menu_
    # Message: Which row would you like to rotate?
    # Row 1 (Top Row)
    # Row 2 (Middle Row)
    # Row 3 (Bottom Row)
    def append_row_rotation_menu(self):
        #Create row rotation selection menu
        row_rotation_menu = SelectionMenu(
                            title="Which row would you like to rotate?",
                            strings=["Top Row","Middle Row","Bottom Row"],
                            show_exit_option=True,
                            exit_option_text="Back",
                            clear_screen=True
                        )

    #__ Show row rotation menu__
    # _Row Rotation Menu_
    # Which row would you like to rotate?
    # 0. Row 0 (Top Row)
    # 1. Row 1 (Middle Row)
    # 2. Row 2 (Bottom Row)
    def show_row_rotation_menu(self):
        pass

    #__ Add row rotation direction menu as submenu to ? menu __
    # Rotate Row Direction
    # Which direction would you like to rotate the row?
    # 0. Left
    # 1. Right
    def append_row_rotation_direction_menu(self):
        pass

    #__ Show row rotation direction menu __
    # Rotate Row Direction
    # Which direction would you like to rotate the row?
    # 0. Left
    # 1. Right
    def show_row_rotation_direction_menu(self):
        pass




    #__ Add column rotation menu as submenu to rotation menu __
    # _Column Rotation Menu_
    # Message: Which column would you like to rotate?
    # 0. Column 0 (Left Column)
    # 1. Column 1 (Middle Column)
    # 2. Column 2 (Right Column)
    def append_column_rotation_menu(self):
        #Create column rotation selection menu
        column_rotation_menu = SelectionMenu(
                            title="Which column would you like to rotate?",
                            strings=["Left Column","Middle Column","Right Column"],
                            show_exit_option=True,
                            exit_option_text="Back",
                            clear_screen=True
                        )


    #__ Show column rotation menu __
    # _Column Rotation Menu_
    # Message: Which column would you like to rotate?
    # 0. Column 0 (Left Column)
    # 1. Column 1 (Middle Column)
    # 2. Column 2 (Right Column)
    def show_column_rotation_menu(self):
        pass


    #__ Add column rotation direction menu as submenu to column rotation menu __
    # _Column Rotation Direction Menu_
    # Message: Which direction would you like to rotate the column?
    # 0. Up
    # 1. Down
    def append_rotate_column_direction_menu(self):
        pass

    #__ Show column rotation direction menu__
    # _Column Rotation Direction Menu_
    # Message: Which direction would you like to rotate the column?
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


    #Error Message Menu
    def show_error_menu(self, error: int):

        error_mesage: str = ""
        match error:
            case 0:
                error_mesage = "Invalid index: This is not a valid choice for a cube."

        error_function = FunctionItem("Start a New Cube", Screen().printf("{error}: {error_message}"), should_exit=True)
        error_function.clean_up()
