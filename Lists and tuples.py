print('plop')

first_list = list()
first_list.append(3)
print(first_list)
first_list.append(4)
first_list.insert(1, 'a')
print( first_list)
second_list = ['a', 'b', 'c']
first_list.append(second_list)
print(first_list)
first_list.extend(second_list)
print(first_list)
first_list += second_list
print(first_list)
del first_list[2]
print(first_list)
for i, elt in enumerate(first_list):
    print('{} est situé à l\'indice {}'.format(elt, i))

print(enumerate(first_list))
for elt in enumerate(first_list):
    print(elt)

first_tuple = (1, 2, 3)
print(first_tuple)
first_tuple = (3, 4, 5)
print(first_tuple)


def eucl_div(diviseur, dividande):

    ent_part = diviseur // dividande
    scraches = diviseur % dividande
    return ent_part, scraches


ent_part, scraches = eucl_div(53, 8)

print('Partie entière {}\nReste {}'.format(ent_part, scraches))
