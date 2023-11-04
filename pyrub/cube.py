from face import Face

class Cube():

    def __init__(self):
        self.front =  Face("o", "r", 3)
        self.back = Face("r", "o", 3)
        self.left = Face("g", "b", 3)
        self.right = Face("b", "g", 3)
        self.top = Face("y", "w", 3)
        self.bottom = Face("w", "y", 3)

    def print_cube(self) -> None:

        print(f"Front:")
        self.front.print_face()

        print(f"Back:")
        self.back.print_face()

        print(f"Left:")
        self.left.print_face()

        print(f"Right:")
        self.right.print_face()

        print(f"Top:")
        self.top.print_face()

        print(f"Bottom:")
        self.bottom.print_face()

    def cube_to_string(self) -> str:

        cube = ""
        cube += self.front.face_to_string()
        cube += "\n"

        cube += self.back.face_to_string()
        cube += "\n"

        cube += self.left.face_to_string()
        cube += "\n"

        cube += self.right.face_to_string()
        cube += "\n"

        cube += self.top.face_to_string()
        cube += "\n"

        cube += self.bottom.face_to_string()
        cube += "\n"
        
        return cube

    #Faces: Front: 0, Right: 1, Back: 2, Left: 3, Top: 4, Bottom: 5
    def face_to_string(self, face:int) -> str:
        
        face = ""
        match face:
            case 0:
                face += self.front.face_to_string()
            case 1:
                face += self.right.face_to_string()
            case 2:
                face += self.back.face_to_string()
            case 3:
                face += self.left.face_to_string()
            case 4:
                face += self.top.face_to_string()
            case 5:
                face += self.bottom.face_to_string()
        
        return face

    def print_cube_by_rows(self) -> None:
        print(f"Front:")
        self.front.print_rows()

        print(f"Back:")
        self.back.print_rows()

        print(f"Left:")
        self.left.print_rows()

        print(f"Right:")
        self.right.print_rows()

        print(f"Top:")
        self.top.print_rows()

        print(f"Bottom:")
        self.bottom.print_rows()

    def print_cube_by_cols(self) -> None:
        print(f"Front:")
        self.front.print_columns()

        print(f"Back:")
        self.back.print_columns()

        print(f"Left:")
        self.left.print_columns()

        print(f"Right:")
        self.right.print_columns()

        print(f"Top:")
        self.top.print_columns()

        print(f"Bottom:")
        self.bottom.print_columns()

    #Check if all are solved
    def check_solved(self) -> bool:

        front_is_solved = self.front.validate_cell_uniformity()
        back_is_solved = self.back.validate_cell_uniformity()
        top_is_solved = self.top.validate_cell_uniformity()
        bottom_is_solved = self.bottom.validate_cell_uniformity()
        left_is_solved = self.left.validate_cell_uniformity()
        right_is_solved = self.right.validate_cell_uniformity()

        return front_is_solved and back_is_solved and top_is_solved and bottom_is_solved and left_is_solved and right_is_solved

    #Check a specific side for if it's solved
    #Front: 0
    #Back: 1
    #Top: 2
    #Bottom: 3
    #Left: 4
    #Right: 5
    def check_side(self, side: int) -> bool:
        solved = False
        match side:
            case 0:
                solved = self.front.validate_cell_uniformity()
            case 1:
                solved = self.back.validate_cell_uniformity()
            case 2:
                solved = self.top.validate_cell_uniformity()
            case 3:
                solved = self.bottom.validate_cell_uniformity()
            case 4:
                solved = self.left.validate_cell_uniformity()
            case 5:
                solved = self.right.validate_cell_uniformity()

        return solved


    #print which sides are solved
    def print_solved_sides(self) -> None:
        solved_sides = []

        for i in range(0, 7):
            solved_side = self.check_side(i)
            if solved_side:
                solved_sides.append(i)

        for side in solved_sides:
                match side:
                    case 0:
                        print(f"Front:")
                        solved = self.front.print_face()
                    case 1:
                        print(f"Back:")
                        solved = self.back.print_face()
                    case 2:
                        print(f"Top:")
                        solved = self.top.print_face()
                    case 3:
                        print(f"Bottom:")
                        solved = self.bottom.print_face()
                    case 4:
                        print(f"Left:")
                        solved = self.left.print_face()
                    case 5:
                        print(f"Right:")
                        solved = self.right.print_face()


    ##
    # Row Operations #
    ##

    #top row rotations
    def rotate_top_right(self):
        #Get top row of front, right, back, and left side
        front_top = self.front.get_row(0)
        right_top = self.right.get_row(0)
        back_top = self.back.get_row(0)
        left_top = self.left.get_row(0)

        #Swap all top row faces in order
        # self.front.cells[0], self.left.cells[0], self.back.cells[0], self.right.cells[0] = left_top, back_top, right_top, front_top

        self.front.replace_row_with_row(left_top, 0, True)   # self.front.cells[0] = left_top,
        self.right.replace_row_with_row(front_top, 0, True)    # self.left.cells[0] = back_top,
        self.back.replace_row_with_row(right_top, 0, True)    # self.back.cells[0] = right_top,
        self.left.replace_row_with_row(back_top, 0, True)    # self.right.cells[0] = front_top

        #Rotate top face 90 degrees counter-clockwise
        self.top.rotate_CCW()

    def rotate_top_left(self):
        #Get top row of front, right, back, and left side
        front_top = self.front.get_row(0)
        right_top = self.right.get_row(0)
        back_top = self.back.get_row(0)
        left_top = self.left.get_row(0)

        #Swap all top row faces in order
        # self.front.cells[0], self.right.cells[0], self.back.cells[0], self.left.cells[0] = right_top, back_top, left_top, front_top
        self.front.replace_row_with_row(right_top, 0, True)   # self.front.cells[0] = left_top,
        self.right.replace_row_with_row(back_top, 0, True)    # self.left.cells[0] = back_top,
        self.back.replace_row_with_row(left_top, 0, True)    # self.back.cells[0] = right_top,
        self.left.replace_row_with_row(front_top, 0, True)    # self.right.cells[0] = front_top

        #Rotate top face 90 degrees counter clockwise
        self.top.rotate_CW()

    #middle row rotations
    def rotate_mid_right(self):
        #Get middle row of front, right, back, and left side
        front_mid = self.front.get_row(1)
        right_mid = self.right.get_row(1)
        back_mid = self.back.get_row(1)
        left_mid = self.left.get_row(1)

        #Swap all middle row faces in order
        self.front.replace_row_with_row(left_mid, 1, True)   # self.front.cells[1] = left_mid,
        self.right.replace_row_with_row(front_mid, 1, True)    # self.left.cells[1] = back_mid,
        self.back.replace_row_with_row(right_mid, 1, True)    # self.back.cells[1] = right_mid,
        self.left.replace_row_with_row(back_mid, 1, True)    # self.right.cells[1] = front_mid

    def rotate_mid_left(self):
        #Get middle row of front, right, back, and left side
        front_mid = self.front.get_row(1)
        right_mid = self.right.get_row(1)
        back_mid = self.back.get_row(1)
        left_mid = self.left.get_row(1)

        #Swap all middle row faces in order
        self.front.replace_row_with_row(right_mid, 1, True)   # self.front.cells[1] = right_mid,
        self.right.replace_row_with_row(back_mid, 1, True)    # self.right.cells[1] = back_mid,
        self.back.replace_row_with_row(left_mid, 1, True)    # self.back.cells[1] = left_mid,
        self.left.replace_row_with_row(front_mid, 1, True)    # self.left.cells[1] = front_mid


    #bottom row rotations
    def rotate_bottom_right(self):
        #Get bottom (last) row of front, right, back, and left side
        front_bot = self.front.get_row(2)
        right_bot = self.right.get_row(2)
        back_bot = self.back.get_row(2)
        left_bot = self.left.get_row(2)

        #Swap all bottom row faces in order
        self.front.replace_row_with_row(left_bot, 2, True)   # self.front.cells[2] = left_bot
        self.right.replace_row_with_row(front_bot, 2, True)    # self.right.cells[2] = front_bot
        self.back.replace_row_with_row(right_bot, 2, True)    # self.back.cells[2] = right_bot
        self.left.replace_row_with_row(back_bot, 2, True)    # self.left.cells[2] = back_bot

        #Rotate bottom face right 90 degrees clockwise
        self.bottom.rotate_CW()

    def rotate_bottom_left(self):
        #Get bottom (last) row of front, right, back, and left side
        front_bot = self.front.get_row(2)
        right_bot = self.right.get_row(2)
        back_bot = self.back.get_row(2)
        left_bot = self.left.get_row(2)

        #Swap all bottom row faces in order
        self.front.replace_row_with_row(right_bot, 2, True)   # self.front.cells[2] = right_bot
        self.right.replace_row_with_row(back_bot, 2, True)    #  self.right.cells[2] = back_bot
        self.back.replace_row_with_row(left_bot, 2, True)    # self.back.cells[2] = left_bot
        self.left.replace_row_with_row(front_bot, 2, True)    #  self.left.cells[2] = front_bot

        #Rotate bottom face right (90 degrees counter-clockwise)
        self.bottom.rotate_CCW()

    ##
    # Column Operations #
    ##
    #left column rotations
    def rotate_left_column_up(self):

        #Get left column of front, top faces
        #Get right column of back face
        #Get left column of bottom face
        front_left = self.front.get_column(0)
        top_left = self.top.get_column(0)

        back_right = self.back.get_column(2)
        bottom_left = self.bottom.get_column(0)


        #Swap columns
        #Treat them all as individual calls

        self.front.replace_col_with_col(bottom_left, 0, True)
        self.top.replace_col_with_col(front_left, 0, True)
        self.back.replace_col_with_col(top_left, 2, False)
        self.bottom.replace_col_with_col(back_right, 0, False)


        #Rotate left face left (90 degrees counter clockwise)
        self.left.rotate_CCW()

    def rotate_left_column_down(self):

        #Get left column of front, top faces
        #Get right column of back face
        #Get left column of bottom face
        front_left = self.front.get_column(0)
        top_left = self.top.get_column(0)

        back_right = self.back.get_column(2)
        bottom_left = self.bottom.get_column(0)

        #Swap columns
        #Treat them all as individual calls
        #This could return none if I wanted, but I'm not sure if I want to make that
        #jump yet.
        #Maybe I should have two separate methods, one returning, and one not returning
        self.front.replace_col_with_col(top_left, 0, True)
        self.top.replace_col_with_col(back_right, 0, False)
        self.back.replace_col_with_col(bottom_left, 2, False)
        self.bottom.replace_col_with_col(front_left, 0, True)


        #Rotate left face right (90 degrees clockwise)
        self.left.rotate_CW()


    #middle column rotations
    def rotate_mid_column_up(self):
        #Get middle column of front, top, back, and bottom face
        front_mid = self.front.get_column(1)
        top_mid = self.top.get_column(1)
        back_mid = self.back.get_column(1)
        bottom_mid = self.bottom.get_column(1)

        #Note the orientations
        self.front.replace_col_with_col(bottom_mid, 1, True)
        self.top.replace_col_with_col(front_mid, 1, True)
        self.back.replace_col_with_col(top_mid, 1, False)
        self.bottom.replace_col_with_col(back_mid, 1, False)

    def rotate_mid_column_down(self):
        #Get middle column of front, top, back, and bottom face
        front_mid = self.front.get_column(1)
        top_mid = self.top.get_column(1)
        back_mid = self.back.get_column(1)
        bottom_mid = self.bottom.get_column(1)

        #Note the orientations
        self.front.replace_col_with_col(top_mid, 1, True)
        self.top.replace_col_with_col(back_mid, 1, False)
        self.back.replace_col_with_col(bottom_mid, 1, False)
        self.bottom.replace_col_with_col(front_mid, 1, True)


    #right column rotations
    def rotate_right_column_up(self):
        #Get right column of front, top face
        #Get left column of back face
        #Get right column of bottom face
        front_right = self.front.get_column(2)
        top_right = self.top.get_column(2)
        back_left = self.back.get_column(0)
        bottom_right = self.bottom.get_column(2)


        #Replace columns
        self.front.replace_col_with_col(bottom_right, 2, True)
        self.top.replace_col_with_col(front_right, 2, True)
        self.back.replace_col_with_col(top_right, 0, False)
        self.bottom.replace_col_with_col(back_left, 2, False)

        #Rotate right face left (90 degrees clockwise)
        self.right.rotate_CW()

    def rotate_right_column_down(self):
        #Get right column of front, top face
        #Get left column of back face
        #Get right column of bottom face
        front_right = self.front.get_column(2)
        top_right = self.top.get_column(2)
        back_left = self.back.get_column(0)
        bottom_right = self.bottom.get_column(2)


        #Replace columns
        self.front.replace_col_with_col(top_right, 2, True)
        self.top.replace_col_with_col(back_left, 2, False)
        self.back.replace_col_with_col(bottom_right, 0, False)
        self.bottom.replace_col_with_col(front_right, 2, True)

        #Rotate right face left (90 degrees counter clockwise)
        self.right.rotate_CCW()

    def rotate_middle_face_left(self):

        #Get top face's middle row
        #Get left face's middle column
        #Get bottom face's middle row
        #Get right face's middle column
        top_mid = self.top.get_row(1)
        left_mid = self.left.get_column(1)
        bottom_mid = self.bottom.get_row(1)
        right_mid = self.right.get_column(1)

        #Replace top middle row with right middle column, ascending order
        #Replace right middle column with bottom middle row, descending order
        #Replace bottom middle row with left middle column, ascending order
        #Replace left middle column  with top middle row, descending order
        self.top.replace_row_with_col(right_mid, 1, True)
        self.right.replace_col_with_row(bottom_mid, 1, False)
        self.bottom.replace_row_with_col(left_mid, 1, True)
        self.left.replace_col_with_row(top_mid, 1, False)


    def rotate_middle_face_right(self):
        #Get top face's middle row
        #Get right face's middle column
        #Get bottom face's middle row
        #Get left face's middle column
        top_mid = self.top.get_row(1)
        right_mid = self.right.get_column(1)
        left_mid = self.left.get_column(1)
        bottom_mid = self.bottom.get_row(1)


        #Replace top middle row with left middle column, descending order
        #Replace right middle column with top middle row, ascending order
        #Replace bottom middle row with right middle column, descending order
        #Replace left middle column with bottom middle row, ascending order
        self.top.replace_row_with_col(left_mid, 1, False)
        self.right.replace_col_with_row(top_mid, 1, True)
        self.bottom.replace_row_with_col(right_mid, 1, False)
        self.left.replace_col_with_row(bottom_mid, 1, True)

    def rotate_back_face_left(self):
        #Get top face's top row
        #Get right face's right column
        #Get bottom face's bottom row
        #Get left face's left column
        top_top = self.top.get_row(0)
        right_right = self.right.get_column(2)
        bottom_bottom = self.bottom.get_row(2)
        left_left = self.left.get_column(0)


        #Replace top face's top row with right face's right column, ascending order
        #Replace right face's right column with bottom face's bottom row, descending order
        #Replace bottom face's bottom row with left face's left column, ascending order
        #Replace left face's left column with top face's top row, descending order
        self.top.replace_row_with_col(right_right, 0, True)
        self.right.replace_col_with_row(bottom_bottom, 2, False)
        self.bottom.replace_row_with_col(left_left, 2, True)
        self.left.replace_col_with_row(top_top, 0, False)

        #Rotate back face counter clockwise
        self.back.rotate_CCW()

    def rotate_back_face_right(self):
        #Get top face's top row
        #Get right face's right column
        #Get bottom face's bottom row
        #Get left face's left column
        top_top = self.top.get_row(0)
        right_right = self.right.get_column(2)
        bottom_bottom = self.bottom.get_row(2)
        left_left = self.left.get_column(0)

        #Replace top face's top row with left face's left column, descending order
        #Replace right face's right column with top face's top row, ascending order
        #Replace bottom face's bottom row with right face's right column, descending order
        #Replace left face's left column with bottom face's bottom row, ascending order
        self.top.replace_row_with_col(left_left, 0, False)
        self.right.replace_col_with_row(top_top, 2, True)
        self.bottom.replace_row_with_col(right_right, 2, False)
        self.left.replace_col_with_row(bottom_bottom, 0, True)

        #Rotate back face clockwise
        self.back.rotate_CW()

    #These move faces as a whole, so that the user is viewing a different face
    #Will address these later after I get the base rotations down
    def change_front(self, index: int):

        match index:
            case 0:
                self.set_left_to_front()
            case 1:
                self.set_back_to_front()
            case 2:
                self.set_right_to_front()
            case 3:
                self.set_top_to_front()
            case 4:
                self.set_bottom_to_front()
        


    #These change these current face's to the front face
    #They still need more testing but I think this is how they would work
    def set_left_to_front(self):

        self.front, self.left, self.back, self.right = self.left, self.back, self.right, self.front

        #Rotate top and bottom so that they're relative to the new front
        self.top.rotate_CW()
        self.bottom.rotate_CW()

    def set_back_to_front(self):

        self.front, self.left, self.right, self.back = self.back, self.right, self.left, self.front

        self.top.rotate_CCW()
        self.top.rotate_CCW()

        self.bottom.rotate_CCW()
        self.bottom.rotate_CCW()
        

    def set_right_to_front(self):

        self.front, self.left, self.right, self.back = self.right, self.front, self.back, self.left

        self.top.rotate_CCW()
        self.bottom.rotate_CCW()

    def set_top_to_front(self):

        self.front, self.back, self.bottom, self.top = self.top, self.bottom, self.front, self.back

        #self.left same but rotated CCW
        #self.right same bot rotated CW
        self.left.rotate_CCW()
        self.right.rotate_CW()

        #top should also be upside down
        self.top.rotate_CW()
        self.top.rotate_CW()

        #back should be upside down
        self.back.rotate_CCW()
        self.back.rotate_CCW()

    def set_bottom_to_front(self):
        
        self.front, self.top, self.back, self.bottom = self.bottom, self.front, self.top, self.back

        # self.left needs to be rotated
        self.left.rotate_CW()

        # self.right need to be rotated
        self.right.rotate_CCW()

        #bottom should be upside down
        self.bottom.rotate_CW()
        self.bottom.rotate_CW()

        #back should be upside down
        self.back.rotate_CW()
        self.back.rotate_CW()