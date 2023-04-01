import random

listrandom = []
for i in range(11):
  listrandom.append(random.randint(-10, 10))
print("list random - ", listrandom)

q=int(input())
l=[]
for i in range(0,q+1):
  l.append(listrandom[i])
print(max(l))
