a = 0
b = 0
for i in range(0,16,2):
    a = i+b
    b = i*a
    print(i,a,b)
