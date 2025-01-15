import random

class Grid:
    def __init__(self, grid_size: int) -> None:
        '''
        Grid class which stores the actual Grid Object.
        '''
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
                    print(' ' + str(self.object[i][j]) + ' ', end=' ')
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
    

    def check_grid_boundary(self, row_value: int, col_value: int) -> bool:
        '''
        Function to check the if given index is inside the grid boundary.
        '''
        if (row_value >= 0 
            and row_value < self.size 
            and col_value >= 0 
            and col_value < self.size):
            return True
        return False


    def check_grid_index(self, row_value: int, col_value: int) -> bool:
        '''
        Function to check if given index on the grid is playable.
        '''
        print("Checking index: " + str(row_value) + " - " + str(col_value))
        if self.check_grid_boundary(row_value, col_value):
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
        '''
        Function to check if game is over.
        '''
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


    def update_stack(self, stack: list) -> list:
        '''
        Function to update the stack stored.
        '''
        # Process the column
        for index in range(len(stack)):
            if index + 1 < len(stack):
                if stack[index] == stack[index+1]:
                    stack[index] += stack[index + 1]
                    stack.pop(index+1)
            else:
                continue
        return stack


    def align_right(self):
        '''
        Function to align all the elements to the right.
        '''
        # Go through each row
        for i in range(self.size):
            stack: list = []

            # Store the row
            for j in range(self.size-1, -1, -1):
                if self.object[i][j] != 0:
                    stack.append(self.object[i][j])
                    # Update the object
                    self.object[i][j] = 0
                else:
                    continue
        
            # Process the row
            stack = self.update_stack(stack)

            # Update the row
            stack_index: int = 0
            for j in range(self.size-1, -1, -1):
                if stack_index < len(stack):
                    self.object[i][j] = stack[stack_index]
                    stack_index += 1
                else:
                    self.empty_list.append([i,j])
        return


    def align_down(self):
        '''
        Function to align all elements downwards.
        '''
        # Go through each column
        for i in range(self.size):
            stack: list = []
            # Store the column
            for j in range(self.size-1, -1, -1):
                if self.object[j][i] != 0:
                    stack.append(self.object[j][i])
                    # Update this object
                    self.object[j][i] = 0
                else:
                    continue
            
            # Process the column
            stack = self.update_stack(stack)
            
            # Store the updated column, and also store the empty indexes
            stack_index: int = 0
            for j in range(self.size-1, -1, -1):
                if stack_index < len(stack):
                    self.object[j][i] = stack[stack_index]
                    stack_index += 1
                else:
                    self.empty_list.append([j,i])
        return


    def align_left(self):
        '''
        Function to align all elements to the left.
        '''
        # Go through each row
        for i in range(self.size):
            stack: list = []

            # Store the row
            for j in range(self.size):
                if self.object[i][j] != 0:
                    stack.append(self.object[i][j])
                    self.object[i][j] = 0
                else:
                    continue
            
            # Process the row
            stack = self.update_stack(stack)

            for j in range(self.size):
                if j < len(stack):
                    self.object[i][j] = stack[j]
                else:
                    self.empty_list.append([i,j])
        return


    def align_up(self):
        '''
        Function to align all elements upwards.
        '''
        # Go through each column
        for i in range(self.size):
            stack: list = []
            # Store the column
            for j in range(self.size):
                if self.object[j][i] != 0:
                        stack.append(self.object[j][i])
                        # Update this object
                        self.object[j][i] = 0
                else:
                    continue
            
            # Process the column
            stack = self.update_stack(stack)
            
            # Store the updated column, and also store the empty indexes
            for j in range(self.size):
                if j < len(stack):
                    self.object[j][i] = stack[j]
                else:
                    self.empty_list.append([j,i])


    def update(self, key: str) -> None:
        '''
        Function to update the Grid after playable key is pressed.
        '''
        # Update empty indexes
        self.empty_list = []
        if key == 'w':
            self.align_up()
        elif key == 's':
            self.align_down()
        elif key == 'a':
            self.align_left()
        elif key == 'd':
            self.align_right()

