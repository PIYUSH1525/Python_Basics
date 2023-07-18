# Match-Case is the Switch Case of Python
# Here we have to first pass a parameter then try to check with which case the parameter is getting satisfied. If we find a match we will do something and if there is no match at all we will do something else.
# We can also use if else statement

a = int(input("enter something"))
match a:
    case 1:
        print("name is Piyush")
    case 2:
        print("name is Amit")
    case 3:
        print("name is Sushma")
    case 4:
        print("name is Shruti")
    case _:                               # by default value
        print("No match")