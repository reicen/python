#while loop = statement that will execute its block of code
#           AS LONG AS ITS CONDITION REMAINS TRUE

#while 1==1:
#    print('help! im stuck in a loop huhu')

name = None
while not name:
    name = input('Enter your name: ')
print('henlo '+name)

age = ""
while len(age) == 0:
    age = input('What is your age? ')
    if age == "1":
        print('you are '+age+' year old!')
    else:
        print('you are '+age+' years old')
age = int(age)
addtlage = age+1
print("you'll be "+str(addtlage)+" soon!")