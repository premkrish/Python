""" This script contains lessons for Sets """
'''Enter command dir(set) in the python terminal to display all methods and properties in it 
and then use help(set."props/methods") - Ex: help(set.add) to get more insight on the add  method'''

# Instantitate a set
testset = set()
print(testset)

#Instantitate a set with values
testset1 = set([10, 3.14567, True, "Test"])
print(testset1)

#Add/Pop/Remove/Discard from sets
integer = set([1, 2, 3, 4, 5])
print(integer)
integer.add(6)
print(integer)

#remove would throw an error if the element doesn't exist
integer.remove(6)
print(integer)

#discard would exit quietly if the element doesn't exist
integer.discard(6)
print(integer)

#pop would remove an element and return it from the set
print(integer.pop())

#Union,Intersection
odds= set([1, 3, 5, 7, 9])
even= set([2, 4, 6, 8, 10])
print(odds.union(even))
print(odds.intersection(even))