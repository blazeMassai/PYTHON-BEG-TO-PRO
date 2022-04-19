# try:
#     print(x)
# except:
#     print("An execution error")

#---------------------------------------------

# try:
#     print(y)
# except NameError:
#     print("variable y isn't defined")
# except:
#     print("something else went wrong")

#------------------------------------

# try:
#     print("yey")
# except:
#     print("variable y isn't defined")
# else:
#     print("something else went wrong")

#--------------------------------------

x = input("Enter a number: ")
if 7 > int(x):
    raise Exception("Sorry, no numbers below 7 allowed")