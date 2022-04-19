print('tuples r used to store multiple items in a single variable. Tuples are ordered  and unchangeable. Tuple items have an order and cannot change. Items r unchangeable becoz we cannot change add or remove items after the tuple is created. But tuples allow duplicate values')

thistuple=('apple', 'banana', True, 123, 'cherry')

print(thistuple)

print("The tuple() constructor can be used to make a tuple")
print("mytuple=thistuple(('apple', 'banana', True, 123, 'cherry'))")

mytuple = tuple(('cats', 'birds', True, 123, 'dogs', 'fish','hulk'))

print(mytuple)

print('print the last item of a tuple')
print(mytuple[-1])

print('in index range')
print(mytuple[1:5])

print('convert tuple to list')
y=list(mytuple)

y.append("drax")
print(y)

tx = tuple(y)

print(tx)