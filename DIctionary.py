#Dictionary Creation

friends = {'Rakesh':'123 456 789',
           'Fattu': '987 654 321'}

#Printing
print(friends)

#operations:

print(friends['Fattu']) #print the value related to this key

# Adding Elements to the dictionary
friends['Ranjan'] = '984 471 46 17'
print(friends)

#Modify Elements:

friends['Rakesh'] = '909 777 20 20'
print(friends)

#Deleting an entry from dictionary

del friends['Fattu']
print(friends)

friends['Fattu'] = '333 444 55 66'
print(friends)

#Looping in Dictionary
for x in friends:
    print(x, ":",friends[x])

#Printing Length of dictionary:

print(len(friends))

#Print the keys of a dictionary:
print(friends.keys())

#print the values in a dictionary:
print(friends.values())

#Print the value of a specific key in a dictionary:
print(friends.get('Rakesh'))


