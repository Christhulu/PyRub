import sys

from typing import Any, Sequence
from pyrub.cube import Cube
from pyrub.face import Face

from consolemenu import ConsoleMenu
from consolemenu import SelectionMenu
from consolemenu import Screen
from consolemenu import MenuFormatBuilder

from consolemenu.format import MenuBorderStyle
from consolemenu.format import MenuBorderStyleType

from consolemenu.items import SubmenuItem
from consolemenu.items import FunctionItem




# MIT LICENSE FOR CONSOLE-MENU
# The MIT License (MIT)
# Copyright (c) Paul Barrett, Aegir Hall
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


class Game(object):


    #region Game Constructor and field initialization
    def __init__(self):
        self.cubes:list[Cube] = [Cube()]
        #index of current cube
        self.current_cube_index = 0
        self.current_screen = Screen()

        #region Formatting
        self.menu_format = MenuFormatBuilder().set_border_style_type(MenuBorderStyleType.HEAVY_BORDER) \
        .set_prompt("SELECT>") \
        .set_title_align('center') \
        .set_subtitle_align('center') \
        .set_prologue_text_align('center') \
        .set_border_style_type(MenuBorderStyleType.DOUBLE_LINE_BORDER) \
        .set_left_margin(4) \
        .set_right_margin(4) \
        .show_header_bottom_border(True)

        #endregion Formatting

        #region Declare and connect game menus
        self.home_menu = ConsoleMenu("PyRub", "A Console Application for solving Rubik's Cubes", exit_option_text="Quit", show_exit_option=True, screen=self.current_screen, clear_screen=True)

        self.about_menu = ConsoleMenu(title="About",
                            prologue_text= "Created by Chris Alexander\nSpecial Thanks to:\n\n* Aegir Hall (for their incredible work on the console-menu library)\n* Paul Barret (for their work on curses-menu)",
                            show_exit_option=True,
                            exit_option_text="Back",
                            screen=self.current_screen,
                            clear_screen=True,
                            formatter=self.menu_format
                        )
        
        self.help_menu = ConsoleMenu(title="Help",
                            prologue_text= "Welcome to PyRub, a Rubik's cube game built in Python 3. To select an option, type the number corresponding to the option and press enter. Have fun!",
                            show_exit_option=True,
                            exit_option_text="Back",
                            screen=self.current_screen,
                            clear_screen=True,
                            
                            formatter=self.menu_format
                        )
        
        self.cube_menu = ConsoleMenu(
                            title=self.get_current_cube_title,
                            subtitle="Front",
                            prologue_text= self.get_front_face_prologue,
                            show_exit_option=True,
                            exit_option_text="Back",
                            formatter=self.menu_format,
                        )
        
        self.cube_faces_menu = ConsoleMenu(
                            title=self.get_current_cube_title,
                            subtitle="Current Face: Front (Choose a new face to view)",
                            prologue_text=self.get_front_face_prologue,
                            show_exit_option=True,
                            exit_option_text="Back",
                            formatter=self.menu_format,
                        )


        self.operations_menu = ConsoleMenu(
                            title="Operations",
                            prologue_text=self.get_front_face_prologue,
                            show_exit_option=True,
                            exit_option_text="Back",
                            formatter=self.menu_format,
                        )

        self.rotation_menu = ConsoleMenu(
                            title="Rotation Types",
                            prologue_text=self.get_front_face_prologue,
                            show_exit_option=True,
                            exit_option_text="Back",
                            screen=self.current_screen,
                            clear_screen=True,
                            formatter=self.menu_format
                        )

        self.row_rotation_menu = ConsoleMenu(
                            title="Which row would you like to rotate?",
                            prologue_text=self.get_front_face_prologue,
                            show_exit_option=True,
                            exit_option_text="Back",
                            screen=self.current_screen,
                            clear_screen=True,
                            formatter=self.menu_format
                        )
        
        self.row_rotation_direction_menu = ConsoleMenu(
                    title="Which direction would you like to rotate the row?",
                    prologue_text=self.get_front_face_prologue,
                    show_exit_option=True,
                    exit_option_text="Back",
                    screen=self.current_screen,
                    clear_screen=True,
                    formatter=self.menu_format
                )
        
        self.column_rotation_menu = ConsoleMenu(
                            title="Which column would you like to rotate?",
                            prologue_text=self.get_front_face_prologue,
                            show_exit_option=True,
                            exit_option_text="Back",
                            screen=self.current_screen,
                            clear_screen=True,
                            formatter=self.menu_format
                        )
        
        self.column_rotation_direction_menu = ConsoleMenu(
                            title="Which direction would you like to rotate the column?",
                            prologue_text=self.get_front_face_prologue,
                            show_exit_option=True,
                            exit_option_text="Back",
                            screen=self.current_screen,
                            clear_screen=True,
                            formatter=self.menu_format
                        )

        self.face_rotation_menu = ConsoleMenu(
                            title="Which face would you like to rotate?",
                            show_exit_option=True,
                            exit_option_text="Back",
                            screen=self.current_screen,
                            clear_screen=True,
                            formatter=self.menu_format
                        )

        self.face_rotation_direction_menu = ConsoleMenu(
                            title="Which direction would you like to rotate the face? (relative to the front)",
                            show_exit_option=True,
                            exit_option_text="Back",
                            screen=self.current_screen,
                            clear_screen=True,
                            formatter=self.menu_format
                        )

        self.reorient_menu = ConsoleMenu(
                            title="Choose a new Front relative to the current front of the cube:",
                            show_exit_option=True,
                            exit_option_text="Back",
                            screen=self.current_screen,
                            clear_screen=True,
                            formatter=self.menu_format
                        )
        
        self.connect_menus()

        #endregion Declare and connect game menus

    #endregion Game Constructor and field initialization

    #region Dynamic Title Helper Functions

    def get_current_cube_index(self):
        return self.current_cube_index
    
    def get_current_cube_title(self):
        return f"Cube: {self.current_cube_index}"

    #endregion Dynamic Title Helper Functions

    #region Dynamic Subtitle Helper Functions

    #endregion Dynamic Subtitle Helper Functions

    #region Dynamic Prologue Helper Functions
    
    def get_front_face_prologue(self) -> str:
        return self.cubes[self.current_cube_index].face_to_string(0)

    def get_back_face_prologue(self) -> str:
        return self.cubes[self.current_cube_index].face_to_string(1)

    def get_left_face_prologue(self) -> str:
        return self.cubes[self.current_cube_index].face_to_string(2)

    def get_right_face_prologue(self) -> str:
        return self.cubes[self.current_cube_index].face_to_string(3)

    def get_top_face_prologue(self) -> str:
        return self.cubes[self.current_cube_index].face_to_string(4)

    def get_bottom_face_prologue(self) -> str:
        return self.cubes[self.current_cube_index].face_to_string(5)

    #endregion Dynamic Prologue Helper Functions

    #region Helper methods for attaching menu objects to their parent menus

    def attach_base_menus(self):
        # Create and append operations submenu items to operations menu
        operations_sub_menu = SubmenuItem("Play", submenu=self.operations_menu, menu=self.home_menu)

        help_sub_menu = SubmenuItem("Help", submenu=self.help_menu, menu=self.home_menu)

        about_sub_menu = SubmenuItem("About", submenu=self.about_menu, menu=self.home_menu)

        #Append main operations to home
        self.home_menu.append_item(operations_sub_menu)
        self.home_menu.append_item(help_sub_menu)
        self.home_menu.append_item(about_sub_menu)

    def attach_operation_items(self):
        new_cube_item = FunctionItem("Start a New Cube", function=self.add_new_cube, menu=self.operations_menu, should_exit=True)
        # 2nd

        view_cube_item = SubmenuItem(text="View Current Cube", menu=self.operations_menu, submenu=self.cube_menu)
        # #3rd
        rotate_submenu = SubmenuItem(text="Rotate a row, column, or face", menu=self.operations_menu, submenu=self.rotation_menu)
        # #4th
        randomize_cube_item = FunctionItem(text="Randomize Cube", function=self.randomize_cube, menu=self.operations_menu, should_exit=True)

        #Append operations to operations menu
        self.operations_menu.append_item(new_cube_item)
        self.operations_menu.append_item(view_cube_item)
        self.operations_menu.append_item(rotate_submenu)
        self.operations_menu.append_item(randomize_cube_item)

    def attach_rotate_menus(self):
        #Append row operations to rotate menu


        rotate_row_submenu = SubmenuItem(text="Rotate Row", submenu=self.row_rotation_menu, menu=self.rotation_menu)
        rotate_column_submenu = SubmenuItem(text="Rotate Column", submenu=self.column_rotation_menu, menu=self.rotation_menu)
        rotate_face_submenu = SubmenuItem(text="Rotate Face", submenu=self.face_rotation_menu, menu=self.rotation_menu)

        self.rotation_menu.append_item(rotate_row_submenu)
        self.rotation_menu.append_item(rotate_column_submenu)
        self.rotation_menu.append_item(rotate_face_submenu)

        #Add rows to row rotation menu
        rotate_top_row_submenu = SubmenuItem(text="Top Row", submenu=self.row_rotation_direction_menu, menu=self.rotation_menu)
        rotate_middle_row_submenu = SubmenuItem(text="Middle Row", submenu=self.row_rotation_direction_menu, menu=self.rotation_menu)
        rotate_bottom_row_submenu = SubmenuItem(text="Bottom Row", submenu=self.row_rotation_direction_menu, menu=self.rotation_menu)

        self.row_rotation_menu.append_item(rotate_top_row_submenu)
        self.row_rotation_menu.append_item(rotate_middle_row_submenu)
        self.row_rotation_menu.append_item(rotate_bottom_row_submenu)

        #Add direction functions to row rotation direction menu
        rotate_row_left_function_item = FunctionItem(text="Left",function=self.rotate_row, menu=self.row_rotation_direction_menu, should_exit=True)
        rotate_row_right_function_item = FunctionItem(text="Right", function=self.rotate_row, menu=self.row_rotation_direction_menu, should_exit=True)

        self.row_rotation_direction_menu.append_item(rotate_row_left_function_item)
        self.row_rotation_direction_menu.append_item(rotate_row_right_function_item)

        #Add columns to column rotation menu
        rotate_left_column_submenu = SubmenuItem(text="Left Column", submenu=self.column_rotation_direction_menu, menu=self.rotation_menu)
        rotate_middle_column_submenu = SubmenuItem(text="Middle Column", submenu=self.column_rotation_direction_menu, menu=self.rotation_menu)
        rotate_right_column_submenu = SubmenuItem(text="Right Column", submenu=self.column_rotation_direction_menu, menu=self.rotation_menu)

        self.column_rotation_menu.append_item(rotate_left_column_submenu)
        self.column_rotation_menu.append_item(rotate_middle_column_submenu)
        self.column_rotation_menu.append_item(rotate_right_column_submenu)

        #Add direction functions to column rotation direction menu
        rotate_column_up_function_item = FunctionItem(text="Up",function=self.rotate_column, menu=self.column_rotation_direction_menu, should_exit=True)
        rotate_column_down_function_item = FunctionItem(text="Down", function=self.rotate_column, menu=self.column_rotation_direction_menu, should_exit=True)

        self.column_rotation_direction_menu.append_item(rotate_column_up_function_item)
        self.column_rotation_direction_menu.append_item(rotate_column_down_function_item)

        #Add faces to face rotation menu
        rotate_left_face_submenu = SubmenuItem(text="Left Face", submenu=self.face_rotation_direction_menu, menu=self.rotation_menu)
        rotate_right_face_submenu = SubmenuItem(text="Right Face", submenu=self.face_rotation_direction_menu, menu=self.rotation_menu)
        rotate_front_face_submenu = SubmenuItem(text="Front Face", submenu=self.face_rotation_direction_menu, menu=self.rotation_menu)
        rotate_middle_face_submenu = SubmenuItem(text="Middle Face", submenu=self.face_rotation_direction_menu, menu=self.rotation_menu)
        rotate_back_face_submenu = SubmenuItem(text="Back Face", submenu=self.face_rotation_direction_menu, menu=self.rotation_menu)
        rotate_top_face_submenu = SubmenuItem(text="Top Face", submenu=self.face_rotation_direction_menu, menu=self.rotation_menu)
        rotate_bottom_face_submenu = SubmenuItem(text="Bottom Face", submenu=self.face_rotation_direction_menu, menu=self.rotation_menu)

        
        self.face_rotation_menu.append_item(rotate_front_face_submenu)
        self.face_rotation_menu.append_item(rotate_middle_face_submenu)
        self.face_rotation_menu.append_item(rotate_back_face_submenu)
        self.face_rotation_menu.append_item(rotate_left_face_submenu)
        self.face_rotation_menu.append_item(rotate_right_face_submenu)
        self.face_rotation_menu.append_item(rotate_top_face_submenu)
        self.face_rotation_menu.append_item(rotate_bottom_face_submenu)

        #Add direction functions to face rotation direction menu
        rotate_face_CW_function_item = FunctionItem(text="Left (Counter-Clockwise)",function=self.rotate_face, menu=self.face_rotation_direction_menu, should_exit=True)
        rotate_face_CCW_function_item = FunctionItem(text="Right (Clock-Wise)", function=self.rotate_face, menu=self.face_rotation_direction_menu, should_exit=True)

        self.face_rotation_direction_menu.append_item(rotate_face_CW_function_item)
        self.face_rotation_direction_menu.append_item(rotate_face_CCW_function_item)

    def attach_cube_menus(self):
        #Append sections to view cube menu

        #Update front face if it's not up to date
        self.cube_front_string = self.cubes[self.current_cube_index].face_to_string(0)

        # self.front_face_menu = ConsoleMenu(title=f"Cube {self.current_cube_index}", subtitle="Front", prologue_text=f"{self.cube_front_string}", formatter=self.menu_format, show_exit_option=True, exit_option_text="Back", clear_screen=True)
        # self.back_face_menu = ConsoleMenu(title=f"Cube: {self.current_cube_index}", subtitle="Back", prologue_text=f"{self.cubes[self.current_cube_index].face_to_string(2)}", formatter=self.menu_format, show_exit_option=True, exit_option_text="Back", clear_screen=True)
        # self.left_face_menu = ConsoleMenu(title=f"Cube: {self.current_cube_index}", subtitle="Left", prologue_text=f"{self.cubes[self.current_cube_index].face_to_string(3)}", formatter=self.menu_format, show_exit_option=True, exit_option_text="Back", clear_screen=True)
        # self.right_face_menu = ConsoleMenu(title=f"Cube: {self.current_cube_index}", subtitle="Right", prologue_text=f"{self.cubes[self.current_cube_index].face_to_string(1)}", formatter=self.menu_format, show_exit_option=True, exit_option_text="Back", clear_screen=True)
        # self.top_face_menu = ConsoleMenu(title=f"Cube: {self.current_cube_index}", subtitle="Top", prologue_text=f"{self.cubes[self.current_cube_index].face_to_string(4)}", formatter=self.menu_format, show_exit_option=True, exit_option_text="Back", clear_screen=True)
        # self.bottom_face_menu = ConsoleMenu(title=f"Cube: {self.current_cube_index}", subtitle="Bottom", prologue_text=f"{self.cubes[self.current_cube_index].face_to_string(5)}", formatter=self.menu_format, show_exit_option=True, exit_option_text="Back", clear_screen=True)

        self.front_face_menu = ConsoleMenu(title=self.get_current_cube_title, subtitle="Front", prologue_text=f"{self.cube_front_string}", formatter=self.menu_format, show_exit_option=True, exit_option_text="Back", clear_screen=True)
        self.back_face_menu = ConsoleMenu(title=self.get_current_cube_title, subtitle="Back", prologue_text=f"{self.cubes[self.current_cube_index].face_to_string(2)}", formatter=self.menu_format, show_exit_option=True, exit_option_text="Back", clear_screen=True)
        self.left_face_menu = ConsoleMenu(title=self.get_current_cube_title, subtitle="Left", prologue_text=f"{self.cubes[self.current_cube_index].face_to_string(3)}", formatter=self.menu_format, show_exit_option=True, exit_option_text="Back", clear_screen=True)
        self.right_face_menu = ConsoleMenu(title=self.get_current_cube_title, subtitle="Right", prologue_text=f"{self.cubes[self.current_cube_index].face_to_string(1)}", formatter=self.menu_format, show_exit_option=True, exit_option_text="Back", clear_screen=True)
        self.top_face_menu = ConsoleMenu(title=self.get_current_cube_title, subtitle="Top", prologue_text=f"{self.cubes[self.current_cube_index].face_to_string(4)}", formatter=self.menu_format, show_exit_option=True, exit_option_text="Back", clear_screen=True)
        self.bottom_face_menu = ConsoleMenu(title=self.get_current_cube_title, subtitle="Bottom", prologue_text=f"{self.cubes[self.current_cube_index].face_to_string(5)}", formatter=self.menu_format, show_exit_option=True, exit_option_text="Back", clear_screen=True)


        self.front_face_submenu = SubmenuItem(text="Front Face", submenu=self.front_face_menu, menu=self.cube_menu)
        self.back_face_submenu = SubmenuItem(text="Back Face", submenu=self.back_face_menu, menu=self.cube_menu)
        self.left_face_submenu = SubmenuItem(text="Left Face", submenu=self.left_face_menu, menu=self.cube_menu)
        self.right_face_submenu = SubmenuItem(text="Right Face", submenu=self.right_face_menu, menu=self.cube_menu)
        self.top_face_submenu = SubmenuItem(text="Top Face", submenu=self.top_face_menu, menu=self.cube_menu)
        self.bottom_face_submenu = SubmenuItem(text="Bottom Face", submenu=self.bottom_face_menu, menu=self.cube_menu)
        
        self.cube_menu.append_item(self.front_face_submenu)
        self.cube_menu.append_item(self.back_face_submenu)
        self.cube_menu.append_item(self.left_face_submenu)
        self.cube_menu.append_item(self.right_face_submenu)
        self.cube_menu.append_item(self.top_face_submenu)
        self.cube_menu.append_item(self.bottom_face_submenu)

    #Attach the menus for changing which face is the front
    def attach_orientation_menus(self):
        pass

    #Connect relevant menus to each other
    def connect_menus(self):

        self.attach_base_menus()
        self.attach_operation_items()
        self.attach_rotate_menus()
        self.attach_cube_menus()

    #endregion Helper methods for attaching menu objects to their parent menus

    #region Game Setup

    def play(self):
        self.home_menu.show()

    #endregion Game Setup

    #region Cube Management
    def add_new_cube(self):
        new_cube = Cube()
        self.cubes.append(new_cube)

    def update_current_cube(self, index: int):
        if index > 0 and index < len(self.cubes):
            self.current_cube_index = index
        else:
            #Display error message
            self.show_error_menu()
    
    def get_cube_string(self) ->str:
        cube = self.cubes[self.current_cube_index].cube_to_string()
        return cube

    def update_front_face_string(self) -> None:
        self.cube_front_string:str = self.cubes[self.current_cube_index].face_to_string(0)
    
    def randomize_cube(self) -> None:
        self.cubes[self.current_cube_index].randomize_cube()

    #endregion Cube Management

    #region Rotation Menu Functions
    
    #region Row Rotation Menu Functions
    def rotate_row(self):
        
        #Get previous menu
        row_name = self.row_rotation_menu.currently_active_menu.get_title()
        row_direction = self.row_rotation_direction_menu.currently_active_menu.get_title()

        #Define these explicitly in case row name or row direction aren't defined yet
        if row_name == "Top Row":
            self.cubes[self.current_cube_index].rotate_top_row_left() if row_direction == "Left" else self.cubes[self.current_cube_index].rotate_top_row_right()
        elif row_name == "Middle Row":
            self.cubes[self.current_cube_index].rotate_middle_row_left() if row_direction == "Left" else self.cubes[self.current_cube_index].rotate_middle_row_right()
        elif row_name == "Bottom Row":
            self.cubes[self.current_cube_index].rotate_bottom_row_left() if row_direction == "Left" else self.cubes[self.current_cube_index].rotate_bottom_row_right()

        self.update_front_face_string()
        self.row_rotation_menu.prologue_text = f"{self.cube_front_string}"
        self.row_rotation_direction_menu.prologue_text = f"{self.cube_front_string}"

    #endregion Row Rotation Menu Functions

    #region Column Rotation Menu Functions

    def rotate_column(self):
        #Get previous menu
        column_name = self.row_rotation_menu.currently_active_menu.get_title()
        column_direction = self.row_rotation_direction_menu.currently_active_menu.get_title()

        #Define these explicitly in case column name or column direction aren't defined yet
        if column_name == "Left Column":
            self.cubes[self.current_cube_index].rotate_left_column_up() if column_direction == "Up" else self.cubes[self.current_cube_index].rotate_left_column_down()
        elif column_name == "Middle Column":
            self.cubes[self.current_cube_index].rotate_middle_column_up() if column_direction == "Up" else self.cubes[self.current_cube_index].rotate_middle_column_down()
        elif column_name == "Right Column":
            self.cubes[self.current_cube_index].rotate_right_column_up() if column_direction == "Up" else self.cubes[self.current_cube_index].rotate_right_column_down()

        self.update_front_face_string()

    #endregion Column Rotation Menu Functions

    #region Face Rotation Menu Functions
    def rotate_face(self):
        #Get previous menu
        face_name = self.face_rotation_menu.currently_active_menu.get_title()
        face_direction = self.face_rotation_direction_menu.currently_active_menu.get_title()

        #There are some more things I need to do in terms of being able to rotate any face
        # if face_name == "Front Face":
        #     self.cubes[self.current_cube_index] if face_direction == "Left" else self.cubes[self.current_cube_index]
        # elif face_name == "Back Face":
        #     self.cubes[self.current_cube_index] if face_direction == "Left" else self.cubes[self.current_cube_index]
        # elif face_name == "Left Face":
        #     self.cubes[self.current_cube_index] if face_direction == "Left" else self.cubes[self.current_cube_index]
        # elif face_name == "Right Face":
        #     self.cubes[self.current_cube_index] if face_direction == "Left" else self.cubes[self.current_cube_index]
        # elif face_name == "Top Face":
        #     self.cubes[self.current_cube_index] if face_direction == "Left" else self.cubes[self.current_cube_index]
        # else:
        #     self.cubes[self.current_cube_index] if face_direction == "Left" else self.cubes[self.current_cube_index]
        #     #Bottom Face
        self.update_front_face_string()

    #endregion Face Rotation Menu Functions

    #endregion Rotation Menu Functions

    #region Reorient Cube Menu Functions

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

    #endregion Reorient Cube Menu Functions


    #region Error Menu Functions

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

    #endregion Error Menu Functions


    #region Cube Export/Import Functions

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

    #endregion Cube Export/Import Functions
