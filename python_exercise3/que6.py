#We have a tuple of numbers given below. Remove the largest number from the tuple and print it in sorted order.
num_tuple = (5, 8, 13, 2, 17, 1)

list = list(num_tuple)
list.remove(max(list))
list.sort()
print(list)

