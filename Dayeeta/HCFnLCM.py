a = int(input("Enter first number: ")) #a=12
b = int(input("Enter second number: ")) #b=18

#HCF must be smaller than the smallest number

hcf = 1
minimum=min(a,b)

for i in range (1,minimum+1):
    if a%i==0 and b%i==0:
        hcf = i

print("HFC is ", hcf)

# lcm * hcf = a * b

lcmp= (a * b)/hcf
print("LCM using product is ", lcmp)

lcm = max(a,b)

while lcm % a != 0 or lcm % b != 0:
    lcm +=1

print("LCM is ", lcm)

#HCF = 6
#LCM = 36