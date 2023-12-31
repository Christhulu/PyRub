from pyrub.face import Face
from types import FunctionType
import random

class Cube(object):
    """
        The base cube class for a 3x3 Rubik's cube.
        This extends the object class.

        Attributes:
            front - The Front face of the cube
    """

    #region Cube Constructor
    
    def __init__(self):
        self.opposites:dict[str, str] = {'o': 'r', 'r':'o', 'g': 'b', 'b':'g', 'y':'w', 'w':'y'}
        self.side_length:int = 3

        self.front =  Face("o", self.side_length)
        self.back = Face("r", self.side_length)
        self.left = Face("g", self.side_length)
        self.right = Face("b", self.side_length)
        self.top = Face("y", self.side_length)
        self.bottom = Face("w", self.side_length)

    #endregion Cube Constructor

    #region Cube Display Methods

    def cube_to_string(self) -> str:
        """
            Purpose: 
        """
        cube = "Front:\n"
        cube += self.front.face_to_string()
        cube += "\n"

        cube += "Back:\n"
        cube += self.back.face_to_string()
        cube += "\n"

        cube += "Left:\n"
        cube += self.left.face_to_string()
        cube += "\n"

        cube += "Right:\n"   
        cube += self.right.face_to_string()
        cube += "\n"

        cube += "Top:\n"
        cube += self.top.face_to_string()
        cube += "\n"

        cube += "Bottom:\n"
        cube += self.bottom.face_to_string()
        cube += "\n"
        
        return cube

    #Faces: Front: 0, Back: 1, Left: 2, Right: 3, Top: 4, Bottom: 5
    def face_to_string(self, face:int) -> str:
        """
            Purpose:
                This method returns a string corresponding to the face int that is passed

            Args:
                self (Cube) - The instance of cube that is calling this method
                face (int) - An integer variable corresponding to the face that we want
                
            Return Type:
                str
        """
        if face == 0:
            return self.front.face_to_string()
        elif face == 1:
            return self.back.face_to_string()
        elif face == 2:
            return self.left.face_to_string()
        elif face == 3:
            return self.right.face_to_string()
        elif face == 4:
            return self.top.face_to_string()
        else:
            return self.bottom.face_to_string()

     #endregion Cube Display Methods

    #region Cube Completeness Checks
    
    #Check if all are solved
    def check_solved(self) -> bool:
        """
            This method checks if all sides are solved.

            Args:
                self - The instance of cube that is calling this method
        """
        front_is_solved = self.front.validate_cell_uniformity()
        back_is_solved = self.back.validate_cell_uniformity()
        top_is_solved = self.top.validate_cell_uniformity()
        bottom_is_solved = self.bottom.validate_cell_uniformity()
        left_is_solved = self.left.validate_cell_uniformity()
        right_is_solved = self.right.validate_cell_uniformity()

        return front_is_solved and back_is_solved and top_is_solved and bottom_is_solved and left_is_solved and right_is_solved



    def check_side(self, side: int) -> bool:
        """
            This method takes in an int parameter called side, that checks a specific side for if it's solved (homogeneous)

            Args:
                self (Cube) - The instance of cube that is calling this method
                side(int) - Corresponds to a side and is the range [0,5]
                Front: 0, Back: 1, Top: 2, Bottom: 3, Left: 4, Right: 5
        """

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



    def print_solved_sides(self) -> None:
        """
            This method prints which sides are solved
            Args:
                self (Cube) - The instance of cube that is calling this method
        """

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

    #endregion Cube Completeness Checks

    #region Rotations

    #region Row Operations
    #region Top Row Rotations
    def rotate_top_row_right(self):
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

    def rotate_top_row_left(self):
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
    #endregion Top Row Rotations

    #region Middle Row Rotations
    def rotate_middle_row_right(self):
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

    def rotate_middle_row_left(self):
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
    
    #endregion Middle Row Rotations

    #region Bottom Row Rotations
    def rotate_bottom_row_right(self):
        #Get bottom (last) row of front, right, back, and left side
        front_bottom_row = self.front.get_row(2)
        right_bottom_row = self.right.get_row(2)
        back_bottom_row = self.back.get_row(2)
        left_bottom_row = self.left.get_row(2)

        #Swap all bottom row faces in order
        self.front.replace_row_with_row(left_bottom_row, 2, True)   
        self.right.replace_row_with_row(front_bottom_row, 2, True)    
        self.back.replace_row_with_row(right_bottom_row, 2, True)    
        self.left.replace_row_with_row(back_bottom_row, 2, True)

        #Rotate bottom face right 90 degrees clockwise
        self.bottom.rotate_CW()

    def rotate_bottom_row_left(self):
        #Get bottom (last) row of front, right, back, and left side
        front_bot = self.front.get_row(2)
        right_bot = self.right.get_row(2)
        back_bot = self.back.get_row(2)
        left_bot = self.left.get_row(2)

        #Swap all bottom row faces in order
        self.front.replace_row_with_row(right_bot, 2, True)
        self.right.replace_row_with_row(back_bot, 2, True) 
        self.back.replace_row_with_row(left_bot, 2, True)
        self.left.replace_row_with_row(front_bot, 2, True)  

        #Rotate bottom face right (90 degrees counter-clockwise)
        self.bottom.rotate_CCW()

    #endregion Bottom Row Rotations
    #endregion Row Operations

    #region Column Operations

    #region Left Column Rotations
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
    #endregion Left Column Rotations

    #region Middle Column Rotations
    def rotate_middle_column_up(self):
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

    def rotate_middle_column_down(self):
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

    #endregion Middle Column Rotations

    #region Right Column Rotations
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

    #endregion Right Column Rotations
    #endregion Column Operations

    #region Face Operations

    #region Front Face Operations
    def rotate_front_face_CCW(self):
        """
        This method rotates the front face of the cube counter-clockwise.
        Args:
            self - The current face instance
        """
        
        #rotate front 90 degrees counter-clockwise
        self.front.rotate_CCW()
        
        #Get bottom row of top face
        #Get right column of left face
        #Get left column of right face
        #Get top row of bottom face
        top_bottom_row = self.top.get_row(2)
        left_right_column = self.left.get_column(2)
        right_left_column = self.right.get_column(0)
        bottom_top_row = self.bottom.get_row(0)

        #Replace columns with each other
        self.left.replace_col_with_row(top_bottom_row, 2, False)
        self.top.replace_row_with_col(right_left_column, 2, True)
        self.right.replace_col_with_row(bottom_top_row, 0, False)
        self.bottom.replace_row_with_col(left_right_column, 0, True)


    def rotate_front_face_CW(self):
        """
        This method rotates the front face of the cube clockwise.
        Args:
            self - The current face instance
        """
        #rotate front 90 degrees clockwise
        self.front.rotate_CW()
        
        #Get bottom row of top face
        #Get right column of left face
        #Get left column of right face
        #Get top row of bottom face
        top_bottom_row = self.top.get_row(2)
        left_right_column = self.left.get_column(2)
        right_left_column = self.right.get_column(0)
        bottom_top_row = self.bottom.get_row(0)

        #Replace columns with each other
        self.left.replace_col_with_row(bottom_top_row, 2, True)
        self.top.replace_row_with_col(left_right_column, 2, False)
        self.right.replace_col_with_row(top_bottom_row, 0, True)
        self.bottom.replace_row_with_col(right_left_column, 0, False)

    #endregion Front Face Operations

    #region Left Face Operations
    def rotate_left_face_CCW(self):
        """
        This method rotates the left face of the cube counter-clockwise.
        (It's replicated from a different section, but for readability, it's named like this here)
        Args:
            self - The current face instance
        """
        self.rotate_left_column_up()

    def rotate_left_face_CW(self):
        """
        This method rotates the left face of the cube clockwise.
        (It's replicated from a different section, but for readability, it's named like this here)
        Args:
            self - The current face instance
        """
        self.rotate_left_column_down()

    #endregion Left Face Operations

    #region Right Face Operations
    def rotate_right_face_CCW(self):
        """
        This method rotates the right face of the cube counter-clockwise.
        (It's replicated from a different section, but for readability, it's named like this here)
        Args:
            self - The current face instance
        """
        self.rotate_right_column_down()

    def rotate_right_face_CW(self):
        """
        This method rotates the right face of the cube clockwise.
        (It's replicated from a different section, but for readability, it's named like this here)
        Args:
            self - The current face instance
        """
        self.rotate_right_column_up()

    #endregion Right Face Operations
    
    #region Top Face Operations
    def rotate_top_face_CW(self):
        """
        This method rotates the top face of the cube clockwise.
        Args:
            self - The current face instance
        """
        #This is just rotating the top row left
        self.rotate_top_row_left()


    def rotate_top_face_CCW(self):
        """
        This method rotates the top face of the cube counter-clockwise.
        Args:
            self - The current face instance
        """
        #This is just rotating the top row right
        self.rotate_top_row_right()
    
    #endregion Top Face Operations

    #region Bottom Face Operations
    def rotate_bottom_face_CW(self):
        """
        This method rotates the top face of the cube clockwise.
        Args:
            self - The current face instance
        """
        self.rotate_bottom_row_right()

    def rotate_bottom_face_CCW(self):
        """
        This method rotates the top face of the cube counter-clockwise.
        Args:
            self - The current face instance
        """
        self.rotate_bottom_row_left()

    #endregion Bottom Face Operations

    #region Middle Face Operations
    def rotate_middle_face_CCW(self):
        """
        This method rotates the middle face of the cube counter-clockwise.
        Args:
            self - The current face instance
        """
        #Get top face's middle row
        #Get left face's middle column
        #Get bottom face's middle row
        #Get right face's middle column
        top_mid_row = self.top.get_row(1)
        left_mid_column = self.left.get_column(1)
        bottom_mid_row = self.bottom.get_row(1)
        right_mid_column = self.right.get_column(1)

        #Replace top middle row with right middle column, ascending order
        #Replace right middle column with bottom middle row, descending order
        #Replace bottom middle row with left middle column, ascending order
        #Replace left middle column  with top middle row, descending order
        self.top.replace_row_with_col(right_mid_column, 1, True)
        self.right.replace_col_with_row(bottom_mid_row, 1, False)
        self.bottom.replace_row_with_col(left_mid_column, 1, True)
        self.left.replace_col_with_row(top_mid_row, 1, False)


    def rotate_middle_face_CW(self):
        """
        This method rotates the middle face of the cube clockwise.
        Args:
            self - The current face instance
        """
        #Get top face's middle row
        #Get right face's middle column
        #Get bottom face's middle row
        #Get left face's middle column
        top_mid_row = self.top.get_row(1)
        right_mid_column = self.right.get_column(1)
        left_mid_column = self.left.get_column(1)
        bottom_mid_row = self.bottom.get_row(1)


        #Replace top middle row with left middle column, descending order
        #Replace right middle column with top middle row, ascending order
        #Replace bottom middle row with right middle column, descending order
        #Replace left middle column with bottom middle row, ascending order
        self.top.replace_row_with_col(left_mid_column, 1, False)
        self.right.replace_col_with_row(top_mid_row, 1, True)
        self.bottom.replace_row_with_col(right_mid_column, 1, False)
        self.left.replace_col_with_row(bottom_mid_row, 1, True)

    #endregion Middle Face Operations
    
    #region Back Face Operations
    def rotate_back_face_CCW(self):
        """
        This method rotates the back face of the cube counter-clockwise.
        Args:
            self - The current face instance
        """
        #Rotate back face counter clockwise
        self.back.rotate_CCW()

        #Get top face's top row
        #Get right face's right column
        #Get bottom face's bottom row
        #Get left face's left column
        top_top_row = self.top.get_row(0)
        right_right_column = self.right.get_column(2)
        bottom_bottom_row = self.bottom.get_row(2)
        left_left_column = self.left.get_column(0)


        #Replace top face's top row with left face's left column, descending order
        #Replace right face's right column with top face's top row, ascending order
        #Replace bottom face's bottom row with right face's right column, descending order
        #Replace left face's left column with top face's top row, ascending order
        self.top.replace_row_with_col(left_left_column, 0, False)
        self.right.replace_col_with_row(top_top_row, 2, True)
        self.bottom.replace_row_with_col(right_right_column, 2, False)
        self.left.replace_col_with_row(bottom_bottom_row, 0, True)

    def rotate_back_face_CW(self):
        """
        This method rotates the back face of the cube clockwise.
        Args:
            self - The current face instance
        """

        #Rotate back face clockwise
        self.back.rotate_CW()

        #Get top face's top row
        #Get right face's right column
        #Get bottom face's bottom row
        #Get left face's left column
        top_top_row = self.top.get_row(0)
        right_right_column = self.right.get_column(2)
        bottom_bottom_row = self.bottom.get_row(2)
        left_left_column = self.left.get_column(0)

        #Replace top face's top row with right face's right column, ascending order
        #Replace right face's right column with bottom face's bottom row, descending order
        #Replace bottom face's bottom row with left face's left column, ascending order
        #Replace left face's left column with top face's top row, descending order
        self.top.replace_row_with_col(right_right_column, 0, True)
        self.right.replace_col_with_row(bottom_bottom_row, 2, False)
        self.bottom.replace_row_with_col(left_left_column, 2, True)
        self.left.replace_col_with_row(top_top_row, 0, False)



    #endregion Back Face Operations

    #endregion Face Operations

    #endregion Rotations

    #region Cube Helper Methods


    def set_cube_methods(self):
        """
        Purpose:\n
        This method gets the list of methods for the cube from its __dict__ and groups them into a list for the cube instance.\n
        Args:\n
            * self: The current face instance\n
        """
        #Hold a list of the methods you can do on this cube
        self.methods = [y for x, y in Cube.__dict__.items() if type(y) == FunctionType and (x.startswith('rot') and not x.startswith('_'))]

    def choose_number_of_random_operations(self, min:int, max:int):

        num_operations = random.randint(min, max)
        return num_operations

    def choose_random_operations(self, num_operations):
        
        op_list = [None]*num_operations

        for i in range(num_operations):
            op_list[i] = random.choice(self.methods)

        return op_list

    def choose_random_operation(self):
        func = random.choice(self.methods)
        return func


    def randomize_cube(self):
        """
        Purpose:\n
        This method gets the list of methods for the cube face, selects a random set of them, and enacts them on the cube.\n
        I can probably exclude certain methods with a pattern or just make a list with the method names. I'll play around with it
        Args:\n
            * self: The current face instance\n
        """

        self.set_cube_methods()
        num_operations = self.choose_number_of_random_operations(10, 30)

        #This works because we're just rotating, which shouldn't require any parameters
        for i in range(num_operations):
            op = self.choose_random_operation()
            op(self)


    #endregion Cube Helper Methods

    #region Shift Cube Orientation Operations
    #These move faces as a whole, so that the user is viewing a different face
    #Will address these later after I get the base rotations down
    def change_front(self, index: int):
        """
        Purpose:\n
        This method selects a method to update the front face based on the index parameter that is passed.\n
        Args:\n
            * self: The current face instance\n
            * index (int): The index corresponding to the new face (not including front itself)\n\n
         
            Notes: What each index means: Left - 0, Back - 1, Right - 2, Top - 3, Bottom - 4\n
        """
        match index:
            case 0:
                self.set_back_to_front()
            case 1:
                self.set_left_to_front()
            case 2:
                self.set_right_to_front()
            case 3:
                self.set_top_to_front()
            case 4:
                self.set_bottom_to_front()
        

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

    #endregion Shift Cube Orientation Operations