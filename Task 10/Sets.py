# set is one of the built in data type that used to store the values.
# set is unoredered, unchanable, does not allow duplicates if duplicates are inserted then that is ignored and
# unindexed. that is identified with the {}
# sets can be in indexed any time or can be any type. 

myset = {100, 20, 7, 79}
print(type(myset))
print(myset)
print("Length of the set>>",len(myset))

# create set using set constructure

s = set(("one", "two", ""))
print(s)
print(type(s))

#access set by loop

for i in s:
    print(i)

#check the value 

#add() method
myset.add(99)
print(myset)

myset2 = {"true","false"}
myset.update(myset2)
print("upgraded by update method>>",myset)

#remove() method, discard() method is as same as remove
s.remove("")
print(s)

#pop() method to remove the first element 
p = s.pop()
print("popped element>>",p)
print(s)

# clear() method to empties the set
s.clear()
print(s)

#del keyword to delete the set
#del s

# join set by union method
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = set1.union(set2)
print("Union set>>",set3)

set3 = set1 | set2
print("union by '|' operator>>",set3)

set1.update(set2)
print("update set>> ",set1)

set4 = {"google", "microsoft", "apple"}
set5 = {"google", "samsung"}
set6 = set4.intersection(set5)
print("intersection set>>",set6)

#this method will return the same output without creating new set
set4.intersection_update(set5)
print(set4)

# difference method will give the output which is not common in the two set
set7 = set4.difference(set5)
print(set7)

# likewise intersection_update you don't need to create the extra variable
set4.difference_update(set5)
print("difference method>>",set4)

# disjoint method will return true if none of the elemnts is present in the set
d = set1.isdisjoint(set2)
print(d)

# if set2 is subset of set1
s = set2.issubset(set1)
print(s)

