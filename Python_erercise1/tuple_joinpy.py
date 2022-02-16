#We have the name and seat numbers of a student given below as two tuples. With this given data, print the students' names and their assigned seat numbers in a single line using the appropriate data type.

name = ('Shaun','Ron','Michael')
seat_numbers = (101,102,103)
join = {}
for i in range(len(seat_numbers)):
    join[name[i]] = seat_numbers[i]
print(join)