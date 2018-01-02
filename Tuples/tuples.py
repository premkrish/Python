""" This script contains lessons for tuples """

# List and Tuple have similar features
list1 = [1, 2, 3, 4, 5, 6]
tuple1 = (1, 2, 3, 4, 5, 6)

print(f"Length of list : {len(list1)}")
print(f"Length of tuple : {len(tuple1)}")

#Iterate and print the elements
for n in list1:
    print(f"List element: {n}")

print(80*"-")

for n in tuple1:
    print(f"Tuple element: {n}")

#Tuple's are smaller in size when compared to list
import sys
print(f"Size of List: {sys.getsizeof(list1)}")
print(f"Size of Tuple: {sys.getsizeof(tuple1)}")

#Tuples are immutable - cannot add/edit/delete elements once tuple is created
import timeit
list_time = timeit.timeit(stmt= "[1, 2, 3, 4, 5]",number=100000)
tuple_time = timeit.timeit(stmt="(1,2,3,4,5)",number=100000)
print(f"Time taken to create 1 million list : {list_time}")
print(f"Time taken to create 1 million tuples : {tuple_time}")

#Alternative ways to create tuple
test1 = 1
test2 = 1,2
test3 = 1,2,3

print(test1)
print(test2)
print(test3)

#Adding a comma after a single element would make it as a tuple
test1 = 1,
print(test1)

#Ways to retrieve elements from tuple
user_tuple = (100, "premkumar", "krishnankutty")
userid = user_tuple[0]
fname = user_tuple[1]
lname =user_tuple[2]
print(f"User Id: {userid}")
print(f"First name: {fname}")
print(f"Last name: {lname}")

user_tuple2 = (200,"prem","krish")
userid2,fname2,lname2 = user_tuple2
print(f"User Id: {userid2}")
print(f"First name: {fname2}")
print(f"Last name: {lname2}")

