simple_words = '   helLo EVeryOne      '

print(simple_words.capitalize())
print(simple_words.lower())
print(simple_words.upper())
print(simple_words.strip())
print(simple_words.center(40))
print(simple_words.strip().capitalize())

a = 'Hello'
b = 'My name is'
c ='Stein'

print('{} everyone!! {} and will always be {}'.format(a, b, c))

print(len(simple_words[5]))
print(a[1:])
print(a[:len(a)])
print(a[:len(a)-2])
print('yo', a.count('l', 2, 4))
help(str.replace)
print(a.replace('l',b))
print(len(a))
print(a[0])
print(a[:254753425])
for char in a:
    print(char)