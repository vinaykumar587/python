#Reverse the integer given below.
n = 5623
rev =0
while (n>0):
    rev=(rev*10)+n%10
    n=n//10
    print(rev)