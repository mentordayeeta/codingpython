Value=0
buttonpress=input("Button 1 or Button 2?").lower()
while(Value!=-1):
  if(buttonpress=="1"):
    Value+=10000
    print("Added 10,000 to your value!")
    print("Your current value is ",Value)
    buttonpress=input("Another go?:")
  elif(buttonpress=="2"):
    Value+=100
    print("Added 100 to your value!")
    print("Your current value is ",Value)
    buttonpress=input("Another go?:")
  else:
    print("Either press 1 for adding 10,000 or 2 for adding 100,thanks!")
    buttonpress=input("Try again!:")