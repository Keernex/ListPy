import random

listrandom = []
for i in range(11):
  listrandom.append(random.randint(-10, 10))
print("list random - ", listrandom)

ser=sum(listrandom)/len(listrandom)
print("середнє арифметичне ",ser)
l=[]
for i in listrandom:
  if ser<i:
    l.append(i)
print(l)
