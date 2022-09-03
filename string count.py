a=input("enter a or j")
str_count=0
balanced=0

for i in a:
    if i=='a' or i=='A':
        str_count+=1
    if i=='j' or i=='J':
        str_count-=1
    if str_count==0:
        balanced+=1
print("no of balanced value",balanced)