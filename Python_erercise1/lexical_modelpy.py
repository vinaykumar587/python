#I have four variables, each assigned with certain values given below. A massive expression line follows it. Re-write the expression which suits the desired lexical model.
a = int(input("print the value of a:"))
b = int(input("print the value of b:"))
c = int(input("print the value of c:"))
d = int(input("print the value of d:"))
x = (((a + b) * (a + c) * (a + d)) / ((b + a) * (b + c) * (b + d)) / ((c + a) * (c + b) * (c + d))) * (a * b * c * d)
print(x)