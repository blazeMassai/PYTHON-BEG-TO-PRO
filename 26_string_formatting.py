price = 48.457
txt = "the price is {} dollars"
print(txt.format(price))

#below we use 2 decimal places
txt2 = "the price is {:.2f} dollars"
print(txt2.format(price))

quantity = 3
itemno=100
price=60.3288

myorder = "I want {} pieces of item number {} for {:.2f} dollars."

print(myorder.format(quantity,itemno,price))

age=36
name = "Ree"

txt3 = "His name is {1}. {1} is {0} years"
print(txt3.format(age,name))

#named indexes

myorder2 = "I have a {brand}, it is a {model}."
print(myorder2.format(brand="Toyota", model="Prado"))