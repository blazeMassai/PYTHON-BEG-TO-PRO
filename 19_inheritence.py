class Birds:
    def __init__(silly, name, wingspan):
        silly.name=name
        silly.wingspan=wingspan

z=Birds('Eagle',6)

print(z.name, z.wingspan)

print('----inheritence----------')

class Hawk(Birds):
    pass

p=Hawk('Kipanga',8)

print(p.name)

# init method overides the parent class unless u call as line 24
class Parrot(Birds):
    def __init__(self, color, habitat):
        self.color=color
        self.habitat=habitat
        # Birds.__init__(self, color, habitat)


pz=Parrot('blue','trees')

print(pz.color, pz.habitat)