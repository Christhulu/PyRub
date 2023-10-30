
class Face(object):

    #Default constructor
    def __init__(self, color:str, opposite:str, side_length: int):
        self.color = color
        self.opposite = opposite
        self.side_length = side_length
        self.cells:list[list[str]] = [[color] * side_length] * side_length

        self.list_view:list[str] = []
        self.flatten_face()

        #Tracks if they're all the same color, on initialization they are
        #I don't want to keep this updated constantly, I think I'll have a button or something that they can use to check uniformity that will update this
        self.all_uniform = True

    #String representation of face
    def __str__(self):
        #represent all of face object's fields out in a human readable format
        return f'Color: {self.color}, Opposite Color: {self.opposite}, Cells: {self.cells}'

    #Function representation of face
    def __repr__(self):
        #represent face in a human readable format
        return f'Face(Color: {self.color}, Opposite Color: {self.opposite}, All cells the same: {self.all_uniform})'

    #Flatten face into list
    def flatten_face(self) -> None:
        self.list_view = [item for rowlist in self.cells for item in rowlist]

    #Check if face is all one color by checking list version of face as a set
    def validate_cell_uniformity(self) -> bool:
        self.flatten_face()
        set_view = set(self.list_view)
        self.all_uniform = len(set_view) == 1
        return self.all_uniform

    #Print face
    def print_face(self) -> None:
        for i in self.cells:
            print('\t'.join(map(str, i)))

    #Print face in flattened list view
    def print_list_view(self) -> None:
        print(self.list_view)

    #Print in row order
    def print_rows(self) -> None:
        for row in self.cells:
            print(f"\t {row}")
        pass

    #Print in column order
    def print_columns(self) -> None:

        for index in range(0, self.side_length):
            col = self.get_column(index)
            print(f"\t {col}")
        pass

    #Used in print row and also for when we need to rotate something
    #Get row by index with 0 being the top and 2 being the bottom row
    def get_row(self, index:int) -> list[str]:

        try:
            row = self.cells[index]
        except IndexError:
            print("index: {index} out of range for face")
        else:
            return row

    #Get column by index with 0 being the leftmost 2 being the rightmost column
    def get_column(self, index: int) -> list[str]:

        try:
            col = [i[index] for i in self.cells]
        except IndexError:
            print("index: {index} out of range for face")
        else:
            return col

    #Rotates face 90 degrees clockwise on the X axis
    def rotate_CW(self) -> None:
        n = self.side_length

        #Transpose face matrix
        for i in range(n) :
            for j in range(i + 1, n) :
                self.cells[i][j], self.cells[j][i] = self.cells[j][i], self.cells[i][j]

        #Reverse rows
        for i in range(n // 2) :
            top = 0
            bot = n - 1
            while (top < bot):
                self.cells[i][top], self.cells[i][bot] = self.cells[i][bot], self.cells[i][top]
                top += 1
                bot -= 1

    #Rotates face 90 degrees counter-clockwise on the X axis
    def rotate_CCW(self) -> None:
        n = self.side_length

        #Transpose face matrix
        for i in range(n):
            for j in range(i,n):
                self.cells[i][j], self.cells[j][i] = self.cells[j][i], self.cells[i][j]

        #Reverse columns
        for i in range(n):
            for j in range (int(n/2)):
                self.cells[n-j-1][i], self.cells[j][i] = self.cells[j][i], self.cells[n-j-1][i]

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

        #Get bottom row of top, right column of top, top row of top, left column of top
        #Rotate top face 90 degrees clockwise
        self.front.cells[0], self.left.cells[0], self.back.cells[0], self.right.cells[0] = left_top, back_top, right_top, front_top
        self.top.rotate_CCW()

    def rotate_top_left(self):
        #Get top row of front, right, back, and left side
        front_top = self.front.get_row(0)
        right_top = self.right.get_row(0)
        back_top = self.back.get_row(0)
        left_top = self.left.get_row(0)

        self.front.cells[0], self.right.cells[0], self.back.cells[0], self.left.cells[0] = right_top, back_top, left_top, front_top

        #Get bottom row of top, right column of top, top row of top, left column of top
        #Rotate top face 90 degrees counter clockwise
        self.top.rotate_CW()

    #middle row rotations
    def rotate_mid_right(self):
        #Get middle row of front, right, back, and left side

        pass

    def rotate_mid_left(self):
        #Get middle row of front, right, back, and left side
        pass


    #bottom row rotations
    def rotate_bottom_right(self):
        #Get bottom (last) row of front, right, back, and left side
        #Swap to the right

        #Rotate bottom face right 90 degrees clockwise
        pass

    def rotate_bottom_left(self):
        #Get bottom (last) row of front, right, back, and left side
        #Swap to the left

        #Rotate bottom face right (90 degrees clockwise)
        pass

    ##
    # Column Operations #
    ##
    #left column rotations
    def rotate_left_column_up(self):

        #Get left column of front, top faces
        #Get right column of back face
        #Get left column of bottom face

        #Rotate left face left (90 degrees counter clockwise)
        pass

    def rotate_left_column_down(self):

        #Get left column of front, top faces
        #Get right column of back face
        #Get left column of bottom face

        #Rotate left face right (90 degrees clockwise)
        pass

    #middle column rotations
    def rotate_mid_column_up(self):
        #Get middle column of front, top, back, and bottom face
        pass

    def rotate_mid_column_down(self):
        #Get middle column of front, top, back, and bottom face
        pass


    #right column rotations
    def rotate_right_column_up(self):
        #Get right column of front, top face
        #Get left column of left
        #Get right column of bottom face

        #Rotate right face left (90 degrees clockwise)
        pass

    def rotate_right_column_down(self):
        #Get right column of front, top face
        #Get left column of back face
        #Get right column of bottom face

         #Rotate right face left (90 degrees counter clockwise)
        pass



    #These move faces as a whole, so that the user is viewing a different face
    #Will address these later after I get the base rotations down
    def flip(self):
        pass


##Test area
my_cube = Cube()

#my_cube.print_cube()
# my_cube.print_cube_by_cols()
# my_cube.print_cube_by_rows()
my_cube.rotate_top_right()

my_cube.print_cube()
#Print list views to check
# my_cube.front.print_list_view()
# my_cube.back.print_list_view()
# my_cube.top.print_list_view()
# my_cube.bottom.print_list_view()
# my_cube.left.print_list_view()
# my_cube.right.print_list_view()
