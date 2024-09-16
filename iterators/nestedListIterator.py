#Nested List Iterator: Design an iterator that can traverse a list with an arbitrary nested structure. 
#For example, given a list like [[1, 2], [3, [4, 5]], 6], the iterator should return the elements in the order 1, 2, 3, 4, 5, 6.


class NestedListIterator:
    def __init__(self, nested_list):
        self.flat_list = list(self.flatten(nested_list))
    
    def __iter__(self):
        return iter(self.flat_list)

#the diff with fibonacci is that in fibonacci the state of progression is being personalizced to the nest prime number.
#In this case, by using the yield, the __next__ is being handled automatically, it manages the iteration by itself.
#Yield allows to pause and keep doing things. Return gives back whatever, and ends the functione. So in this case, yield is giving back the list gotten and using as parameter of the function to create recursive behaviour.
    def flatten(self, nested_list):
        for element in nested_list:
            if isinstance(element, list):
                yield from self.flatten(element)  
            else:
                yield element  

if __name__ == '__main__':
    nested_list = [[1, 2], [3, [4, 5]], 6, [1,2,3,4,["pñknl,","mkd", [1,2]]]]
    nested_iterator = NestedListIterator(nested_list)

    for j in nested_iterator:
        print(j)
