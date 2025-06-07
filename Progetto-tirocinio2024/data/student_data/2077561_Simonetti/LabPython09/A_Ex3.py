def A_Ex3(fileName):
    subjects=set()
    with open(fileName,encoding='UTF-8') as fin:
        next(fin)
        totalList=[]
        for line in fin:
            line=line.strip().split(',')
            totalList.append(line)
        subjDict={}
        for i in totalList:
            subjDict[i[2]]=subjDict.get(i[2],0)+int(i[1])
        for subj in subjDict:
            if subjDict[subj]>=58:
                subjects.add(subj)
            
    return subjects
                        
                            
                            
            

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun
    
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex3, ["esami1.csv"], {'Fisica'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami2.csv"], set())
    counter_test_positivi += tester_fun(A_Ex3, ["esami3.csv"], {'Ricerca Operativa','Analisi'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami4.csv"], {'Basi di Dati'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami5.csv"], set())

    print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
