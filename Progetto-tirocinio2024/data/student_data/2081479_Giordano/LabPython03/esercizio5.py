import curses.ascii
import operator

word=input('Insert string: ')
while word.islower()==False or word.isalpha()==False:
    print(word[0]+word[-1])
    word=input('Insert string: ')
if word.islower()==True and word.isalpha()==True:
    print(word[0]+word[-1])
