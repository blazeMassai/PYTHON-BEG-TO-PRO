f = open(r"D:\\Dyamic_Programming\Python-Beginner-to-Pro\filez\ree.txt", "r")
# f = open("ree.txt", 'rt')
x = open(r"D:\\Dyamic_Programming\Python-Beginner-to-Pro\filez\ree.txt", "r")

y = open(r"D:\\Dyamic_Programming\Python-Beginner-to-Pro\filez\ree.txt", "r")

a = open(r"D:\\Dyamic_Programming\Python-Beginner-to-Pro\filez\ree.txt", "r")

print(f.read())
print('=================')
print(x.readline())
print('=================')
print(y.read(26))
print('=================')

for line in a:
    print(line)

print('-----------write operations---------------')
z=open(r"D:\\Dyamic_Programming\Python-Beginner-to-Pro\filez\imani.txt", "w")
z.write("Now faith is the substance of things hoped for, the evidence of things not seen.")
# z.close()
z=open(r"D:\\Dyamic_Programming\Python-Beginner-to-Pro\filez\imani.txt", "r")
print(z.read())

z=open(r"D:\\Dyamic_Programming\Python-Beginner-to-Pro\filez\imani.txt", "a")

z.write("SOME APPENDED TEXT")
z.close()

# Deleting a file

import os

if os.path.exists(r"D:\\Dyamic_Programming\Python-Beginner-to-Pro\filez\trial.txt"):
    os.remove(r"D:\\Dyamic_Programming\Python-Beginner-to-Pro\filez\trial.txt")
#     to remove directory use os.rmdir
else:
    print("Hiyo file haipoo")
