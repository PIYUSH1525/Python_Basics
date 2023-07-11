l = [3,5,32,1,9,8]
m= [8,1,6,0,"APPLE",56]
a=type(l)                                             # LIST IS MUTABLE
print(a)                                              # CHANGES ARE DIRECTLY DONE IN MAIN LIST NO SEPRATED LIST IS CREATED

# METHODS AVILALABLE IN LIST
b= l.count(3)
print("the count of number is" ,b)
l.sort()                                               # CAN DONE IN SAME DATA TYPE
l.append("piyush")                                     # ADD ITEM TO THE LAST OF THE LIST
print(l.index(32))
l.pop(0)                                               # POP REMOVE THE LAST ELEMENT OF THE LIST WHEN NO INDEX IS GIVEN
m.extend(l)                                            # TO ADD TWO LIST TOGETHER
print(l.index(32))
print(l[0:3])                                          # SLICICNG OF LIST
print(m)
l[0] = "PIYUSH "
print(l)



list1=[80,90,100,120]
print(list1[::-2])                       #$ IMPORTANT
print(13//4)

import math
print(math.sqrt(25))

tup1= (4,9,11,23)
print(tup1[1:4])
