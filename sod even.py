sum=0
d=0
for i in range(100,200):
    while i>0:
        d=i%10
        sum=sum+d
        i=i/10
    print(int(sum))