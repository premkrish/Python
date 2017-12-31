""" This script contains lessons for list """

#Instantitate a list
list1 = [1, 2, 3, 4, 5]
print(list1)

list2 = [6, 7, 8, 9, 10]
print(list2)

#concatenation - maintains order
print(f"List 1 + List 2: {list1 + list2}")
print(f"List 2 + List 1: {list2 + list1}")

#Add item to list
list1.append(6)
print(type(list1))
print(list1)

#insert element at a given index
list1.insert(2, 25)
list1.insert(0, 34)
print(list1)

#Sort List
list1.sort()
print(list1)

#Reverse list
list1.reverse()
print(list1)

#Count no of times an element appears
list1 = [3, 4, 6, 6, 5, 2, 1]
print(list1.count(26))

#pop - removes element from the last
print(list1.pop())

#remove - removes first occurence of a value
list1.remove(6)
print(list1)

#clear - clears all elements of the list
list1.clear()
print(list1)