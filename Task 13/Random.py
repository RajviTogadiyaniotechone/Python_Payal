import random

# print random number
print(random.random())

# random uniform float number between 1 to 10
print("Uniform float number between given range::",random.uniform(0,10))

print("Random integer number between given range::",random.randint(7,100))

print("Random range::",random.randrange(0, 100, 1))

my_list = ["one", "seven", "nine"]
print("Random choice from the list::",random.choice(my_list))

#Shuffling and sampling

mylist = [1, 2, 3, 4, 5]
random.shuffle(mylist)
print(mylist)

# this will give the random 3 number from the list
print(random.sample(mylist, 3))

#print(random.choices(mylist, K=2))

#print(random.choices(mylist, weights=[1, 2, 3], k=3))  
