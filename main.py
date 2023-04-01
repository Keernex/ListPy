list = [
  "as1df", "as23df", "a12s12121df", "adfsdf", "asdfsdsdff", "sdf", "sdf",
  "asdfs"
]
print(list)
p = input("prefix: ")

l = []
for i in list:
  if i.startswith(p):
    l.append(i)
print(l)
