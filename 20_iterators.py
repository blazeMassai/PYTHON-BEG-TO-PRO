print('----------iterators--------')
mytuple=('apple','banana','cherry')
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

x = 'dracula'

hesabu=iter(x)

print(next(hesabu))
print(next(hesabu))
print(next(hesabu))

print('-----------create an iterator-------')

class myNumbers:
    def __iter__(self):
        self.a = 10
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = myNumbers()

zaga=iter(myclass)
print(next(zaga))
print(next(zaga))
print(next(zaga))