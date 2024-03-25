Set1 = {'b1', 'g2', 'r3', 'b4', 'g5'}
Set2 = {'g1', 'b2', 'r3', 'b5', 'r6', 'g7'}
Set3 = {'r1', 'b9', 'g3', 'r4', 'r5', 'g6', 'b7'}
Set4 = set()
Set5 = set()
Set6 = set()
for item in Set1:
    if item[0].startswith('g'):
        Set5.add(item)
    elif item[0].startswith('r'):
        Set6.add(item)
    elif item[0].startswith('b'):
        Set4.add(item)
for item in Set2:
    if item[0].startswith('b'):
        Set4.add(item)
    elif item[0].startswith('r'):
        Set6.add(item)
    elif item[0].startswith('g'):
        Set4.add(item)
for item in Set3:
    if item[0].startswith('b'):
        Set4.add(item)
    elif item[0].startswith('g'):
        Set5.add(item)
    elif item[0].startswith('r'):
        Set6.add(item)
print("Set1:", Set4)
print("Set2:", Set5)
print("Set3:", Set6)