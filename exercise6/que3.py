#Create a function in Python that displays the name and results of a candidate. The function should accept the candidate's name and his/her results as "Pass/Fail." If the result is missing in the function call, show it as "Pass."def

def student(name,results="pass"):
   print("{} is {}".format(name , results))
student("sam")
student("judy","Fail")


