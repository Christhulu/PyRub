from cube import Cube
from face import Face

from consolemenu import *
from consolemenu.items import *
from consolemenu.format import *
import sys

# MIT LICENSE FOR CONSOLE-MENU
# The MIT License (MIT)
# Copyright (c) Paul Barrett, Aegir Hall
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


class Game(object):

    #Thinking of not nesting any menus to be honest
    def __init__(self):
        self.cubes:list[Cube] = []
        #index of current cube
        self.current_cube_index = 0

        self.menu_format = MenuFormatBuilder().set_border_style_type(MenuBorderStyleType.HEAVY_BORDER) \
        .set_prompt("SELECT>") \
        .set_title_align('center') \
        .set_subtitle_align('center') \
        .set_prologue_text_align('left') \
        .set_left_margin(4) \
        .set_right_margin(4) \
        .show_header_bottom_border(True)

        self.home_menu = ConsoleMenu("PyRub", "A Console Application for solving Rubik's Cubes", exit_option_text="Quit", show_exit_option=True, clear_screen=True)

        self.about_menu = ConsoleMenu(title="About",
                            prologue_text= "Created by Chris Alexander\nSpecial Thanks to:\n\n* Aegir Hall (for their incredible work on the console-menu library)\n* Paul Barret (for their work on curses-menu)",
                            show_exit_option=True,
                            exit_option_text="Back",
                            clear_screen=True,
                            formatter=self.menu_format
                        )
        
        self.help_menu = ConsoleMenu(title="Help",
                            prologue_text= "Welcome to PyRub, a Rubik's cube game built in Python 3. To select an option, type the number corresponding to the option and press enter. Have fun!",
                            show_exit_option=True,
                            exit_option_text="Back",
                            clear_screen=True,
                            formatter=self.menu_format
                        )
        

        self.operations_menu = SelectionMenu(
                            title="Operations",
                            strings=["Start a New Cube", "Print Current Cube (if Applicable)",
                            "Rotate a row, column, or face","Randomize Cube"],
                            show_exit_option=True,
                            exit_option_text="Back",
                            clear_screen=True,
                            formatter=self.menu_format
                        )

        self.rotation_menu = SelectionMenu(
                            title="Rotation Types",
                            strings=["Rotate Row","Rotate Column","Rotate Face"],
                            show_exit_option=True,
                            exit_option_text="Back",
                            clear_screen=True,
                            formatter=self.menu_format
                        )

        self.row_rotation_menu = SelectionMenu(
                            title="Which row would you like to rotate?",
                            strings=["Top Row","Middle Row","Bottom Row"],
                            show_exit_option=True,
                            exit_option_text="Back",
                            clear_screen=True,
                            formatter=self.menu_format
                        )
        
        self.row_rotation_direction_menu = SelectionMenu(
                    title="Which row would you like to rotate?",
                    strings=["Left","Right"],
                    show_exit_option=True,
                    exit_option_text="Back",
                    clear_screen=True,
                    formatter=self.menu_format
                )
        
        self.column_rotation_menu = SelectionMenu(
                            title="Which column would you like to rotate?",
                            strings=["Left Column","Middle Column","Right Column"],
                            show_exit_option=True,
                            exit_option_text="Back",
                            clear_screen=True,
                            formatter=self.menu_format
                        )
        
        self.column_rotation_direction_menu = SelectionMenu(
                            title="Which direction would you like to rotate the column?",
                            strings=["Up","Down"],
                            show_exit_option=True,
                            exit_option_text="Back",
                            clear_screen=True,
                            formatter=self.menu_format
                        )

        self.face_rotation_menu = SelectionMenu(
                            title="Which face would you like to rotate?",
                            strings=["Front Face","Middle Face","Back Face"],
                            show_exit_option=True,
                            exit_option_text="Back",
                            clear_screen=True,
                            formatter=self.menu_format
                        )

        self.face_rotation_direction_menu = SelectionMenu(
                            title="Which direction would you like to rotate the face? (relative to the front)",
                            strings=["Left","Right"],
                            show_exit_option=True,
                            exit_option_text="Back",
                            clear_screen=True,
                            formatter=self.menu_format
                        )

        self.reorient_menu = SelectionMenu(
                            title="Choose a new Front relative to the current front of the cube:",
                            strings=["Right", "Back", "Left", "Top", "Bottom"],
                            show_exit_option=True,
                            exit_option_text="Back",
                            clear_screen=True,
                            formatter=self.menu_format
                        )
        
        self.connect_menus()




    #Connect relevant menus to each other
    def connect_menus(self):

        operations_sub_menu = SubmenuItem("Play", submenu=self.operations_menu, menu=self.home_menu)
        help_sub_menu = SubmenuItem("Help", submenu=self.help_menu, menu=self.home_menu)
        about_sub_menu = SubmenuItem("About", submenu=self.about_menu, menu=self.home_menu)

        #Append main operations to home
        self.home_menu.append_item(operations_sub_menu)
        self.home_menu.append_item(help_sub_menu)
        self.home_menu.append_item(about_sub_menu)


    
    def play(self):
        self.show_home_menu()

        

    #Show home menu
    def show_home_menu(self):
        self.home_menu.show()


    def append_help_menu(self):
        pass


    #Show help menu
    def show_help_menu(self):
        self.help_menu.clear_screen_before_render = True
        self.show_help_menu.show()

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


    # __ Add operations menu to game menu __
    # _ Operations Menu _ 
    # Start a New Cube
    # Print Current Cube (if Applicable)
    # Rotate a row, column, or face
    # Randomize Cube
    # Instantly "Solve" Cube
    # Exit
    def append_operations_menu(self):
        #Not sure if I should add this to anything
        pass
        

    
    # __ Show operations menu __
    # _ Operations Menu _ 
    # Start a New Cube
    # Print Current Cube (if Applicable)
    # Rotate a row, column, or face
    # Randomize Cube
    # Instantly "Solve" Cube
    # Exit
    def show_operations_menu(self):
        self.operations_menu.clear_screen_before_render = True
        self.operations_menu.show()

    # __ Close operations menu __
    # _ Operations Menu _ 
    # Start a New Cube
    # Print Current Cube (if Applicable)
    # Rotate a row, column, or face
    # Randomize Cube
    # Instantly "Solve" Cube
    # Exit
    def close_operations_menu(self):
        self.operations_menu.exit()


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
        self.rotation_menu.clear_screen_before_render = True
        self.rotation_menu.show()

    
    #__ Add row rotation menu to rotation menu __
    # _Row Rotation Menu_
    # Message: Which row would you like to rotate?
    # Row 1 (Top Row)
    # Row 2 (Middle Row)
    # Row 3 (Bottom Row)
    def append_row_rotation_menu(self):
        self.rotation_menu.append_item(self.row_rotation_menu)


    #__ Show row rotation menu__
    # _Row Rotation Menu_
    # Which row would you like to rotate?
    # 0. Row 0 (Top Row)
    # 1. Row 1 (Middle Row)
    # 2. Row 2 (Bottom Row)
    def show_row_rotation_menu(self):
        self.row_rotation_menu.clear_screen_before_render = True
        self.row_rotation_menu.show()

    #__ Add row rotation direction menu as submenu to ? menu __
    # Rotate Row Direction
    # Which direction would you like to rotate the row?
    # 0. Left
    # 1. Right
    def append_row_rotation_direction_menu(self):
        row_rotation_direction_menu = SelectionMenu(
                    title="Which row would you like to rotate?",
                    strings=["Left","Right"],
                    show_exit_option=True,
                    exit_option_text="Back",
                    clear_screen=True
                )

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
        column_rotation_direction_menu = SelectionMenu(
                            title="Which direction would you like to rotate the column?",
                            strings=["Up","Down"],
                            show_exit_option=True,
                            exit_option_text="Back",
                            clear_screen=True
                        )

    #__ Show column rotation direction menu__
    # _Column Rotation Direction Menu_
    # Message: Which direction would you like to rotate the column?
    # 0. Up
    # 1. Down
    def show_rotate_column_direction_menu(self):
        pass

    #__ Add face rotation menu as submenu to rotation menu __
    # _Face Rotation Menu_
    # Message: Which face would you like to rotate? (relative to the front)
    # 0. Front Face
    # 1. Middle Face
    # 2. Back Face
    def append_rotate_face_menu(self):
        face_rotation_menu = SelectionMenu(
                            title="Which face would you like to rotate?",
                            strings=["Front Face","Middle Face","Back Face"],
                            show_exit_option=True,
                            exit_option_text="Back",
                            clear_screen=True
                        )
        
    #__ Show face rotation menu __
    # _ Face Rotation Menu_
    # Message: Which face would you like to rotate? (relative to the front)
    # 0. Front Face
    # 1. Middle Face
    # 2. Back Face
    def show_rotate_face_menu(self):
        pass

    #__ Add face rotation direction menu as submenu to face rotation menu __
    # _Face Rotation Direction Menu_
    # Message: Which direction would you like to rotate the face? (relative to the front)
    # 0 - Left (Counter-Clockwise relative to the front face, Clockwise relative to the back face)
    # 1 - Right (Clockwise relative to the front face, Counter-Clockwise relative to the back face) 
    def append_rotate_face_direction_menu(self):
        face_rotation_direction_menu = SelectionMenu(
                            title="Which direction would you like to rotate the face? (relative to the front)",
                            strings=["Left","Right"],
                            show_exit_option=True,
                            exit_option_text="Back",
                            clear_screen=True
                        )
        pass

    #__ Show face rotation direction menu __
    # _Face Rotation Direction Menu_
    # Which direction would you like to rotate the face?
    # 0 - Clockwise
    # 1 - Counter-Clockwise
    def show_rotate_face_direction_menu(self):
        pass


    #__ Add reorient cube menu __
    # _ Reorient Cube _
    # Message: Choose a new Front relative to the current front of the cube:
    # 0 - Front
    # 1 - Right
    # 2 - Back
    # 3 - Left
    # 4 - Top
    # 5 - Bottom
    def append_reorient_menu(self):
        reorient_menu = SelectionMenu(
                            title="Choose a new Front relative to the current front of the cube:",
                            strings=["Right", "Back", "Left", "Top", "Bottom"],
                            show_exit_option=True,
                            exit_option_text="Back",
                            clear_screen=True
                        )
        pass

    #__ Add reorient cube menu __
    # _ Reorient Cube _
    # Message: Choose a new Front relative to the current front of the cube:
    # 0 - Front
    # 1 - Right
    # 2 - Back
    # 3 - Left
    # 4 - Top
    # 5 - Bottom
    def show_reorient_menu(self):
        pass

    # __ Add error menu __
    # _ Error Menu _ 
    # 
    def append_error_menu(self):
        pass

    # __ Show error menu __
    # _ Error Menu _ 
    # 
    def show_error_menu(self, error: int):

        error_mesage: str = ""
        match error:
            case 0:
                error_mesage = "Invalid index: This is not a valid choice for a cube."

        # error_function = FunctionItem("Error", Screen().printf("{error}: {error_message}"), should_exit=True)
        # error_function.clean_up() I don't know if I need to call this directly

    # __ Export cube list __
    # _ Export Cubes Menu _ 
    # TBD: Decide how to export cube list
    def export_cubes(self):
        pass

    # __ Import cube list __
    # _ Import Cubes Menu _ 
    # TBD: Decide how to import cubes
    def import_cubes(self):
        pass
