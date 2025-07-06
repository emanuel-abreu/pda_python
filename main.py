# .\.venv\Scripts\python.exe -m pip install readchar #import threading #import readchar
from PDA import PDA
from State import State
from Test import *

if __name__ == "__main__":
    Test.multiplo3('00001111')
    Test.multiplo3('1010')
    Test.reverso('101010')
    Test.reverso('10100101')
    Test.reverso('1001001001')

    Test.calc('a*a+(a+a)')
    Test.calc('((a+a)*a)')

    Test.enquanto('eqt(a){eqt(a){}}eqt(a){}')
    Test.enquanto('eqt(a){eqt(a){eqt(a){}}}')
    Test.enquanto('eqt(a){eqt(a){}}')
    Test.enquanto('eqt(a){eqt(a){}')
