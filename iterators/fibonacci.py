#Implement an iterator that generates the Fibonacci sequence but allows the user to set the initial values of the first two numbers in the sequence.

class Fibonacci():
    def __init__ (self, n1 =1,
                  n2=1, max_sequcence = 20):
        self.n1 = n1
        self.n2 = n2
        self.actual_sequence = 1
        self.max_squence = max_sequcence
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.actual_sequence == self.max_squence:
            raise StopIteration("Secuencia finalizada")
        actual_number = self.get_next_num()
        self.n1 = self.n2 
        self.n2 = actual_number
        self.actual_sequence += 1
        return actual_number
    
    
    def get_next_num(self):
        next_num = self.n1 + self.n2
        return next_num
    
    
if __name__ == '__main__':
    fibonacci = Fibonacci(2,3,15)
    print(f"The secuence starts with {fibonacci.n1}, {fibonacci.n2}")
    for number in fibonacci:
        print(number)
