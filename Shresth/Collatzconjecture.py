Number=int(input("Enter your number"))
print(Number)
while(Number!=1):
    if (Number%2==0):
        Number=Number/2
        print(int(Number))
    elif (Number%2!=0):
        Number=Number*3+1
        print(int(Number))
    else:
        break