print("Sets are unordered and unindexed. No duplicate members. Once a set is created, you can't change its items but you can add new items.")

cars={'merce', 'ferrari','toyota','lambo','nissan'}

cars.add('landrover')
print(cars)

bikes={'yamaha','honda','ktm','bmw','kawasaki'}

more_cars ={'honda','audi','vw'}

fancy_cars=['bugati','maserati']

cars.update(more_cars)

more_cars.update(fancy_cars)

print(more_cars)

for x in bikes:
    print(x)

set3 = cars.union(more_cars)
print(set3)