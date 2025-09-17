# VAriables are the containers for the the data in which form data is stored
# Data types is the type of the data hold in the memory

#1. Declare variables for your age and height and print them. 
age = "123";
height = "150cm";

print("Age = ",age);
print("Height = ",height);

x = 5;
y = "Payal";
z = 10.5;
p = ["Apple" , "Banana", "Cherry"];
q = {10, 2, 3};
r = {"name" : "Payal"};
s = (5 , 8);
t = "true";
u = b"hi";
print(type(x))
print(type(y))
print(type(z))
print(type(p))
print(type(q))
print(type(r))
print(type(s))
print(type(t))
print(type(u))

#2. Convert a floating-point number to an integer and print it. 
a = int(z);
print("Type conversion>>",type(a));

#3. Create a string variable and find its length.
print("Length of the string is>>",len(y))

#LIST
#Length of the list
print("Length of the list>> ",len(p))

#Change value in the list
p[1] = "Grapes";
print(p)

#List Comprehention
mylist = [x for x in p if x == "cherry"]
print("List Comprehention>> ",mylist);

newlist = [x for x in range(10) if x > 5]
print(newlist)

list1 = [100 ,25, 35, 7, 99]
list1.sort(reverse=True);
print(list1);

p.insert(3,"Mango");
p.append("Orange");
list2 = ["apple", "banana", "cherry"]
p.extend(list2)

#TUPLE
# Unpacking a Tuple

(green , *yellow, red) = p
print("This is list 2>>",p)

print("this is the yellow variable>>   ",*yellow)

p.remove("apple")
p.pop(5)    #Remove at the specified index
print(p)

#DICTIONARIES

dicti = {
    "name" : "abc",
    "city" : "Rajkot",
    "country" : "India"
}
print(dicti)
print(dicti["city"])
print(len(dicti))
print(type(dicti))

this_dict = dict(a = 'A', b = 'B')
print(this_dict)
this_dict.get(a)

m = this_dict.keys()
n = this_dict.values()
print(m)
print(n)

# change the value
dicti["country"] = "Singapore"
print(dicti)

tuple = ("one", "two", "three");
print(type(tuple)) 
o = list(tuple) #tuple into list type conversion
print(o)

#SET
print("Lenght of the set is>>>   ",len(q))

s1 = set(("s1", "s2", "s3"))
print(s1)
s1.add("s4")
q.discard("s4")

#delete
del s1

for x in q:
    print("result of the x is >>",x)

print(10 in q)

#Join set
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
ans = set1.intersection(set2, set3)
print("ans is >>.",ans)
print(set3)
set3 = set1 | set2
print("set3 >>",set3)
z = set1.difference(set2)
print("difference>>   ",z)

#set copy
k = set1.copy()
print(k)