a = [45, 24, 35, 67, 88, 92, 73, 46, 23, 55]
b = [55, 72, 70, 33, 12, 8, 23, 37, 98, 60]
c = []
for i in a:
    for k in b:
        t = i + k
        if (t==100):
            print("Godzilla")
        elif (t!=100):
            c.append(t)
print(c)