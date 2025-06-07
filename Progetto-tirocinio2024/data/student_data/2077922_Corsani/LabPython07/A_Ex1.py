#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.1

def A_Ex1(l1, l2):
    for i in range(len(l1)):
        if l1[i] == []:
            l1[i] = 0;
    somma = []
    for i in range(len(l2)):
        appoggio = l1[i] + l2[i]
        somma.append(appoggio)
    return somma

l1 = []
l2 = []

test = True
while test:
    app = int(input("Inserire un numero in l1. Per terminare, inserire 0. Numero: "))
    if app == 0:
        test = False
    else:
        l1.append(app)
test = True
print("-------------------------------------")
while test:
    app = int(input("Inserire un numero in l2. Per terminare, inserire 0. Numero: "))
    if app == 0:
        if len(l1)>len(l2):
            print("l2 deve essere maggiore o uguale a l1. Riprova.")
        else:
            test = False
    else:
        l2.append(app)
for i in range(len(l2)-len(l1)):
    l1.append(0)

print(A_Ex1(l1, l2))

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex1, [[3,6],[3,4,9]] , [6, 10, 9])
    counter_test_positivi += tester_fun(A_Ex1, [[],[3,4,9]] , [3, 4, 9])
    counter_test_positivi += tester_fun(A_Ex1, [[3,6],[3,4]] ,[6, 10])
    counter_test_positivi += tester_fun(A_Ex1, [[1],[9]] ,[10])
    counter_test_positivi += tester_fun(A_Ex1, [[],[9]] ,[9])

    print('La funzione',A_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
