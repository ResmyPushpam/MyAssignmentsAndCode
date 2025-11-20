'''# Program 9: Dynamically adding to sys.path

# Note: This is a scenario for understanding, not a best practice.

def dynamic_path_add():

    """_summary_"""

    # Placeholder 1: Import the `sys` module

    # Expected: import sys

    pass

    # Placeholder 2: Add a new path to the system path list

    # Expected: sys.path.append('/path/to/my_modules')

    pass

    # Placeholder 3: Now you can import a module from that new path

    # Expected: import new_module

    pass

 '''

def dynamic_path_add():
    import sys
    sys.path.append('C:\\Rachu\\Skills Boot Camp\\Python-29.10.2025\\my-python-project\\MyAssignments\\Modules')
    import my_module
    my_module.greet("Master")


dynamic_path_add()

