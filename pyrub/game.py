from typing import Any, Sequence
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
        self.cubes:list[Cube] = [Cube()]
        #index of current cube
        self.current_cube_index = 0
        self.current_cube_string:str = self.cubes[self.current_cube_index].cube_to_string()
        self.cube_front_string:str = self.cubes[self.current_cube_index].face_to_string(0)
        self.current_screen = Screen()

        self.menu_format = MenuFormatBuilder().set_border_style_type(MenuBorderStyleType.HEAVY_BORDER) \
        .set_prompt("SELECT>") \
        .set_title_align('center') \
        .set_subtitle_align('center') \
        .set_prologue_text_align('center') \
        .set_border_style_type(MenuBorderStyleType.DOUBLE_LINE_BORDER) \
        .set_left_margin(4) \
        .set_right_margin(4) \
        .show_header_bottom_border(True)

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
                            title=f"Cube {self.current_cube_index}",
                            subtitle="Front",
                            prologue_text= f"{self.cube_front_string}",
                            show_exit_option=True,
                            exit_option_text="Back",
                            formatter=self.menu_format,
                        )
        
        self.cube_faces_menu = ConsoleMenu(
                            title=f"Cube {self.current_cube_index}",
                            subtitle="Current Face: Front (Choose a new face to view)",
                            prologue_text= f"{self.cube_front_string}",
                            show_exit_option=True,
                            exit_option_text="Back",
                            formatter=self.menu_format,
                        )


        self.operations_menu = ConsoleMenu(
                            title="Operations",
                            prologue_text= f"{self.cube_front_string}",
                            show_exit_option=True,
                            exit_option_text="Back",
                            formatter=self.menu_format,
                        )

        self.rotation_menu = ConsoleMenu(
                            title="Rotation Types",
                            show_exit_option=True,
                            exit_option_text="Back",
                            screen=self.current_screen,
                            clear_screen=True,
                            formatter=self.menu_format
                        )

        self.row_rotation_menu = ConsoleMenu(
                            title="Which row would you like to rotate?",
                            show_exit_option=True,
                            exit_option_text="Back",
                            screen=self.current_screen,
                            clear_screen=True,
                            formatter=self.menu_format
                        )
        
        self.row_rotation_direction_menu = ConsoleMenu(
                    title="Which direction would you like to rotate the row?",
                    show_exit_option=True,
                    exit_option_text="Back",
                    screen=self.current_screen,
                    clear_screen=True,
                    formatter=self.menu_format
                )
        
        self.column_rotation_menu = ConsoleMenu(
                            title="Which column would you like to rotate?",
                            show_exit_option=True,
                            exit_option_text="Back",
                            screen=self.current_screen,
                            clear_screen=True,
                            formatter=self.menu_format
                        )
        
        self.column_rotation_direction_menu = ConsoleMenu(
                            title="Which direction would you like to rotate the column?",
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
        randomize_cube_item = FunctionItem(text="Randomize Cube (Under Construction)", function=self.randomize_cube, menu=self.operations_menu, should_exit=True)

        #Append operations to operations menu
        self.operations_menu.append_item(new_cube_item)
        self.operations_menu.append_item(view_cube_item)
        self.operations_menu.append_item(rotate_submenu)
        self.operations_menu.append_item(randomize_cube_item)

    def attach_rotate_menus(self):
        #Append row operations to rotate menu
        rotate_row_item = SubmenuItem(text="Rotate Row", submenu=self.row_rotation_menu, menu=self.rotation_menu)
        rotate_column_item = SubmenuItem(text="Rotate Column", submenu=self.column_rotation_menu, menu=self.rotation_menu)
        rotate_face_item = SubmenuItem(text="Rotate Face", submenu=self.face_rotation_menu, menu=self.rotation_menu)

        self.rotation_menu.append_item(rotate_row_item)
        self.rotation_menu.append_item(rotate_column_item)
        self.rotation_menu.append_item(rotate_face_item)

        #Add rows to row rotation menu
        # strings=["Top Row","Middle Row","Bottom Row"]
        rotate_top_row = SubmenuItem(text="Top Row", submenu=self.row_rotation_direction_menu, menu=self.rotation_menu)
        rotate_middle_row = SubmenuItem(text="Middle Row", submenu=self.row_rotation_direction_menu, menu=self.rotation_menu)
        rotate_bottom_row = SubmenuItem(text="Bottom Row", submenu=self.row_rotation_direction_menu, menu=self.rotation_menu)

        self.row_rotation_menu.append_item(rotate_top_row)
        self.row_rotation_menu.append_item(rotate_middle_row)
        self.row_rotation_menu.append_item(rotate_bottom_row)

        #Add columns to column rotation menu
        rotate_left_column = SubmenuItem(text="Left Column", submenu=self.column_rotation_direction_menu, menu=self.rotation_menu)
        rotate_middle_column = SubmenuItem(text="Middle Column", submenu=self.column_rotation_direction_menu, menu=self.rotation_menu)
        rotate_right_column = SubmenuItem(text="Right Column", submenu=self.column_rotation_direction_menu, menu=self.rotation_menu)

        self.column_rotation_menu.append_item(rotate_left_column)
        self.column_rotation_menu.append_item(rotate_middle_column)
        self.column_rotation_menu.append_item(rotate_right_column)

        #Add faces to face rotation menu
        rotate_left_face = SubmenuItem(text="Left Face", submenu=self.face_rotation_direction_menu, menu=self.rotation_menu)
        rotate_right_face = SubmenuItem(text="Right Face", submenu=self.face_rotation_direction_menu, menu=self.rotation_menu)
        rotate_front_face = SubmenuItem(text="Front Face", submenu=self.face_rotation_direction_menu, menu=self.rotation_menu)
        rotate_middle_face = SubmenuItem(text="Middle Face", submenu=self.face_rotation_direction_menu, menu=self.rotation_menu)
        rotate_back_face = SubmenuItem(text="Back Face", submenu=self.face_rotation_direction_menu, menu=self.rotation_menu)
        rotate_bottom_face = SubmenuItem(text="Bottom Face", submenu=self.face_rotation_direction_menu, menu=self.rotation_menu)
        rotate_top_face = SubmenuItem(text="Top Face", submenu=self.face_rotation_direction_menu, menu=self.rotation_menu)

        self.face_rotation_menu.append_item(rotate_front_face)
        self.face_rotation_menu.append_item(rotate_middle_face)
        self.face_rotation_menu.append_item(rotate_back_face)

    def attach_cube_menus(self):
        #Append sections to view cube menu  
        #self.front_face_item = ConsoleMenu(title=f"Cube {self.current_cube_index}", subtitle="Front", prologue_text=self.current_cube_string, formatter=self.menu_format, show_exit_option=True, exit_option_text="Back")
        #self.back_face_item = ConsoleMenu(title=f"Cube: {self.current_cube_index}", subtitle="Back", prologue_text=f"Cube: {cube_str} \n Face: {self.face_str}", formatter=self.menu_format, show_exit_option=True, exit_option_text="Back")
        # self.left_face_item = ConsoleMenu(title=f"Cube: {self.current_cube_index}", subtitle="Left", prologue_text=f"Cube: {cube_str} \n Face: {self.face_str}", formatter=self.menu_format, show_exit_option=True, exit_option_text="Back")
        # self.right_face_item = ConsoleMenu(title=f"Cube: {self.current_cube_index}", subtitle="Right", prologue_text=f"Cube: {cube_str} \n Face: {self.face_str}", formatter=self.menu_format, show_exit_option=True, exit_option_text="Back")
        # self.top_face_item = ConsoleMenu(title=f"Cube: {self.current_cube_index}", subtitle="Top", prologue_text=f"Cube: {cube_str} \n Face: {self.face_str}", formatter=self.menu_format, show_exit_option=True, exit_option_text="Back")
        # self.bottom_face_item = ConsoleMenu(title=f"Cube: {self.current_cube_index}", subtitle="Bottom", prologue_text=f"Cube: {cube_str} \n Face: {self.face_str}", formatter=self.menu_format, show_exit_option=True, exit_option_text="Back")
        
        #self.cube_menu.append_item(self.front_face_item)
        # self.cube_menu.append_item(self.back_face_item)
        # self.cube_menu.append_item(self.left_face_item)
        # self.cube_menu.append_item(self.right_face_item)
        # self.cube_menu.append_item(self.top_face_item)
        # self.cube_menu.append_item(self.bottom_face_item)
        pass

    #Connect relevant menus to each other
    def connect_menus(self):

        self.attach_base_menus()
        self.attach_operation_items()
        self.attach_rotate_menus()
        self.attach_cube_menus()

    def play(self):
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
    
    def get_cube_string(self) ->str:
        cube = self.cubes[self.current_cube_index].cube_to_string()
        return cube
    
    def get_face_string(self) ->str:
        pass
    
    def randomize_cube(self) -> None:
        a = "We don't have randomize in yet"


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
