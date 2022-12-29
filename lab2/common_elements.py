def common(list1, list2):
  set1 = set(list1)
  set2 = set(list2)

  if len(set1.intersection(set2)) > 0:
      return list(set1.intersection(set2)) 
  else:
      return []

list1 = ['a', 'b', 'c']
list2 = ['c', 'a', 'z']

print(common(list1, list2))

print(list1, list2)