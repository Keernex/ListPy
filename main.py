import random

listrandom = []
for i in range(11):
  listrandom.append(random.randint(-10, 10))
print("list random - ", listrandom)

q=[]
for i in listrandom:
  if i>-1:
    q.append(i)
print("dodatni+: ", q)