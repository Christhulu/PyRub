
class Face(object):

    #Default constructor
    def __init__(self, color:str, opposite:str, side_length: int):
        self.color = color
        self.opposite = opposite
        self.side_length = side_length
        self.cells:list[list[str]] = []

        for i in range(self.side_length):
            row = []
            for j in range(self.side_length):
                row.append(color)
            self.cells.append(row)

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

        row:list[str] = []
        try:
            row.extend(self.cells[index])
        except IndexError:
            print("index: {index} out of range for face")
        else:
            return row

    #Get column by index with 0 being the leftmost 2 being the rightmost column
    def get_column(self, index: int) -> list[str]:

        col:list[str] = []
        try:
            col.extend([i[index] for i in self.cells])
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

    # With these, I'm not sure if I want a face to know that another face exists
    # But I think passing a list to it would probably be fine
    # Should have an orientation
    # This orientation reflects if the row will be descending (i.e. top to bottom) or ascending (bottom to top)
    # This would basically affect which order we read the row from
    # True for ascending, False for descending
    # Use case: Rotating the front head on would also require the bottom row of the top face to swap with the innermost columns on the left or the right face and
    # require for the top row of the bottom face to swap with the inner most column on the left or right side
    def swap_row_with_col(self, row: list[str], col: int, ascending: bool) -> list[str]:

        old_col:list[str] = []

        if ascending:
            for i in range(self.side_length):
                #Get old cell in column
                old_col.append(self.cells[i][col])

                #Swap col with row
                row[i], self.cells[i][col] = self.cells[i][col], row[i]

        else:
            for i in range(self.side_length):
                #Get old cell in column
                old_col.append(self.cells[i][col])

                #Swap col with row
                row[self.side_length - i - 1], self.cells[i][col] = self.cells[i][col], row[self.side_length - i - 1]

        return old_col

    # Should have an orientation
    # This orientation reflects if the row will be descending (i.e. top to bottom) or ascending (bottom to top)
    # This would basically affect which order we read the column from
    # True for ascending, False for descending
    # Use case: Rotating the front head on would also require the innermost columns on the left or the right face to swap with the bottom row of the top face
    # and the top row of the bottom face depending on the direction
    def swap_col_with_row(self, col: list[str], row: int, ascending: bool) -> list[str]:
        old_row:list[str] = []

        # 0 - 1 - 2 becomes 0 - 1 - 2
        if ascending:
            for i in range(self.side_length):
                old_row.append(self.cells[row][i])
                col[i], self.cells[row][i] = self.cells[row][i], col[i]
        else:
            for i in range(self.side_length):
                old_row.append(self.cells[row][i])
                col[self.side_length - i - 1], self.cells[row][i] = self.cells[row][i], col[self.side_length - i - 1]

        return old_row

    # I think for these, they'll always be in the same orientation
    # The top of one column is also the top of another if we rotate
    def swap_col_with_col(self, col: list[str], col_index: int, ascending: bool) -> list[str]:

        old_col:list[str] = []

        if ascending:
            # print(f"Ascending Loop:\n")
            # for row_index, row in enumerate(self.cells):
            for i in range(self.side_length):
                #get cell and add to list
                old_col.append(self.cells[i][col_index])

                # print(f"Old Cell: [{i}, {col_index}]: {self.cells[i][col_index]}")
                # print(f"Col Value: [{i}]: {col[i]}")

                #swap in place with list
                self.cells[i][col_index] = col[i]

                # print(f"New Cell: [{i}, {col_index}]: {self.cells[i][col_index]}\n")
                self.front.print_rows()

        else:
            # print(f"Descending Loop:\n")
            # for row_index, row in enumerate(self.cells):
            for i in range(self.side_length):
                #get cell and add to list
                old_col.append(self.cells[i][col_index])

                # print(f"Old Cell: [{i}, {col_index}]: {old_cell}")
                # print(f"Col Value: [{self.side_length - i - 1}]: {col[self.side_length - i - 1]}")

                #swap in place with list
                self.cells[i][col_index], col[self.side_length - i - 1] = col[self.side_length - i - 1], self.cells[i][col_index]

                # print(f"New Cell: [{i}, {col_index}]: {self.cells[i][col_index]}")

        return old_col

    #Replace row with passed row with front to back or back to front orientation
    def replace_row_with_row(self, row: list[str], row_index: int, ascending: bool) -> None:
        # 0 - 1 - 2 becomes 0 - 1 - 2
        if ascending:
            for i in range(len(self.cells[row_index])):
                #Replace cell at [row][i] with cell at row[i]
                self.cells[row_index][i] = row[i]
        else:
            for i in range(self.side_length):
                self.cells[row_index][i] = row[self.side_length - i - 1]

    #Replace row with passed column with top to bottom or bottom to top orientation
    def replace_row_with_col(self, col: list[str], row_index: int, ascending: bool) -> None:
        # 0 - 1 - 2 becomes 0 - 1 - 2
        if ascending:
            for i in range(self.side_length):
                #Replace cell at [row][i] with cell at col[i]
                self.cells[row_index][i] = col[i]
        else:
            for i in range(self.side_length):
                self.cells[row_index][i] = col[self.side_length - i - 1]


    #Replace column with passed row with front to back or back to front orientation
    def replace_col_with_row(self, row: list[str], col_index: int, ascending: bool) -> None:

        if ascending:
            for i in range(self.side_length):
                #Replace cell at [i][col] with cell at row[i]
                self.cells[i][col_index] = row[i]
        else:
            for i in range(self.side_length):
                #Replace cell at [i][col] with cell at row[i]
                self.cells[i][col_index] = row[self.side_length - i - 1]

    #Replace column with passed column with top to bottom or bottom to top orientation
    def replace_col_with_col(self, col: list[str], col_index: int, ascending: bool) -> None:
        if ascending:
            # print("Ascending")
            for i in range(self.side_length):
                #Replace cell at [i][col] with cell at col[i]
                self.cells[i][col_index] = col[i]
        else:
            # print("Descending")
            for i in range(self.side_length):
                #Replace cell at [i][col] with cell at col[self.side_length - i - 1]
                self.cells[i][col_index] = col[self.side_length - i - 1]

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
        pass

    def rotate_middle_face_right(self):
        pass

    def rotate_back_face_left(self):
        pass

    def rotate_back_face_right(self):
        pass
    #These move faces as a whole, so that the user is viewing a different face
    #Will address these later after I get the base rotations down
    def flip(self):
        pass