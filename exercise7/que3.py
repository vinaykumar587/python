# We have a program given below that generates an AttributeError exception. Make changes in the program to handle this exception and print the message 'An error occured.'

inp = 10
try:
    inp.append(5)
except AttributeError:
    print("An error occured")