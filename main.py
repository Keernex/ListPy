import random

listrandom = []
for i in range(11):
  listrandom.append(random.randint(-10, 10))
print("list random - ", listrandom)

parni = []
noparni = []
dod = []
nodod = []
for j in listrandom:
  if j % 2 == 0:
    parni.append(j)
  if j % 2 != 0:
    noparni.append(j)
  if j < 0:
    dod.append(j)
  if j > -1:
    nodod.append(j)

print("парні числа з першого списку;", parni)
print("непарні числа з першого списку;", noparni)
print("від’ємні числа з першого списку;", dod)
print("додатні числа з першого списку.", nodod)