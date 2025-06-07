n= int(input('inserire il valore della base del triangolo isolscele'))
for i in range (1,n+1,2):
    k=(n-i)/2
    k=int(k)
    print((' '*k)+('*'*i)+(' '*k))
