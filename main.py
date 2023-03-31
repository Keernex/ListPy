import random

listrandom = []
for i in range(11):
  listrandom.append(random.randint(-10, 10))
print("list random - ", listrandom)

for i in range(0, len(listrandom)):
  if listrandom.count(listrandom[i])>1:
    for j in listrandom:
      if listrandom[i] == j and listrandom.count(listrandom[i])>1:
        listrandom.pop(i)