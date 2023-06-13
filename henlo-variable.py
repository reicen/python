#STRING
name = "Leslie"
print(name)
print("henlo "+name)
print(type(print))
print(type(name))

first_name = "Leslie"
last_name = "Fu"
full_name = first_name + " " + last_name

print(first_name)
print(last_name)
print(full_name)

print("henlo "+ full_name)

# INTEGER datatype

age = 22
print(age)
#age = age + 1
print(age)
#shorthand for the equation
age += 1
print(age)
age -=2
print(age)
age *= 3
print(age)
print(type(age))

#print("my age is "+ age)
#^^^ BAWAL SYA coz kala nya math ahahaha
print("my age is "+ str(age))


#FLOAT = decimal numbers
weight = 69.9
print(weight)
print(type(weight))
print("i weigh "+str(weight)+"kg")

#BOOLEAN
human = True
gay = False
print(gay)
print(human)
print(type(human))
print("are u human? " + str(human))
print('bakla ka ba ha? ' +str(gay))
if human is True:
    print("yas kween")
if gay is False:
    print("naur")