print('dictionary is uniordered and changeable')

car={
    'brand':'toyota',
    'model':'athlete',
    'year':2019
}

x=car.keys()
print(x)
y=car.values()
print(y)
z=car.items()
print(z)

car['year']=2020
print(car)

car['color']='red'
print(car)

for x,y in car.items():
    print(x,y)


print('Nested dictionaries')

myfamily = {
    "child1" : {
    "name" : "Emil" ,
    "year" : 2004
    },
    "child2" : {
    "name" : "Tobias" ,
    "year" : 2007
    },
    "child3" : {
    "name" : "Linus" ,
    "year" : 2011
    }
}

print(myfamily)