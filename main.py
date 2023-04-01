import random

listrandom = []
for i in range(11):
  listrandom.append(random.randint(-10, 10))
print("list random - ", listrandom)

l = []
for i in listrandom:
    if i not in l:
        l.append(i)
print(l)