#Write a Python program to add the three lists given below using Python map and Lambda function.
list_1 = [1, 5, 8]
list_2 = [3, 2, 5]
list_3 = [2, 3, 6]

list4 =map( lambda a,b,c:a+b+c,list_1,list_2,list_3)
print(list(list4))
