print("hello World")
# VARIABLES
a = 4
print(a)  # integer datatype
a = 4.56  # float data type
print(a)
c = True  # or False boolean
print(c)

d = "Piyush"  # string data type
print(d)

e = None
print(e)

''' TYPECASTING IN PYTHON (CONVERTING ONE DATATYPE TO OTHER )'''
z = "6"  # Here the value of z is in string form
'''print("the value of z is", z+1)'''  # THis will give erro becoz z which is a string is being added to a integer
print("the value of z is", int(z)+1)  # THis will give output coz first z is coverted into the same data type
print("the value of z is", z + "1")  # THis will give output coz both are of the same data type
e = 6
print("the value of e is", e + 1.34)  # will work as well as vice versa

