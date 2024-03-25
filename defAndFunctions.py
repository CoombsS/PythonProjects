swapL = [10,20]
def swap(x,y):
    i = swapL.index(x)
    swapL.pop()
    swapL.insert(i,y)
    print(swapL)
swap(10,20)

numL = [11,24,21,64,23,7,23,66,9,13]
def bigAndSmall (array):
    numL.sort()
    b = len(numL)
    b = b-1
    alpha = (numL[0])
    beta = (numL[b])
    return alpha, beta
print(bigAndSmall(numL))



