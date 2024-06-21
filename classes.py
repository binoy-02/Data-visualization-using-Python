class Person:
        x=20

obj=Person()

#print(obj.x)

class person1:
        def __init__(me,fname,lname):
                me.f=fname
                me.l=lname

obj1=person1("Binoy","Jolly")

print("My name is "+obj1.f+" "+obj1.l)