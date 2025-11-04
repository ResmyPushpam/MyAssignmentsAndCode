try:
    for i in range(1,100):
        if i%2==0:
            continue
        print(i)
except Exception as e:
    print("Error:",e)

 