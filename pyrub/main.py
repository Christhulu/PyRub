from rubiks import Cube
from rubiks import Face
from consolemenu import *
from consolemenu.items import *


# Create the menu
menu = ConsoleMenu("PyRub", "A Console Application for solving Rubik's Cubes")
# A SelectionMenu constructs a menu from a list of strings
options_menu = SelectionMenu(["Play", "Help", "Quit"])

submenu_item = SubmenuItem("Submenu item", options_menu, menu)

menu.append_item(submenu_item)

menu.show()
