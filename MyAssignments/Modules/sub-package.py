'''# Answers: 1. from my_package.sub_module import func_in_sub, 2. func_in_sub()

# Program 6: Importing from a sub-package

# Assume the package structure: my_package/__init__.py, my_package/sub_module.py (with `def func_in_sub(): print("Success!")`)

def package_import():

    """_summary_"""

    # Placeholder 1: Import `func_in_sub` from the sub_module inside my_package

    # Expected: from my_package.sub_module import func_in_sub

    pass

    # Placeholder 2: Call the imported function

    # Expected: func_in_sub()

    pass'''

def package_import():
    from my_package.sub_module import func_in_sub
    func_in_sub()
    
package_import() 