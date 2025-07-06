import itertools
from State import State
class PDA: #PDA = (Q, Σ, δ, q0, F)
    def __init__(self, q: State):
        self._q = q
        self._pilha = []
        self.log = False
        self._pilha.append('#')

    def run(self, w: str):
        # Insira seu código para manipular a pilha (e "w") aqui!
        return False
