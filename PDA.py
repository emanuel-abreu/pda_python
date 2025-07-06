from State import State
import copy


class PDA:
    def __init__(self, q: State):
        self._q0 = q            # estado inicial
        self.log = False
        self._pilha_inicio = ['#']  # símbolo de fundo de pilha

    def run(self, w: str) -> bool:
        """
        Reconhece ou não a string w. Retorna True se existe um caminho de transição
        que consome toda w e chega a um estado final com pilha limpa (ou só '#').
        """
        # Cada configuração é uma tripla (estado_atual, posição_em_w, pilha_atual)
        # Começamos com configuracao inicial
        inicial = (self._q0, 0, list(self._pilha_inicio))
        # vamos fazer busca em largura / backtracking simples
        fila = [inicial]
        visitados = set()

        while fila:
            estado, i, pilha = fila.pop(0)
            key = (estado.getName(), i, tuple(pilha))
            if key in visitados:
                continue
            visitados.add(key)

            # condição de aceitação:
            if i == len(w) and estado.isFinal():
                # opcionalmente exigir pilha só com '#'
                if pilha == ['#']:
                    return True

            # símbolo atual de entrada (ou None para epsilon)
            c = w[i] if i < len(w) else None
            topo = pilha[-1] if pilha else None

            # iterar por transições que leem c (incluindo c=None) e com pop=topo
            # e também transições epsilon (c=None) com pop=topo
            for t in estado._transitions:
                e = t.getEdge()
                # verificar leitura: e.c pode ser caractere ou None para epsilon
                if e.getC() != c and e.getC() is not None:
                    continue
                # verificar pop de pilha: e.pop pode ser simbolo ou None (não consome)
                if e.getPop() is not None and e.getPop() != topo:
                    continue

                # monta nova configuração
                novo_estado = t.getState()
                novo_i = i + (1 if e.getC() is not None else 0)
                nova_pilha = pilha.copy()

                # opera pop
                if e.getPop() is not None:
                    nova_pilha.pop()
                # opera push (sequência de símbolos, empilhados inversamente)
                if e.getPush() is not None:
                    for s in reversed(e.getPush()):
                        nova_pilha.append(s)

                fila.append((novo_estado, novo_i, nova_pilha))

        return False
