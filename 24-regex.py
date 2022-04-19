import re
txt = "The rain in Spain"
neno = "We are the chosen_ generation, a royal priesthood"
riri = "The 5 bird_ on the 3 walls 15"

x = re.search("^The.*Spain$", txt)
y = re.findall("[*a-s+]", txt)
z = re.search("The|in", txt)
a = re.search(r"\AWe", neno)
b = re.search(r"\bpriesthood", neno)
c = re.findall(r"\d", riri)
d = re.findall(r"\D", riri)
e = re.findall(r"\s", riri)
f = re.findall(r"\S", riri)

g = re.findall(r"\w", riri)
h = re.findall(r"\W", riri)
j = re.findall(r"[a-n]", riri)
k = re.findall(r"[0-9]", riri)

ab=re.split("\S", txt)#split at evry non white space
ac=re.split("\s", txt, 2) #split the string at the 2nd appearance
ad=re.sub("\s","5", txt) #substuting every space with 5

l = re.search(r"\bS\w+", txt) #looks for any words that starts with upper case S

print(x)
print(x.span()) #this is a match object
print(y)
print(z)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(j)
print(k)
print(ab)
print(ac)
print(ad)
print(l.span()) #print the position(start-and end position) of the first match occurence
print(l.string) #printing the passed string
print(l.group()) #printing the part of the string that is matching
