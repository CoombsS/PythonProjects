#myTuple = (50,30,40)

#x = list(myTuple)

#x.append()
#x.remove()

#myTuple = tuple(x)
#print(myTuple)


tuple = (1,2,3,4,5,6,7,8,9,10)
x = list(tuple)
x.append(11)
x.append(12)
print(x)
z = list(x)
z.remove(1)
z.remove(2)
print(z)
tuple1 = tuple(x)
print(tuple1)