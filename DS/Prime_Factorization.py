# Prime Factorization by Efficient Method

def Prime_Factors(n):
    Factors = []

    while n % 2 == 0:
        Factors.append(2)
        n //= 2
            
    # Check for odd factors from 3 to the square root of n
    divisor = 3
    while divisor * divisor <= n:
        while n % divisor == 0:
            Factors.append(divisor)
            n //= divisor
        divisor += 2
    # if n is the prime number greater than 2
    if n > 2:
        Factors.append(n)

        return Factors
    
number = int(input("Enter a Number:: "))
Factors = Prime_Factors(number)
print("Factors Of the given Number is::",Factors)