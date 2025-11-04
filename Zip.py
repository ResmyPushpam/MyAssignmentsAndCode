try:
    names=["Resmy","Joji"]
    scores=[100,100]
    for name,score in zip(names,scores):
       print(f"{name}:{score}")        
except Exception as e:
 print("Error",e)
