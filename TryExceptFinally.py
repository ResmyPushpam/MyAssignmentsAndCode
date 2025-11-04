try:
    f = open("sample.txt","r")
    content = f.read()
    print(content)
except FileNotFoundError:
    print("File Not Found.")
finally:
    print("Task completed")

   
    