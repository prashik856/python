import random

class Grid:
    def __init__(self, grid_size: int) -> None:
        # the grid size
        self.grid_size: int = grid_size
        
        # The actual grid object
        self.grid_object: list = []

        # The list which stores which indexes are empty
        self.grid_empty_list: list = []

        # the mapping which stores the map of random index to grid index
        self.grid_space_map: dict = {}

        # Initializing grid
        for i in range(grid_size):
            self.grid_object.append([])
            for j in range(grid_size):
                index: int = i * grid_size + j
                self.grid_object[i].append(0)
                self.grid_empty_list.append(False)
                self.grid_space_map[index] = [i,j]


    def display_grid(self) -> None:
        '''
        Function which will display the current grid
        '''
        for i in range(len(self.grid_object)):
            for j in range(len(self.grid_object[i])):
                if self.grid_object[i][j] == 0:
                    print('.', end=' ')
                else:
                    print(self.grid_object[i][j], end=' ')
            print()
        print()
    

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


    def update_grid(self) -> None:
        '''
        function which will update the grid and all related values
        '''
        random_index = self.get_random_item_location()
        self.grid_empty_list[random_index] = True
        index_as_list = self.grid_space_map[random_index]
        self.grid_object[index_as_list[0]][index_as_list[1]] = 2
