def all_permutations(permList, nameList):
  if len(nameList) == 0:
    for i in range(len(permList)):
      print(permList[i], end=' ')
    print()
  else:
    for i in range(len(nameList)):
      newPerm = [x for x in permList] + [nameList[i]]
      newNameList = [x for x in nameList]
      newNameList.pop(i)
      all_permutations(newPerm, newNameList)
if __name__ == '__main__':
  nameList = input().split(' ')
  permList = []
  all_permutations(permList, nameList)