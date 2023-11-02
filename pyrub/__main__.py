from cube import Cube
from face import Face
from game import Game
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



if __name__=="__main__":
    main() 
