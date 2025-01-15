from modules.grid import Grid
from modules.user import User

def main():
    '''
    Main driver code
    '''
    # Initialize the grid
    user = User()
    user.get_user_input("init")

    print("Grid size to be used: " + str(user.grid_size))

    grid = Grid(user.grid_size)
    # Display initialzed grid without random value
    grid.display()

    # Randomize the grid, put our first playable 2
    grid.random_update()
    # save this state
    grid.save_current_state()
    grid.display()

    # Now we play our game
    while not grid.check_game_over():
        # Get the key pressed
        key : str = user.get_user_input("play")
        print("Key pressed: " + key)
        # Update our grid
        grid.update(key)
        if grid.is_equal_with_previous_state():
            print("No changes observed in current and previous state. Don't add a random 2.")
        else:
            print("Grid changed. Add a random 2.")
            grid.random_update()
            # save this new random state
            grid.save_current_state()
        grid.display()

    
    print("Game Over.")
    grid.display()


if __name__ == "__main__":
    '''
    Entrypoint.
    '''
    main()