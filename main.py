import random

listrandom = []
for i in range(11):
  listrandom.append(random.randint(-10, 10))
print("list random - ", listrandom)

listrandom2 = []
for i in range(11):
  listrandom2.append(random.randint(-10, 10))
print("list random 2 - ", listrandom2)
list=listrandom+listrandom2
l = []
for i in list:
    if i not in l:
        l.append(i)
print(l)