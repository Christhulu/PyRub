class Face(object):
    """
    Purpose: This class is responsible for handling all of the details involved with a single face of the Rubik's cube.

    Args:
        color (str): This is the color this side is initialized to.
        side_length (int): This is the length of the side, and is used to set the dimensions of the face. (The face is a square)
        cells (list[list[str]]): This is what stores the face's matrix. It has side_length x side_length cells. (Right now, that's 3x3)
        all_uniform (bool): This is a variable that is updated to keep track of if all of the cells on a side are the same.
    """


    #Default constructor
    def __init__(self, color:str, side_length: int):
        """
            Purpose:\n 
            Default Constructor:\n\t
            * Initialize default variables and create matrix for cells\n
            * Also create list view for checking if this face is solved\n

            Args:\n
            * self (Face): The face that is calling this method \n
        """
        self.color:str = color
        self.side_length:int = side_length
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

    def __str__(self):
        """
        Purpose: This method represents all of this face object's fields in a human readable format \n

        Args:\n
            * self (Face): The face that is calling this method \n
        """

        return f'Cells: {self.cells}'

    def __repr__(self):
        """
        Purpose: This method also represents all of this face object's fields in a human readable format\n
        To be honest, I can't tell the difference between this and __str__, but I've added in a check for if the face is complete.\n
        
        Args:\n
            * self (Face): The face that is calling this method \n
        """
        return f'Cells: {self.cells}, Face complete: {self.validate_cell_uniformity()})'

    def flatten_face(self) -> None:
        """
        Purpose: This method flattens the face down into a single list so that we can more easily convert it to a set\n
        or just display it as a list if we want. We're using a list comprehension here.\n

        Args:\n
            * self (Face): The face that is calling this method \n
        """
        self.list_view = [item for rowlist in self.cells for item in rowlist]

    def validate_cell_uniformity(self) -> bool:
        """
        Purpose:\n 
        This method flattens the face down into a single list and then converts it to a set to make sure the cells all have the same color.\n
        If they all have the same color, the set should only have one element, and the face is solved for some color. (Doesn't have to be the original)\n

        Args:
            * self (Face): The face that is calling this method \n
        """
        self.flatten_face()
        set_view = set(self.list_view)
        self.all_uniform = len(set_view) == 1
        return self.all_uniform

    def face_to_string(self) -> str:
        """
        Purpose: This method converts the cells in the face into a string that is easy to display in the interface.

        Args:
            * self (Face): The face that is calling this method \n
        """
        face_str:str = ''
        for i in self.cells:
            face_str += '\t'.join(map(str, i))
            face_str += '\n'

        face_str += '\n'

        return face_str


    def print_list_view(self) -> None:
        """
        Purpose:
        Print face in flattened list view
        Args:
            * self (Face): The face that is calling this method \n
        """
        print(self.list_view)


    def print_rows(self) -> None:
        """
        Purpose:\n
        Print face in row order\n\n

        Args:\n
            * self (Face): The face that is calling this method \n
        """
        for row in self.cells:
            print(f"\t {row}")


    def print_columns(self) -> None:
        """
        Purpose:
        Print face in column order\n
        Args:\n
            * self (Face): The face that is calling this method \n
        """
        for index in range(0, self.side_length):
            col = self.get_column(index)
            print(f"\t {col}")


    def get_row(self, index:int) -> list[str]:
        """
        Purpose:
        Get row by index with 0 being the top row and 2 being the bottom row.\n
        Args:\n
            * self (Face): The face that is calling this method \n
        """
        row:list[str] = []
        try:
            row.extend(self.cells[index])
        except IndexError:
            print("index: {index} out of range for face")
        else:
            return row
        
    def get_column(self, index: int) -> list[str]:
        """
        Purpose:
        Get column by index with 0 being the leftmost 2 being the rightmost column\n
        Args:\n
            * self (Face): The face that is calling this method \n
        """
        col:list[str] = []
        try:
            col.extend([i[index] for i in self.cells])
        except IndexError:
            print("index: {index} out of range for face")
        else:
            return col

    def rotate_CW(self) -> None:
        """
        Purpose:
        Rotates face 90 degrees clockwise on the X axis\n
        Args:\n
            * self (Face): The face that is calling this method \n
        """
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


    def rotate_CCW(self) -> None:
        """
        Purpose:
        Rotates face 90 degrees counter-clockwise on the X axis\n
        Args:\n
            * self (Face): The face that is calling this method \n
        """
        n = self.side_length

        #Transpose face matrix
        for i in range(n):
            for j in range(i,n):
                self.cells[i][j], self.cells[j][i] = self.cells[j][i], self.cells[i][j]

        #Reverse columns
        for i in range(n):
            for j in range (int(n/2)):
                self.cells[n-j-1][i], self.cells[j][i] = self.cells[j][i], self.cells[n-j-1][i]

    def replace_row_with_row(self, row: list[str], row_index: int, ascending: bool) -> None:
        """
        Purpose: Replace row with passed row with left to right or right to left orientation\n

        Args:\n
            * row (list[str]): The row that is replacing the row at row_index\n
            * row_index (int): The index of the row that we are modifying\n
            * ascending (bool): The direction we use to read the passed row\n
        """
        if ascending:
            for i in range(len(self.cells[row_index])):
                #Replace cell at [row][i] with cell at row[i]
                self.cells[row_index][i] = row[i]
        else:
            for i in range(self.side_length):
                self.cells[row_index][i] = row[self.side_length - i - 1]


    def replace_row_with_col(self, col: list[str], row_index: int, ascending: bool) -> None:
        """
        Purpose: Replace row with passed column with top to bottom or bottom to top orientation

        Args:
            col (list[str]): The column that is replacing the row at row_index
            row_index (int): The index of the row that we are modifying
            ascending (bool): The direction we use to read the passed column
        """
        if ascending:
            for i in range(self.side_length):
                #Replace cell at [row][i] with cell at col[i]
                self.cells[row_index][i] = col[i]
        else:
            for i in range(self.side_length):
                self.cells[row_index][i] = col[self.side_length - i - 1]


    def replace_col_with_row(self, row: list[str], col_index: int, ascending: bool) -> None:
        """
        Purpose: Replace column with passed row with left to right or right to left orientation

        Args:
            row (list[str]): The row that is replacing the column at col_index
            col_index (int): The index of the column that we are modifying
            ascending (bool): The direction we use to read the passed row
        """
        if ascending:
            for i in range(self.side_length):
                #Replace cell at [i][col] with cell at row[i]
                self.cells[i][col_index] = row[i]
        else:
            for i in range(self.side_length):
                #Replace cell at [i][col] with cell at row[i]
                self.cells[i][col_index] = row[self.side_length - i - 1]

    
    def replace_col_with_col(self, col: list[str], col_index: int, ascending: bool) -> None:
        """
        Purpose: Replace column with passed column with top to bottom or bottom to top orientation
        
        Args:
            col (list[str]): The column that is replacing the column at col_index
            col_index (int): The index of the column that we are modifying
            ascending (bool): The direction we use to read the passed column

        """
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