#We have a list of numbers given below. Print the square of these numbers into another list using list comprehension.
num = [2, 4, 6, 8]
squaring_iterator = map(lambda n: n ** 2, num)
squared_numbers = list(squaring_iterator)
print(squared_numbers)

