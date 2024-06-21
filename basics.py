'''a=float(5)
b=4.44
c= a+b
text="Hello"
fname="Binoy"
lname="Jolly"
string ="My name is Binoy Jolly"
# age=22
print(type(a))
print(type(b))
print(type(c))

print("I am " + fname +" "+ lname)

for i in fname:
    print(i)

s1=slice(-1,5,2)'''



#LIST

'''list1=[1,2,3,4]
list2=["binoy","Jolly"]
newlist=list((45,32,23,11))
abc=list2.copy()
print(list1)
print(list2)
print(newlist)
print(list2[1])
list1[2]=7
list2.append(list1)
print(list2)
print(list1)
newlist=list2
print(newlist)
print(abc)
del abc
print(abc)'''


#TUPLE

'''tuple1 = (11,33,22,55,77,'Binoy','Jolly',[1,2,3])
tuple2=tuple((21,22,23,24))
print(tuple1)
print(tuple2)
a=tuple2.count(21)
print(a)'''

#SET

d1={
    "name" : "Binoy",
    "age" : 22,
    "course" : "Python",
}

# print(d1)

d2={
   "name" : {"Binoy","Athulya","Anjali","Gopika"},
   "age" :(21,22,22,21),
}

d3={
    "Python":{
        "stu1" :20,
        "stu2" :24,
        "stu3" : 45
    },

    "DIP":{
        "stu1" :24,
        "stu2" :35,
        "stu3" : 30,
    }
}

print(d3["Python"]["stu1"])