import json

x ='{"name":"Ryn", "age":31, "city":"Arusha"}'

y = json.loads(x)

print(y["age"])

a = {
    'make':'Toyota',
    'mode':'athlete',
    'year':2019
}

b=json.dumps(a)
print(b)

print('---jason dump with all data formats---')
c = {
    'make':'Toyota',
    'mode':'athlete',
    'year':2019,
    'petrol':True,
    'related':('royal crown','majesta'),
    'turbo':None,
    'Other-brands': [
        {'brand':'benz','mpg':29.5},
        {'brand': 'vw','mpg': 24.1}
    ]
}

d = json.dumps(c, indent=4, separators=(",", "="))
print(d)