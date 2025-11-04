try:
    for i in range(10):
        if i== 5:
            print ("Stopping at 5")
            break
        print(i)
except Exception as e:
    print("Error:",e)        