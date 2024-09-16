#Cyclic Iterator: Create an iterator that cycles through a given collection indefinitely. For example, given a list [1, 2, 3], the iterator should continuously return 1, 2, 3, 1, 2, 3, ....

class CyclicIterator():
    #lets set this so infinite vlaues are not printed
    _MAX_ITERS =100
    def __init__ (self,collection):
        self.collection = collection
        self.actual_iters = 0
        self.index = 0
        
    def __iter__ (self):
        return self
        
    def __next__ (self):
        if self.actual_iters >= CyclicIterator._MAX_ITERS:
            raise StopIteration ("Iteration finished")
        
        value = self.collection[self.index]
        #the index is being reset when the rest is 0, in the final element of the list
        self.index = (self.index + 1) % len(self.collection)  
        self.actual_iters += 1  
        
        return value
            

                
if __name__ == '__main__':
    collection = [1,2,3]

    cyclicIter= CyclicIterator(collection)
    for i in cyclicIter:
        print(i)