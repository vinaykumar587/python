#Print the number and the cube of that number in a dictionary from 0 to 5.

set1 =(0,1,2,3,4,5)
set2 =(0,1,2,3,4,5)

join = { }
for i in range(len(set2)):
    join[set1[i]] = set2[i]**3
print(join)