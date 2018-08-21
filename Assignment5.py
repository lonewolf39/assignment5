#Q.1- Verify leap year

year=int(input("Enter a year to check if its leap year"))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("leap")
        else:
            print("not leap year")
    else:
        print("leap year")
else:
    print("not leap year")


#Q.2- Check Whether the given dimensions are of square or rectangle

length=int(input("Enter length"))
breadth=int(input("Enter breadth"))
if(length==breadth):
    print("IT'S A SQUARE")
else:
    print("IT'S A RECTANGLE")



#Q.3- Determine oldest and the youngest age

x=int(input("Enter age of first person"))
y=int(input("Enter age of second person"))
z=int(input("Enter age of third person"))
if(x>=y and x>=z):
    print("First person is the oldest")
elif(y>=x and y>=z):
    print("Second person is the oldest")
else:
    print("Third person is the oldest")

if(x<=y and x<=z):
    print("First person is the youngest")
elif(y<=x and y<=z):
    print("Second person is the youngest")
else:
    print("Third person is the youngest")


#Q.4- analyse the given data

age=int(input("Enter age"))
sex=input("Enter sex")
m=input("Enter marital status")
if(sex=='F'):
    print("Work in Urban Areas")
else:
    if(age>=20 and age<=40):
        print("Can work anywhere")
    elif(age>=40 and age<=60):
        print("Work in urban areas")
    else:
        print("Error")


#Q.5- Cost problem

a=int(input("Enter quantity"))
c=100*a
if(c>1000):
    c=c-(c*0.1)
    print("Total cost is =",c)
else:
    print("Total cost is =",c)



#Q.6- print user defined integers
lst=[]
for i in range(10):
    a=int(input("Enter a number"))
    lst.append(a)
print(lst)

#Q.7- Write an infinite loop

while True:
    print("*")

    
#Q.8- Make a list which will store square of elements of other list
    
x=[]
y=[]
num=int(input("enter number of elements"))
for i in range(num):
    z=int(input("enter number"))
    x.append(z)
for j in z:
    r=j*j
    y.append(r)
print(y)

#Q.9- Group the all data types in a list

l1=[]
l2=[]
l3=[]
l4=[]
a=int(input("Enter total number of inputs"))
for i in range(a):
    b=input("Enter elements of list")
    l1.append(b)
for i in l1:
    if(i.isdigit()):
        l2.append(i)
    elif(i.isalpha()):
        l3.append(i)
    else:
        l4.append(i)
print(l2)
print(l3)
print(l4)

#Q.10- Make a list containing prime numbers

r=[]
for i in range(1,101):
    if(i>1):
        flag=False
        for j in range(2,i):
            if(i%j==0):
                flag=True
        if not flag:
            r.append(i)
print(p)

#Q.11- Pattern

for i in range(5):
    for j in range(i):
        print("*",end='')
    print()


#Q.12- Search and delete an element from a user defined list


w=[]
n=int(input("elements of list"))
for i in range(n):
    a=int(input("element"))
    w.append(a)
num=int(input("number you want to delete"))
x=w.count(num)
for i in range(x):
    y=w.index(num)
    del(w[y])
print(w)







