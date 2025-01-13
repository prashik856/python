from modules.grid import Grid
from modules.user import User

def main():
    # Initialize the grid
    user = User()
    user.get_user_input("init")

    print("Grid size to be used: " + str(user.grid_size))

    grid = Grid(user.grid_size)
    grid.display()

if __name__ == "__main__":
    main()