from cube import Cube
from face import Face
from game import Game
from consolemenu import *
from consolemenu.items import *
from consolemenu.format import *
import sys

def main():

    cube_game = Game()

    cube_game.play()


if __name__=="__main__":
    main() 
