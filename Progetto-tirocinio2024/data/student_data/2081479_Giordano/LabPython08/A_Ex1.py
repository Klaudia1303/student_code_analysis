def A_Ex1(l):
    listLetters=[]
    currentWordLetters=[]
    for word in l:
        for letter in word:
            if not letter.islower():
                continue
            elif letter not in currentWordLetters:
                currentWordLetters.append(letter)
        for append in currentWordLetters:
            listLetters.append(append)
        currentWordLetters=[]
    topLetter=''
    topLetterCount=0    
    for letterTopCount in (listLetters):
        if listLetters.count(letterTopCount)>=topLetterCount:
            topLetter=letterTopCount
            topLetterCount=listLetters.count(letterTopCount)
    return topLetter
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex1, [["casa", "senape", "ketchup", "pasta"]] , "s")
    counter_test_positivi += tester_fun(A_Ex1, [["a", "b", "b", "a", "a", "a", "a"]] , "a")
    counter_test_positivi += tester_fun(A_Ex1, [["1fI", "1FI", "1FI", "1FI","1FI" ]] , "f")
    counter_test_positivi += tester_fun(A_Ex1, [["conte", "dpcm"]] , "c")
    counter_test_positivi += tester_fun(A_Ex1, [["Zlatan", "Ibraimovich", "Cristiano", "Ronaldo", "Francesco", "Totti"]] , "o")


    print('La funzione',A_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
