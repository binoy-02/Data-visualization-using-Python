def myfunc():
    print("Hello")

# myfunc()

def area(a):
    area=a*a
    print("Area of Square: "+str(area))
    
#area(10) 

def myfunc2(*name):
    print("Name is "+name[2])

#myfunc2("Amal","Shubam","Lenin")

def myfunc3(name1,name2,name3):
    print(name1)

#myfunc3(name1="Amal",name2="Shubam",name3="Lenin")

def myfunc3(**name):
    print(name["fname"])

myfunc3(fname="Jahnvi",lname="Kapoor")    