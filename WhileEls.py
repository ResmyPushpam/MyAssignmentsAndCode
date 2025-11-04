import time
try:
    Count = int(input("Enter a timer value in seconds: "))
    while Count > 0:
        print("Timer:", Count, "seconds remaining")
        print(Count)
        Count -= 1
        time.sleep(1)
    else:   
        print("Timer finished!")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
except Exception as e:
    print("An error occurred:", e)

