#somma tutti gli interi negativi trovati

n = input("intero n = ")
negativi = 0

while n != '*':
    if int(n) < 0:
        negativi = negativi+int(n)
    n = input("prossimo = ")

print(negativi)
