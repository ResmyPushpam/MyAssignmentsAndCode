#Iterator
# range

class Newrange:
    def __int__(self,start,finish,step=1):
        self.start = start
        self.stop  =  finish
        self.step  =  step
        self.current = start
    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.stop:
            raise StopIteration
        value =  self.current
        self.current += self.step
        return value
 
    
for i in Newrange(1,10):
    print(i)


