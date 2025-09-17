# Dictionary are the data structure which is uppered in the key value pair
# Dictionary are the ordered and changeble, allow duplicates.

cars = {
        "brand": "Toyota", 
        "model_year": 2020, 
        "price": 20000,
        "color": "Blue"
    }

print(type(cars))

print(cars)

# access by keys
print(cars["brand"])

#Length
print(len(cars))

v = cars.values()
print("values>>",v)

k = cars.keys()
print("keys>>",k)

#change value in the dictionary
cars["price"] = 200000
print(cars)

i = cars.items()
print(i)

#check if the value is present or not
if "color" in cars:
    print("Yes Exists")

#update() method to update the dictionary
cars.update({"model_year": 2025})
print(cars)

#add new key in the dictionary
cars["since"] = 1980
print(cars)

#pop() method
cars.pop("since")
print("popped the since variable>>",cars)

#del keyword for the delete the specified key
# cars.clear() method for the empties the dict

print("\n")

# for get the values
print("Values in the dictionary>>")
for x in cars.keys():
    print(x)

print("\n")

# for get the keys
print("keys in the dictionary>>")
for x in cars:
    print(cars[x])

# loop through both key and variable
for x, y in cars.items():
    print(x, y)

#copy dictionary
dic2 = cars.copy()
print("copied dictionary>>")
print(dic2)