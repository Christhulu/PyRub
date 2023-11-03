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
            print()

    def face_to_string(self) -> str:
        face_str:str = ''
        for i in self.cells:
            face_str += '\t'.join(map(str, i))
            face_str += '\n'

        face_str += '\n'

        return face_str

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