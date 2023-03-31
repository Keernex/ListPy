import random

listrandom = []
for i in range(11):
  listrandom.append(random.randint(-10, 10))
print("list random - ", listrandom)
listrandom = [1,2,3,4,5,6,7,8,9,10]
maxind = listrandom.index(max(listrandom))
minind = listrandom.index(min(listrandom))
ind = 0
sum = 0
sum2 = 0
sum1 = 0
sumindex3 = 1
dobminmax = 1

sumdodnom = 0
sumdodnoml = []

for j in listrandom:
  if j < 0:
    sum += j
  if j % 2 == 0:
    sum2 += j
  if j % 2 != 0:
    sum1 += j
  if ind % 3 == 0:
    sumindex3 *= j
  if minind < ind and ind < maxind or ind > maxind and minind > ind:
    dobminmax *= j
  if j >= 0:
    sumdodnoml.append(j)
  ind += 1
a = listrandom.index(sumdodnoml[0])
b = listrandom.index(sumdodnoml[-1])
print(listrandom)
c = sum(listrandom[a+1:b])

print(a,b,c)
print("Суму від’ємних чисел.", sum)
print("Суму парних чисел.", sum2)
print("Суму непарних чисел.", sum1)
print("Добуток елементів з індексами, кратними 3.", sumindex3)
print("Добуток елементів між мінімальним та максимальнимелементом.", dobminmax)
print("Суму елементів, що знаходяться між першим та останнім додатним елементом.", c)