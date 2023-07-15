a = { 3,5,4,6,6}
b = {2,5,5,5,5,5,5,7,8,9}                # one element is counted only one time
c = {3,5,4,6}                            # a nd c are both same sets
d = set()                                # EMPTY SET
print(type(d))
print(b)
a.clear()
print(b.pop())                           # random element will pop
print(b)
print(a)