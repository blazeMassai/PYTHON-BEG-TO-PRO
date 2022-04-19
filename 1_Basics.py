#creating a variable inside a function with the same anme as the global variable

x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is: " +x)

myfunc()
print("Python is-- " +x)

# use the global keyword if u want to change a global variable inside a function

x='awesom'

def xfunc():
    global x

x='burudani'
xfunc()
print('py is ' +x)