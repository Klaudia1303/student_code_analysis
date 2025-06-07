#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.4


def A_Ex4(l):
    lista = [];
    if len(l) == 0:
        lista.append('')
        return l
    else:
        for i in range(len(l)):
            if l[i]%2 != 0:
                lista.append("D")
            else:
                lista.append('P')
        return lista

l = []

test = True
while test:
    app = int(input("Inserire un numero in l. Per terminare, inserire 0. Numero: "))
    if app == 0:
        test = False
    else:
        l.append(app)

print(A_Ex4(l))

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex4, [[3,7,8,9]], 'DDPD')
    counter_test_positivi += tester_fun(A_Ex4, [[3]], 'D')
    counter_test_positivi += tester_fun(A_Ex4, [[8]], 'P')
    counter_test_positivi += tester_fun(A_Ex4, [[]], '')
    counter_test_positivi += tester_fun(A_Ex4, [[7,7,7,7,8]], 'DDDDP')

    print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)