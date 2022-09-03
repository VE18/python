n=int(input("enter lim"))
s=64
for i in range(0,n):
    s+=1
    for j in range(0,(i+1)):
        print(chr(s),end=" ")
        n=n+1
    print("\n")