#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.6


def A_Ex6(l1, l2):
    l =[] 
    for i in range(len(l1)):
        if l1[i] not in l2:
            l.append(l1[i])
    l.sort()
    return l;



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
        test = False
    else:
        l2.append(app)
    
print(A_Ex6(l1,l2))

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex6, [[1, 3, 2, 1, -5],[1, 3]],[-5, 2])
    counter_test_positivi += tester_fun(A_Ex6, [[1, 3, 2, 1, -5],[1, 1, 1]],[-5, 2, 3])
    counter_test_positivi += tester_fun(A_Ex6, [[10, 1, 10, 1, 2],[10, 1, 2]],[])
    counter_test_positivi += tester_fun(A_Ex6, [[],[1, 1, 1]],[])
    counter_test_positivi += tester_fun(A_Ex6, [[100, 12, -2, -1, -2],[]],[-2, -2, -1, 12, 100])

    print('La funzione',A_Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
