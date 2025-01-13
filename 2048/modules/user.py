import re

class User:
    def __init__(self) -> None:
        self.name = "Hello 2048"

    def filter_input(self, key, action):
        '''
        Function to filter user input.
        '''

        if len(key) > 1:
            print("Input can only be of single Digit. Please try again.")
            print()
            return False
        
        pattern: str = r'[2-9]'
        if action == "init":
            # key must be a number
            if not re.match(pattern, key):
                print("Grid size can only be a number between 2 and 9. Please try again.")
                print()
                return False
            
            self.grid_size = int(key)
            return True
        
        elif action == "play":
            # key must be wasd
            pattern: str = r'[wasd]'
            if not re.match(pattern, key):
                print("Play key can only be wasd. Please try again.")
                print()
                return False
            self.key_pressed = key
            return True
    
    # We will fine tune keyboard input later
    def get_user_input(self, action) -> bool:
        '''
        Function to get user input.
        '''
        filter_output: bool = False
        while filter_output is not True:
            if action == "init":
                key = input("Please enter grid size: ")
                print()
            elif action == "play":
                key = input("Please press play key: ")
                print()
            filter_output = self.filter_input(key, action)
        