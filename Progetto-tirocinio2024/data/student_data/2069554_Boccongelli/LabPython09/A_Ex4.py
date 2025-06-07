def A_Ex4(filename,anno):
    f = open(filename, 'r', encoding="UTF-8")
    t = f.read().split('\n') #Trasformi il file in una lista di stringhe
    f.close()
    m = 0 #Massimo
    obj = '' #L'oggetto finale
    for i in range(1, len(t)): #Looppi nella lista di stringhe
        s = t[i].split(',') #Crei una lista di valori (Per ogni stringa del file)
        n = t[0].split(',').index(str(anno)) #Trovi a che index sta l'anno
        if (int(s[n]) > m): #Se il valore alla posizione dell'anno > max
            m = int(s[n]) #Max diventa il nuovo valore
            obj = s[0] #Ti segni l'oggetto che ha questo valore (obj alla pos 0)
        elif (int(s[n]) == m): #Se il valore alla posizione dell'anno == max
            obj = max(obj, s[0]) #Ti segni l'oggetto massimo alfabeticamente
    return obj #Dopo che hai controllato ogni oggetto
            
     
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
