#Write a function to reverse a string if it's length is an even number. I think of the TypeError exception if a numeric value is passed inside the function call. But there might be other exceptions too that can occur while executing the program.
#So, wrap the function around a try-except block and handle the TypeError exception with the message 'Check the string.' For all other exceptions, print the message 'Something went wrong.'
def checkstring(str1):
    try:
        strlen = len(str1)
        if str1.isnumeric():
            raise TypeError
        print(str1[::-1])
    except TypeError:
        print("Check the string.")
    except:
        print("something went wrong.")
str1 = input("enter string:")
checkstring(str1)

