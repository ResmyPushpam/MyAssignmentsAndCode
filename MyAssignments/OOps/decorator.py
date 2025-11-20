#reusability,
# list is funtion , takes some i/p and gives an o/p
# print is function
# we are paasing ip to another function

# decorator ==> take a func ,return a new function that calls the original

def my_decorator(func):
    def wrapper(*args,*kwargs):
        print('this is before function call')
        result = func(*args,**kwargs)
        print('successfuly report generated')
        return result
    return wrapper

@my_decorator
def my_add(a,b):
    a+b
