Set1 = {'b1', 'g2', 'r3', 'b4', 'g5'}
Set2 = {'g1', 'b2', 'r3', 'b5', 'r6', 'g7'}
Set3 = {'r1', 'b9', 'g3', 'r4', 'r5', 'g6', 'b7'}
Set4 = set()
Set5 = set()
Set6 = set()
blueCount = 0
redCount = 0
greenCount = 0
#Counting all the chocolates by color
#Blue count
for item in Set1:
    if item[0].startswith('b'):
        blueCount +=1
        Set4.add(item)
for item in Set2:
    if item[0].startswith('b'):
        blueCount +=1
        Set4.add(item)
for item in Set3:
    if item[0].startswith('b'):
        blueCount +=1
        Set4.add(item)
print("Bluecount in all sets:", blueCount)
#Red count
for item in Set1:
    if item[0].startswith('r'):
        redCount +=1
        Set6.add(item)
for item in Set2:
    if item[0].startswith('r'):
        redCount +=1
        Set6.add(item)
for item in Set3:
    if item[0].startswith('r'):
        redCount +=1
        Set6.add(item)
print("Redcount in all sets:", redCount)
#Green count
for item in Set1:
    if item[0].startswith('g'):
        greenCount += 1
        Set5.add(item)
for item in Set2:
    if item[0].startswith('g'):
        greenCount += 1
        Set5.add(item)
for item in Set3:
    if item[0].startswith('g'):
        greenCount += 1
        Set5.add(item)
print("Greencount in all sets:", greenCount)
print("Set1:", Set4)
print("Set2:", Set5)
print("Set3:", Set6)
print("You threw me off with the repeating red chocolate")
