#We have a function given below that adds elements of two lists. However, I can think of two exceptions that can occur in this program.
#The index entered by the user during the function call may be out of bound.
#The list entered by the user can consist of int objects, str objects, or even a combination of both. And what if we try to add an int object and an str object?
#Re-write this program to handle the two exceptions mentioned above.

list1= [10,20,30,40,]
list2=[5,2,3]
def addlists(list1,list2):
    try:
        res = []
        for i in range(4):
            res.append(list1[i]+list2[2])
    except IndexError:
        print("invalid index,try again.")
    except TypeError:
        print("Invalid type,try again.")

addlists(list1,list2)
