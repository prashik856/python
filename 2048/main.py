from modules.grid import Grid
from modules.user import User

def main():
    # Initialize the grid
    user = User()
    user.get_user_input("init")

    print("Grid size to be used: " + str(user.grid_size))

    grid = Grid(user.grid_size)
    # Display initialzed grid without random value
    grid.display()

    # Randomize the grid, put our first playable 2
    grid.random_update()
    grid.display()

    # Now we play our game
    while not grid.check_game_over():
        # Get the key pressed
        key : str = user.get_user_input("play")
        print("Key pressed: " + key)
        grid.update(key)
        grid.random_update()
        grid.display()

    
    print("Game Over.")
    grid.display()


if __name__ == "__main__":
    main()