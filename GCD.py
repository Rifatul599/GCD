def GCD(a,b):
    if b==0:
        return a
    else:
        return GCD(b,a%b)

a = int(input("Enter a number"))
b = int(input("Enter a number"))

print(GCD(a,b))
