def A_Ex4(filename,anno):
    f=open(filename,'r',encoding='UTF-8')
    a=f.readline().strip().split(',') #prendo la prima riga, non tutte perchè fuori dal ciclo for, e crea una lista
    i=a.index(str(anno)) #cerca nella lista 'a' la posizione della prima volta in cui compare 'anno' dato in input
    M=0 #inizializza il massimo
    for line in f: 
        s=line.strip().split(',') #trasforma tutte le stringhe in liste
        if int(s[i])>=M: #trasforma in intero quante volte venduto l'oggetto nell'anno in input (ovvero quante
                            #volte venduto oggetto in quell'anno)
            res=s[0] #conserva l'oggetto
            M=int(s[i]) #conserva quante volte è stato venduto un determinato oggetto
        elif int(s[i]==M and s[0]>res:
                 res=s[0]
                 M=int(s[i])
    f.close()
    return res
     
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex4, ['Vendite1.csv',2012] , 'Giubbotto')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite2.csv',2012] , 'Maglione')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite2.csv',2013] , 'Zaino')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite3.csv',2011] , 'Giubbotto')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite3.csv',2010] , 'Cellulare')
    
    print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
