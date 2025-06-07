#Ex1(file): scrivere la funzione Python che, preso in ingresso il nome di un file di testo, calcoli, usando le 
#espressioni regolari, quante sono le sequenze non sovrapposte di 2 parole consecutive aventi la seguente 
#proprietà: 
#“La due parole sono composte da almeno due caratteri ed hanno a stessa lettera iniziale e 
#la stessa lettera finale, ignorando la distinzione fra maiuscole e minuscole.”
#Ad esempio, prendendo come input il file contenente il seguente testo: 
#tanto va Aldino annaspando in giro che era andato al bar
#la funzione deve restituire come risultato 1.
#Se invece la funzione prende in input
#Ho trovato delle ossa orsa ora vado velato
#deve restituire come risultato 2, infatti le due sequenze sono ossa orsa e vado velato, mentre 
#orsa ora non va bene perché si sovrappone con la prima.
import re
def Ex1(file):
    dossier=open(file,encoding='utf-8')
    leggo=dossier.read()
    dossier.close()
    pattern=r'\b(\w)\w*(\w)\b\W*\b\1\w*\2\b'
    ris=re.findall(pattern,leggo,re.IGNORECASE)
    return len(ris)
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    
###############################################################################

if __name__ == '__main__':
    from tester import tester_fun
    import re

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex1, ["file1_1.txt"] , 1)
    counter_test_positivi += tester_fun(Ex1, ["file1_2.txt"] , 2)
    counter_test_positivi += tester_fun(Ex1, ["file1_3.txt"] , 3)
    counter_test_positivi += tester_fun(Ex1, ["file1_4.txt"] , 3)
    counter_test_positivi += tester_fun(Ex1, ["file1_5.txt"] , 5)

    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
