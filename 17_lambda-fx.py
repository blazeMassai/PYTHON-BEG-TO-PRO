print('lambda are small anonymous fnxs')

x=lambda a:a+10

print(x(5))

print('-----------ex: 2--------------')
y=lambda a,b: a*b
print(y(5,6))

print('---function within function----')
def mfx(n):
    return lambda a:a*n

mydoubler=mfx(2)

print(mydoubler(10))