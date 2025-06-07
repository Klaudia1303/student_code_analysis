s= str(input())
n= int(input())

x= False

for i in range(len(s)-n):
    if s[i]== s[i+n]:
        x= True
        
print(x)