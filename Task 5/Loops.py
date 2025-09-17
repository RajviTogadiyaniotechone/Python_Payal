# for loops is used for the sequence iteration.
# while loop executed a block of code untill the specic condition is satisfied.
# nested loop is one loop is inside another loop.


l1 = ["one", "two", "three"]
for i in l1:
    print(i);

print("\n");

for i in range(0, len(l1)):
    print(i)

print("\n");

#while loop

j = 1;
while j <= 5:
    print(j);
    j += 1;
    if j == 3:
        break;
    print(j);

print("\n");

#For loop Iteration

print("List Iteration:");
li = ["A", "B", "C"];
for i in li:
    print(i);

for index in range(len(li)):
    print(list[index])
else:
    print("inside else block");

print("\n");

print("tuple Iteration:");
t = ("A", "B", "C");
for i in t:
    print(i)

print("\n");

print("string Iteration:");
s = "string";
for i in s:
    print(i)

print("\n");

print("Dictionary Iteration:");
di = {"one" : 123, "two" : 456}
for i in di:
    print(i)

print("\n");

print(di.keys());
print(di.values());

print("\n");

print("set Iteration:");
se = {"A", "B", "C"};
for i in se:
    print(i);                                       

