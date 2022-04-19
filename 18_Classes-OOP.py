print('----Python OOP----')

class Living:
    x='animals'

p=Living()

print(p.x)

print('-----init function-----')

class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age


p1=Person('Don Mendez', 35)

print(p1.name, p1.age)

