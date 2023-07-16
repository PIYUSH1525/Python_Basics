bjp_vote=0
cong_vote=0
while 1:
    age  = int(input("enter your age "))
    if age>=18:
        print("ELIGIBLE")
        vote = input("please entre your vote : BJP/CONG ")
        a =  vote.upper()
        print(a)
        if a == "BJP":
            bjp_vote+=1
            print("Print your vote has been registred")
        elif a == "CONG" :
            cong_vote+=1
            print("Print your vote has been registred")
        print(bjp_vote)
        print(cong_vote)
    else:
        print("jaa beta bada ho ka aa")
        break
print("\nThe total vote of bjp is " , bjp_vote)
print("The total vote of cong is " , cong_vote)
