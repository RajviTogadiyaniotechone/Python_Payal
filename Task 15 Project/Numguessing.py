import random;

n = random.randrange(1,10)
Guess = int(input("Enter any Number:"));

while n != Guess:
    if Guess <= n:
        print("Too Low")
        Guess = int(input("Enter Number again :"));
    elif Guess >= n:
        print("Too High")
        Guess = int(input("Enter Number again :"))
    else:
        break

print("You Guessed Right ;)")
