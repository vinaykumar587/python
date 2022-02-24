#A list of tuples is given below, containing the candidate's name and their heights(in cm). Sort this list using Lambda functions according to the heights of the candidates.

candidate_details = [('Harry', 168), ('Jhonny', 160), ('Brad', 178), ('Chris', 172)]
candidate_details.sort(key =lambda x:x[1])
print(candidate_details)
