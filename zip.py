# Create a list of tuples: mutant_data
mutants = ['charles xavier', 'bobby drake', 'kurt wagner', 'max eisenhardt', 'kitty pryde']
aliases = ['prof x', 'iceman', 'nightcrawler', 'magneto', 'shadowcat']
powers= ['telepathy', 'thermokinesis', 'teleportation', 'magnetokinesis', 'intangibility']


mutant_data = list(zip(mutants,aliases,powers))

# Print the list of tuples
print(mutant_data)

# Create a zip object using the three lists: mutant_zip
mutant_zip = zip(mutants,aliases,powers)

# Print the zip object
print(mutant_zip)

# Unpack the zip object and print the tuple values
for value1,value2,value3 in mutant_zip:
    print(value1, value2, value3)



#Create dictionary from lists with keys & values


L1 = ['a','b','c','d']
L2 = [1,2,3,4]
d = dict(zip(L1,L2))
print(d)