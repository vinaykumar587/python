#We have the names of six countries given below. Write a Python function to print all the countries that start with the letter 'A.'
countries=['Austraiia', 'India', 'Austria', 'America', 'Russia', 'Iran']

resultcountries= []

for i in countries:
    if i.startswith("A"):
     resultcountries.append(i)
print(resultcountries)

