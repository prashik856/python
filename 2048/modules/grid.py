import random

class Grid:
    def __init__(self, grid_size: int) -> None:
        # the grid size
        self.size: int = grid_size
        self.empty_count: int = grid_size * grid_size

        # The actual grid object
        self.object: list = []

        # Initializing grid
        for i in range(grid_size):
            self.object.append([])
            for j in range(grid_size):
                index: int = i * grid_size + j
                self.object[i].append(0)


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
        print("Empty Count: " + str(self.empty_count))
        print()


    


    def random_update(self) -> bool: 
        '''
        Function to update the grid by placing a random 2 at an empty location.
        '''


    def get_random_item_location(self) -> int:
        '''
        Function to get a random index in the grid which is empty
        '''
        found_index: bool = False
        random_index: int = -1
        while not found_index:
            random_index = random.randrange(0, len(self.grid_empty_list))
            if(self.grid_empty_list[random_index]):
                found_index = True
                break
        return random_index

