r = int(input("Enter any number"))
n = []
for k in range(r):
    y = int(input("Enter your values"))
    n.append(y)
for i in n:
   if (i % 15==0):
       print('Fizz Buzz') 
   elif (i % 5==0):
       print("Buzz")
   elif(i % 3==0):
       print("Fizz")
   else:
       print(i) 
    



