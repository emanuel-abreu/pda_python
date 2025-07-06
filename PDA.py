from State import State
import copy


class PDA:
    def __init__(self, q: State):
        self._q0 = q            # estado inicial
        self.log = False
        self._pilha_inicio = ['#']  # símbolo de fundo de pilha

    def run(self, w: str) -> bool:
        """
        Reconhece ou não a string w.
        Retorna True se existe um caminho de transição
        que consome toda w e chega a um estado final
        com pilha só contendo o símbolo de fundo.
        Busca em largura/backtracking simples.
        """
        inicial = (self._q0, 0, list(self._pilha_inicio))
        fila = [inicial]
        visitados = set()

        while fila:
            estado, i, pilha = fila.pop(0)
            key = (estado.getName(), i, tuple(pilha))
            if key in visitados:
                continue
            visitados.add(key)

            # Aceitação: consumiu toda w, está em estado final e pilha limpa
            if i == len(w) and estado.isFinal() and pilha == ['#']:
                return True

            c = w[i] if i < len(w) else None
            topo = pilha[-1] if pilha else None

            # Explora transições possíveis
            for t in estado._transitions:
                e = t.getEdge()
                # Verifica leitura (terminal ou epsilon)
                if e.getC() is not None and e.getC() != c:
                    continue
                # Verifica pop da pilha
                if e.getPop() is not None and e.getPop() != topo:
                    continue

                novo_estado = t.getState()
                novo_i = i + (1 if e.getC() is not None else 0)
                nova_pilha = pilha.copy()
                # Pop
                if e.getPop() is not None:
                    nova_pilha.pop()
                # Push (inverte ao empilhar)
                if e.getPush() is not None:
                    for s in reversed(e.getPush()):
                        nova_pilha.append(s)
                # Adiciona à fila de exploração
                fila.append((novo_estado, novo_i, nova_pilha))

        return False  # não reconheceu
