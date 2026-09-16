# list=[45, 24, 35, 67, 88, 92, 73, 46, 23, 55]
# user=int(input("Guess a number!:"))
# if(user in list):
#   print("Correct!")
# else:
#   print("Wrong...")

# list=[]
# user=int(input("How many number in your list?:"))
# x=user
# while(user!=0):
#   num=int(input("Enter a number!:"))
#   list.append(num)
#   user-=1
# user=int(input("Guess a number from that list!:"))
# score=0
# while(score!=x):
#   if(user in list):
#     print("Correct!")
#     score+=1
#     print("Your score is ",score)
#     user=int(input("Have another go!:"))
#   else:
#     print("Wrong...")
#     print("Try again!")
#     user=int(input("Try again!:"))

while(user!=0):
  num=int(input("Enter a number!:"))
  list.append(num)
  user-=1
user=int(input("Guess a number from that list!:"))
score=0
while(score!=x):
  if(user in list):
    print("Correct!")
    score+=1
    print("Your score is ",score)
    for i in list:
      print("Count the number of this twxt to find out how many instances of this number!")
    user=int(input("Have another go!:"))
  else:
    print("Wrong...")
    print("Try again!")
    user=int(input("Try again!:"))