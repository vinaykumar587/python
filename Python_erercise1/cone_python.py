#Write a Python program to print the volume of a cone whose height and diameter are given below. (Take pi = 3.14)
h = int(input("height of the cone:"))
d = int(input("diameter of the cone:"))
pi = 3.14
r = d/2
volume = (pi*h*r*r)/3
print(volume)
