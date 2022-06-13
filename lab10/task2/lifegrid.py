"""lab10 task2"""

from arrays import Array2D


class LifeGrid:
    """
    Implements the LifeGrid ADT for use with the Game of Life.
    """
    # Defines constants to represent the cell states.
    DEAD_CELL = 0
    LIVE_CELL = 1

    def __init__(self, num_rows, num_cols):
        """
        Creates the game grid and initializes the cells to dead.
        :param num_rows: the number of rows.
        :param num_cols: the number of columns.
        """
        # Allocates the 2D array for the grid.
        self._grid = Array2D(num_rows, num_cols)
        # Clears the grid and set all cells to dead.
        self.configure([])

    def num_rows(self):
        """
        Returns the number of rows in the grid.
        :return: the number rows in the grid.
        """
        return self._grid.num_rows()

    def num_cols(self):
        """
        Returns the number of columns in the grid.
        :return:Returns the number of columns in the grid.
        """
        return self._grid.num_cols()

    def configure(self, coord_list):
        """
        Configures the grid to contain the given live cells.

        :param coord_list:
        :return:
        """
        for row in range(self.num_rows()):
            for col in range(self.num_cols()):
                if (row, col) in coord_list:
                    self.set_cell(row, col)
                else:
                    self.clear_cell(row, col)

    def is_live_cell(self, row, col):
        """
        Does the indicated cell contain a live organism?

        :param row: row of the cell.
        :param col: column of the cell.
        :return: the result of check.
        """
        if self._grid[row, col] == self.LIVE_CELL:
            return True
        return False

    def clear_cell(self, row, col):
        """
        Clears the indicated cell by setting it to dead.
        :param row: row of the cell.
        :param col: column of the cell.
        """
        self._grid[row, col] = self.DEAD_CELL

    def set_cell(self, row, col):
        """
        Sets the indicated cell to be alive.
        :param row: row of the cell.
        :param col: column of the cell.
        """
        self._grid[row, col] = self.LIVE_CELL

    def num_live_neighbors(self, m_row, m_col):
        """
        Returns the number of live neighbors for the given cell.
        :param row: row of the cell.
        :param col: column of the cell.
        :return:
        """

        search_min = -1
        search_max = 2
        neighbour_num = 0
        for row in range(search_min,search_max):
            for column in range(search_min,search_max):
                neighbour_row = m_row + row
                neighbour_column = m_col + column 
                valid_neighbour = True
                if (neighbour_row) == m_row and (neighbour_column) == m_col:
                    valid_neighbour = False

                elif (neighbour_row) < 0 or (neighbour_row) >= self.num_rows():
                    valid_neighbour = False

                elif (neighbour_column) < 0 or (neighbour_column) >= self.num_cols():
                    valid_neighbour = False

                elif self.is_live_cell(neighbour_row, neighbour_column) is False:
                    valid_neighbour = False

                if valid_neighbour:
                    neighbour_num += 1
        return neighbour_num

    def __str__(self):
        """
        Returns string representation of LifeGrid
        in form of:
        DDLDD
        DLDLD
        DLDLD
        DDLDD
        DDDDD
        Where D - dead cell, L - live cell
        """
        string = ""
        for i in range(self.num_rows()):
            for j in range(self.num_cols()):
                if self.is_live_cell(i, j):
                    string += "L"
                else:
                    string += "D"
            string += "\n"
        string = string[:-1]
        return string
