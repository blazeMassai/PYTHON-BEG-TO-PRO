import mymodule

mymodule.greeting("Ree")

a = mymodule.person['country']

print(a)

print('--------Built In Modules--------')

import  platform
import datetime

x=platform.system()
y=datetime.datetime.now()

print(x)
print(y)
print('-----returning year and name of weekday-----')
print(y.year, y.strftime("%A"),y.strftime("%w"), y.strftime("%b"))