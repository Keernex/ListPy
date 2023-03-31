import random

listrandom = []
for i in range(11):
  listrandom.append(random.randint(-10, 10))
print("list random - ", listrandom)

q=[]
for i in listrandom:
  q.append(i**2)
print(q)