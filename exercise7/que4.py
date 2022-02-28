#We have a function given below which prints an element from the list. But what if the user calls an invalid index? So, I want you to re-write the following function using the try-except block to handle the IndexError exception.

inp = [10,23,45,78]
def printList():
    try:
        res = inp[5]
    except IndexError:
        print("invalid index,try again.")
printList()