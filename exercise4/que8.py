#e have a dictionary given below. Copy this dictionary into another dictionary 'replica,' and change the value of the key 103 to 'Sally' in the replica dictionary only. Finally, print both the dictionaries.

student_details = {101:'Judy', 102:'Victor', 103:'Sam'}

new_student_details = student_details.copy()
new_student_details[103] = "Sally"
print(student_details)
print(new_student_details)
