'''# Answers: 1. if __name__ == "__main__":, 2. print("This script is being run directly.")

# Program 7: Using __name__ == "__main__"

def main_block():

    """_summary_"""

    def my_function():

        print("Function called.")

    # Placeholder 1: Create a block that only runs when the script is executed directly

    # Expected: if __name__ == "__main__":

    pass

        # Placeholder 2: Print a message to confirm direct execution

        # Expected: print("This script is being run directly.")

        pass

        my_function()'''
def main_block():
    def my_function():
        print("Function called.")
    if __name__ == "__main__":
        print("This script is being run directly")
        my_function()    

main_block()        
         
