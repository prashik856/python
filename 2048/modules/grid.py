import random

class Grid:
    def __init__(self, grid_size: int) -> None:
        # the grid size
        self.size: int = grid_size
        # List that stores indexes of empty positions
        self.empty_list: list = []

        # The actual grid object
        self.object: list = []

        # Initializing grid
        for i in range(grid_size):
            self.object.append([])
            for j in range(grid_size):
                self.object[i].append(0)
                self.empty_list.append([i, j])


    def display(self) -> None:
        '''
        Function which will display the current grid
        '''
        print()

        for i in range(self.size):
            for j in range(self.size):
                if self.object[i][j] == 0:
                    print(' . ', end=' ')
                else:
                    print(self.object[i][j], end=' ')
            print("\n")
        print()
    
        # More details for development
        print("Empty Positions: ")
        print(self.empty_list)
        print()


    def get_random_item_location(self) -> int:
        '''
        Function to get a random index in the grid which is empty
        '''
        random_index: int = -1
        random_index = random.randrange(0, len(self.empty_list))
        return random_index


    def check_grid_index(self, row_value, col_value) -> bool:
        print("Checking index: " + str(row_value) + " - " + str(col_value))
        if (row_value >= 0 
            and row_value < self.size 
            and col_value >= 0 
            and col_value < self.size):
            if self.object[row_value][col_value] == 2:
                # Continue Play
                print("2 present. Player can play on this index.")
                return True
            else:
                print("2 not present anywhere. Player cannot play on this index.")
                return False
        else:
            # Bad index
            print("Bad Index.")
            return False


    def check_game_over(self) -> bool:
        print("Random row/col values used: " + str(self.row) + " - " + str(self.col))
        is_game_over: bool = False
        if len(self.empty_list) != 0:
            print("Empty list is not empty. Continue Playing.")
            return is_game_over
        else:
            # Random index will not be equal to -1 here
            is_game_over = not (self.check_grid_index(self.row - 1, self.col)
                or self.check_grid_index(self.row + 1, self.col)
                or self.check_grid_index(self.row, self.col - 1)
                or self.check_grid_index(self.row, self.col + 1))
            print("Is Game Over value: " + str(is_game_over))
            if is_game_over:
                print("No other position to play now. Stop playing.")
            else:
                print("Player can play more positions. Continue Playing.")
        return is_game_over


    def random_update(self) -> bool: 
        '''
        Function to update the grid by placing a random 2 at an empty location.
        '''
        random_index: int = self.get_random_item_location()
        print("Random Index Obtained: " + str(random_index))
        print("Value of Random Index: " + str(self.empty_list[random_index]))
        self.row: int = self.empty_list[random_index][0]
        self.col: int = self.empty_list[random_index][1]
        self.object[self.row][self.col] = 2

        # Update the empty_list as current random index is now not empty
        # Remove the random_index Value
        self.empty_list.remove(self.empty_list[random_index])
