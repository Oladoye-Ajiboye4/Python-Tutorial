text = 'This is a very short text'
# slice - variable_name[starting_indedx:end_index:step]
# print(text[0:9:2])
# print(text[10:25])
# print(text[:10])
# print(text[10:])
# print(text[:])
# print(text[-10::2])

# String methods 

print(type('A string'))

my_sentence = 'I am a Python developer'
# upper() to convert to uppercase
# print(my_sentence.upper())
# print(my_sentence.lower())
# print('  A string  '.strip())

age = 92
name = 'Gideon'
department = 'Computer Science'
print('My name is ' + name + '. I\'m in ' + department + ' . My age is ' + str(age))
# format string
print(f'My name is {name}. I\'m in {department}. My age is {age}')
