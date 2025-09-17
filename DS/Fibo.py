# Memoization is a technique that can help you optimize your 
# algorithms by storing and reusing the results of previous computations.

def fib(n):
    if(n<=1):
        return n 
    
    return fib(n - 1) + fib(n - 2)

if __name__ == '__main__':
    n = 9
    print(fib(n))