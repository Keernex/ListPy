import random

listrandom = []
for i in range(11):
  listrandom.append(random.randint(-10, 10))
print("list random - ", listrandom)

q=0
w=0
for i in listrandom:
  if i>-1:
    q+=1
  else:
    w+=1
print("parni: ", q)
print("ne parni: ", w)