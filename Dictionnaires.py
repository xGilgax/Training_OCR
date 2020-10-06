first_dict = dict()
print(type(first_dict))

first_dict["Name"] = "Bob"
first_dict["Firstname"] = "Jean"

print(first_dict)

print(first_dict['Name'])
#print(first_dict['Names'])


for description in first_dict.keys():
    print(description)
    print(first_dict[description])

for key,value in first_dict.items():
    print('{}: {}'.format(key, value))
