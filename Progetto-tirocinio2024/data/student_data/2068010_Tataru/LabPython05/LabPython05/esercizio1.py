a=input()
b=input()
output=""
for i in range(len(a)*2):
    if i%2==0:
        output+=a[i//2]
    else:
        output+=b[i//2]
print(output)