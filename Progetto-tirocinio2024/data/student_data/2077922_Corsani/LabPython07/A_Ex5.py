#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.5


def A_Ex5(l):
    app = []
    for i in range(len(l)):
        app2 = 0
        for j in range(len(l[i])):
            app2 = app2 + ord(l[i][j])
        app.append(app2)
    return app


l = []

test = True
while test:
    app = input("Inserire una stringa, premere * per fermarsi. Stringa:  ")
    if app == '*':
        test = False
    else:
        l.append(app)

print(A_Ex5(l))
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex5, [["ama","ma","amaca"]], [303,206,499])
    counter_test_positivi += tester_fun(A_Ex5, [[]], [])
    counter_test_positivi += tester_fun(A_Ex5, [["c"]], [99])
    counter_test_positivi += tester_fun(A_Ex5, [["ciao",""]], [412,0])
    counter_test_positivi += tester_fun(A_Ex5, [["",""]], [0,0])

    print('La funzione',A_Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
