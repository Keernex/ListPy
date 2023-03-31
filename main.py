import random

listrandom = []
for i in range(11):
  listrandom.append(random.randint(-10, 10))
print("list random - ", listrandom)

q=listrandom.index(max(listrandom))
w=listrandom.index(min(listrandom))
e=min(listrandom)
r=max(listrandom)

listrandom[q]=e
listrandom[w]=r
print(q,w)
print(listrandom)