a =' Hello, world'

print('uppercase:' + a.upper())
print('lowercase:' + a.lower())
print('remove spaces from the beginning:' + a.strip())
print('replace string:' + a.replace('H','Y'))
print('below is split string')
print(a.split("," ))

print('-----------------')
print('below is string format:')
age = 32
txt = 'My age is {}'
print(txt.format(age))
quantity = 3
itemno = 567
price = 49.95

myorder = "I want to pay {2} dollars for {0} pieces of item {1}"

print(myorder.format(quantity, itemno, price))
print('-----------------')
print('below is string escape characters or backlash, that is using illegal characters:')
escape = "We are the so called \"Vikings\" from the North"

print(escape)
print('-----------------')
print('String methonds below')
c = 'karamajong'
print('capitalize first letter with capitalize meth: ' + c.capitalize())

print('return center string: ' + c.center(20))
print(c.isidentifier())
# print(c.lstrip())