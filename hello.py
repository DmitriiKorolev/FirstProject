print ("hello world")

name="Dima"
age=32
print("my name is "+name, "I am "+str(age) + " old")

Number=input("write number: ")
print(Number)
Number=int(Number)
if Number >0:
    print("the nuber is positive")
elif Number<0:
    print("the number is negative")
else:
    print("0")

for number in range(1,4):
    print(number)
word="Python"
for letter in word:
    print(letter)
count = 1
while count <=3:
    print(count)
    count +=1    

()
while True:
    password=input("Enter password:")
    if password =="secret":
        print("acsess allowed!")
        break
else:
    print("password is wrong")
for number in range(2,11,2):
    print (number)

number = 2
while number <=10:
    print (number)
    number +=2