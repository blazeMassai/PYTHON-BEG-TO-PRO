fruits = ['apple', 'banana', 'cherry', 'pumpkin', 'tango', 'tikiti', 'pera', 'karoti']
print('--fruit list below---')
print(fruits)
print('---first item---')
print(fruits[1])
print('---the last item using negative indexing---')
print(fruits[-1])
print('---range of indexing--- such as fruits[-4:-1]')
print(fruits[-4:-1])
print('---check if cherry fruit exist in list---')

if 'cherry' in fruits:
    print('Yes, Cherry is in the fruitlist')
else:
    print('No it does not')

print('---change a range of items kwa fruits[1:3]---')
fruits[1:3] = ['chungwa','dalansi']
print('--modified list ni--')
print(fruits)

print('---change the 2nd value by replacing with 2 values kwa fruits[1:2]---')
fruits[1:2] = ['ndimu','limao','fenesi']
print('--modified list ni--')
print(fruits)