# tuple is similar to list but it is unchangeble or immutable that it can not change once it is created.
# tuples cannot be removed or appendable, tuple is ordered.
# list can be changed or modified.
# TUple use less memory than list and are faster to access than list. list is mutable while tuple is not. 
# both are in ordered sequence

t1 = (1, 3, 5,)
print(type(t1))
print(t1)
print("Negative INdexing>>",t1[-1])
print(t1[0])

#Traversal
for i in t1:
    print("Traversal>>",i)

#Concatenation
t2 = "Hello","Tuple"
print("Concatenation",t1 + t2)

#Nesting tuples
t3 = (t1,t2)
print("Nesting tuple>> ",t3)

#repetation in tuple
t4 = ("PYTHON",)*3
print(t4)

t = ("one","two","three")
print(t[0:2])
print(t[:])
print(t[:1])

#tup = (0,0)
#del tup
#print("Deleted tuple>>")
#print(tup)

print("\n")

# python code for creating tuples in a loop
t = ('abc',)

# Number of time loop runs
n = 5 
for i in range(int(n)):
    t = (t,)
    print(t)

#MEthods

tu = 1, 2, 3, 7, 8, 43, 3, 6, 7, 3, 5, 4 

print(tu)
o = tu.count(7)
print("count of the value is >>",o)


i = tu.index(5)
print("index of the number is>>",i)

m = max(tu)
print("Maximum of the tuple is>>",m)

n = min(tu)
print("Minimum of the tuple is>>",n)

l = len(tu)
print("Lenght of the tuple is>>",l)
#tuple Packing

x, y, z = 7, 8, 9
print(x,y,z) 

#tuple unpacking

tp = (7, 1 , 3, 1)
front, *_, rear = tp
print(front,rear)

# converting list into tuple

mylist = ["India", "USA", "Canada", "Singapore"]

print("List",type(mylist))

tuple(mylist)

print(mylist)

# removes empty tuples

t = [(1, 2), (), (3, 4), (), (5,)]
res = [a for a in t if a]
print(res)

# Reversing a tuple using slicing technique
print(t[::-1])

#by function
def rev(t):
    tup = t[::-1]
    return tup
print(rev(t))

