fruits = ['apple', 'banana', 'cherry', 'pumpkin', 'tango', 'tikiti', 'pera', 'karoti']

print('----fruit lists-----')
print(fruits)
print("----fruit INSERTING elements ie insert nazi as 3rd item-----fruits.insert(2, 'nazi')")
fruits.insert(2, 'nazi')
print(fruits)

print("----fruit APPEND elements to the end of a list ie insert nazi as 3rd item-----fruits.append('korosho')")
fruits.append('korosho')
print(fruits)

print('---To append elements of one list to another we use EXTEND() method fruits.extend(tropical)')

tropical = ['nanasi', 'chungwa', 'papai']
print('---Tropical list---')
print(tropical)
fruits.extend(tropical)
print('---extended fruits with tropical--')
print(fruits)
print("---not ONLY can we extend list to lists but tuple to a list--ie tuple hii matunda=('parachichi', 'mikusu')")
matunda=('parachichi', 'mikusu')
fruits.append(matunda)
print(fruits)
print('--we can loop thru index of the loop----')
for i in range(len(fruits)):
    print(fruits[i])

print('--Or using list comprehensive----')
[print (x) for x in fruits]