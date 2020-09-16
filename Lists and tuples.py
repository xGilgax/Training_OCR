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


chain = "Hello my name is Stein"
list_of_string = ['My', 'name', 'is', 'Stein']

split_chain = chain.split()
print('split chain:  {}'.format(split_chain))

list_to_chain = " ".join(list_of_string)
print(("List to chain: {}".format(list_to_chain)))

def display_float(number):
    try:
        number = float(number)
    except ValueError:
        print('Not a number')
    split_number = str(number).split('.')

    return ','.join([split_number[0], split_number[1][:3]])

print(display_float(9.7896))


def afficher(*parameters, sep=' ', end='\n'):

    parameters = list(parameters)
    for i, parameter in enumerate(parameters):
        parameters[i] = str(parameter)
    chain_to_display = sep.join(parameters)
    chain_to_display += end
    print(chain_to_display)

    return chain_to_display

chain_to_display = afficher(first_list, first_tuple)

print(chain_to_display)
