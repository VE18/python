p=input("enter")
s=p.split()
# print(s)
t=[]
r=[]
rr=[]
for i in s:
    c=-1
    
    if '#' in i:

        for j in i:
            c+=1
            t.append(j)
            if j=='#':
                b=''.join(reversed(i))
                t[c]=b[c]
        # print(t)
        j=c    
        for i in range(0,c):
            
            if t[i]==t[j]:
                f=1
                
                
            else:
                f=0
                break
            j-=1
        if f==1:
            for i in t:
                r.append(i)
            
        else:
            r.append("@"*c)    

    else:
        r.append(i)
print(r)        
r=r[::-1]        
for i in r:
    rr.append(i)
print(rr)