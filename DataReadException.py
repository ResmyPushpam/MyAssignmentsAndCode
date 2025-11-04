try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("Error:", e)
else:
    print(content)
    file.close()
finally:
    print("Execution completed.")