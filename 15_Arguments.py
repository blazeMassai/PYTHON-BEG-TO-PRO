print('------Keyword arguments or kwargs: this arguments which can be sent with the key=value syntax. This way the order of arguments  does not matter.---------')

def watoto(child1, child2, child3):
    print("the youngest child is " +child3)

watoto(child1='Donnie', child2='Rene', child3='Lala')

print('-----Abitrary Keyword Arguments,**kwargs, are used when u dont know how many kwargs will be passed to yo fx: this way yo the fx will receive a dictionary of args and can access the items accordingly------')

def jamaa(**kid):
    print("His last name is " +kid['lname'])

jamaa(fname='Jomo', lname='Fostino', mname='momo')

print('-------default parameters---------')
def kawaida(country='tznia'):
    print('am from ' +country)

kawaida("kenya")
kawaida()

