n=int(input("Inserire una sequenza di numeri, inserirne uno divisibile per 5 per terminare: "))
while(n%5!=0):
    n=int(input())
print(n//5)
