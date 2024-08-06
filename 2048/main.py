from modules.grid import Grid
from modules.user import UserInput

def main():
    user_input = UserInput()
    user_input.get_user_input()
    # grid_size: int = 4
    # grid = Grid(grid_size=grid_size)
    # grid.display_grid()
    # for i in range(10):
    #     print(i, end='\r')
    # print()

if __name__ == "__main__":
    main()