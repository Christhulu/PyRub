from rubiks import Cube
from rubiks import Face
from consolemenu import *
from consolemenu.items import *

def main():

    my_cube = Cube()



# Create the menu
    home_menu = ConsoleMenu("PyRub", "A Console Application for solving Rubik's Cubes")
    # A SelectionMenu constructs a menu from a list of strings
    options_menu = SelectionMenu(["Play", "Help"], "Options", "Select an option.",show_exit_option=True)

    submenu_item = SubmenuItem(options_menu, home_menu)

    home_menu.append_item(submenu_item)

    home_menu.show()


    #Cube Display (This is the visual display for the cube)



    #Operations Menu
    # Start a New Cube
    # Print Current Cube (if Applicable)
    # Rotate a row, column, or face
    # Randomize Cube
    # Instantly "Solve" Cube
    # Exit


    #Rotate Menu
    # 0. Rotate Row
    # 1. Rotate Column
    # 2. Rotate Face


    # Rotate Row Menu
    # Which row would you like to rotate?
    # 0. Row 0 (Top Row)
    # 1. Row 1 (Middle Row)
    # 2. Row 2 (Bottom Row)

    # Rotate Column Direction
    # Which direction would you like to rotate the row?
    # 0. Left
    # 1. Right


    # Rotate Column Menu
    # Which column would you like to rotate?
    # 0. Column 0 (Top Row)
    # 1. Column 1 (Middle Row)
    # 2. Column 2 (Bottom Row)

    # Rotate Column Direction
    # Which direction would you like to rotate the column?
    # 0. Up
    # 1. Down

    # Rotate Face Menu
    # 0. Front
    # 1. Middle
    # 2. Back

    #Advance to the main foothold. Hold the main foothold to defeat the enemy.
    # Rotate Face Direction
    # Subtitle: *Face*
    # 0 - Clockwise
    # 1 - Counter Clockwise

    # Choose a new Front relative to the current front of the cube:
    # 0 - Front
    # 1 - Right
    # 2 - Back
    # 3 - Left
    # 4 - Top
    # 5 - Bottom





    

if __name__=="__main__":
    main() 
