base= int(input())


for i in range(1,base+1,2):
    k=(base-i)/2
    k=int(k)
    print((" "*k)+("*"*i)+(" "*k))


    