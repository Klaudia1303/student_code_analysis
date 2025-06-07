primo=0
secondo=0
totale=0

for i in range(1,1000):
    primo=primo+20
    secondo=secondo+1
    totale=secondo+totale
    if primo<=totale:
        break
print(i)
