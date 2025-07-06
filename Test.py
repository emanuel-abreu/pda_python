from State import State
from Util import Util
from PDA import PDA
class Test:
    @staticmethod
    def mensagem():
        print("\nPara reconhecer, é necessário implementar o método PDA.run, no PDA.py!")
        print("\nEm PDA.py existe a \"pilha\", para ser trabalhada juntamente com a palavra \"w\" recebida em PDA.run(w)!")

    @staticmethod
    def calc(w):
        print("TODO: para utilizar o PDA aqui!")

    @staticmethod
    def enquanto(w):
        print("TODO: para utilizar o PDA aqui!")

    @staticmethod
    def multiplo3(w): # Exemplo 1: Binário múltiplo de 3
        print("Exemplo:")
        print("{ w in Σ^* | w é um número binario multiplo de 3}")
        q0 = State('q0')
        q1 = State('q1')
        q2 = State('q2')
        q0.setFinal()

        q0.addTransition(q0, '0', None, None)
        q0.addTransition(q1, '1', None, None)
        q1.addTransition(q0, '1', None, None)
        q1.addTransition(q2, '0', None, None)
        q2.addTransition(q2, '1', None, None)
        q2.addTransition(q1, '0', None, None)

        pda = PDA(q0)
        b = pda.run(w)
        Util.checkout(b, w)
        Test.mensagem()

    @staticmethod
    def reverso(w): # Exemplo2: L = { ww^R | w in Σ^*={0,1}}
        q1 = State('q1')
        q2 = State('q2')
        q3 = State('q3')
        q4 = State('q4')
        q4.setFinal()

        q1.addTransition(q2, None, None, '$')
        q2.addTransition(q2, '0', None, '0')
        q2.addTransition(q2, '1', None, '1')
        q2.addTransition(q3, None, None, None)
        q3.addTransition(q3, '0', '0', None)
        q3.addTransition(q3, '1', '1', None)
        q3.addTransition(q4, None, '$', None)

        pda = PDA(q1)
        b = pda.run(w)
        Util.checkout(b,w)
        Test.mensagem()
