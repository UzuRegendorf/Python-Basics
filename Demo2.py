values = [1, 2, "Uzu", 4, 5]
# List is data type that allows multiple values and can be different data types

print(values[0]) #1

print(values[3]) #4

print(values[-1]) #5

print(values[1:3]) #2 Uzu

values.insert(3,"Regendorf")
print(values)
values.append("End")
print(values)

values[2] = "UZU" #updating

del values[0]

print(values)

#Tuple, same as data type but immutable
val = (1, 2, "Uzu", 4.5)

print(val[1])

#val[2] = "Regendorf"

print(val)

# Dictionary

dic = {"a":2, 4:"bcd", "c":"Hello World"}

print(dic[4])
print(dic["c"])

#
dict = {}

dict["firstname"] = "Uzu"
dict["lastname"] = "Regendorf"
dict["gender"] = "Male"
print(dict)
print(dict["lastname"])
