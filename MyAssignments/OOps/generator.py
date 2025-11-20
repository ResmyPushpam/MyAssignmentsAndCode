# genarator
# out put of Tuple comprehension is always generator
#yield is also generator

a = []
for i in range (1,11):
    a.append(i**2)

print(a)

b = [ i**2 for i in range(1,11)]
print(f"Comprension {b}")


imp sys
imp time

def gen_list():
    return (i**2 for i in range(1,10000))

start_time=time.time()
output = gen_list()
end_time=time.time()

print(f" time taken is {end_time}")
print(f"Memory size ,{sys.getsizeof(output)}")

a=[]

for i in range(1100000):
    c=i**2
    a.append(c)
print(f"Memory size , {sys.getsizeof(output)}")

def seq_gen()


