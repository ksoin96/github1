x = int(input("Limit:"))
a=0
b=0
while b < x:
    a+=1
    b+=a
    if b>=x:
        print(b)
        