from State import State
from Util import Util
from PDA import PDA


class Test:

    @staticmethod
    def calc(w: str):
        """
        Reconhece strings que contêm 'a', operadores '+' e '*',
        e que têm parênteses bem balanceados.
        (Não verifica sintaxe completa de expressão, apenas
        símbolos válidos e balanceamento de parênteses.)
        """
        print("Teste CALC:")
        print(f"  w = {w}")
        # Estado único q0
        q0 = State('q0')
        q0.setFinal()

        # Transições para símbolos a, +, *
        for c in ['a', '+', '*']:
            q0.addTransition(q0, c, None, None)

        # Empilha '(' e desempilha ')' para balanceamento
        q0.addTransition(q0, '(', None, '(')
        q0.addTransition(q0, ')', '(', None)

        pda = PDA(q0)
        b = pda.run(w)
        Util.checkout(b, w)
        print()

    @staticmethod
    def enquanto(w: str):
        """
        Reconhece cadeias do tipo eqt(a){...} aninhadas ou em sequência,
        garantindo que `{` e `}` fiquem balanceados.
        """
        print("Teste ENQUANTO:")
        print(f"  w = {w}")
        q0 = State('q0')
        q0.setFinal()

        # Letras de "eqt(a)"
        for c in list("eqt(a)"):
            q0.addTransition(q0, c, None, None)
        # Abre chaves: empilha '{'
        q0.addTransition(q0, '{', None, '{')
        # Fecha chaves: desempilha '{'
        q0.addTransition(q0, '}', '{', None)

        pda = PDA(q0)
        b = pda.run(w)
        Util.checkout(b, w)
        print()

    @staticmethod
    def multiplo3(w: str):
        print("Exemplo MÚLTIPLO DE 3:")
        print("{ w in Σ^* | w é um número binário múltiplo de 3}")
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
        print()

    @staticmethod
    def reverso(w: str):
        print("Exemplo REVERSO ww^R:")
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
        Util.checkout(b, w)
        print()
