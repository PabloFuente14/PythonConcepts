#Iterators area a lazy way to process collections. Instead of storing the whole list at memory, it only works with the current elemnt.
#They are good when generating infinite loops

numbers = range(10**100)
num_iter = iter(numbers) #not working wich a hughe collection this way

for i in num_iter: ##internally calls the next elemnnt of the iterator,
    if i == 20:
        break
    
# Prime Numbers Iterator: Create an iterator that returns consecutive prime numbers starting from 2. 
# The iterator should generate an infinite sequence of primes without storing all previous numbers in memory.
class PrimeIterator():
    def __init__ (self):
        self.current = 0
#define this object as iterator
    def __iter__(self):
        return self
    
    def __next__(self):
        #adding +1 after a true is.prime()
        self.current += 1
        
        while not self.is_prime(self.current):
            self.current += 1
        return self.current    
    
    def is_prime(self,n):
        if n < 2:
            return False
        for i in range(2,int(n**0.5) +1):
            if n%i == 0:
                return False
        return True
    

if __name__ == '__main__':
    primes = PrimeIterator()
    
    #loop calls next infinite, till the break is being Ture
    for number in primes:
        print(number)
        if number > 100:
            break