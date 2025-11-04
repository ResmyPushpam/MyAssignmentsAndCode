try:
    f = open("non_existent_file.txt", "r")
    content = f.read()
    print(content)
except FileNotFoundError:
    print("Error: The file was not found.")
except IOError:
    print("Error: An I/O error occurred while handling the file.")