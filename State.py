from Util import Util
from Edge import Edge
from Transition import Transition

class State:
    def __init__(self, name: str):
        self.name = name
        self.is_final = False
        self._transitions = []

    def getName(self): return self.name
    def setFinal(self): self.is_final = True
    def isFinal(self): return self.is_final

    def addTransition(self, _state, c: str, pop: str, push: str):
        return self.addTransitions(_state, Edge.instance(c, pop, push))

    def addTransitions(self, _state, *edges):
        for edge in edges:
            transition = Transition.instance(_state, edge)
            if transition in self._transitions:
                continue
            self._transitions.append(transition)
        return self

    def transitions(self, ch: str, pop: str): # return Set<ITransition>
        r = set()
        for t in self._transitions:
            e = t.getEdge()
            if (e.getC()==ch and e.getPop()==pop):
                r.add(t)
        return r
      
    def equals(self, s):
        if isinstance(s, State):
            return s.getName()==self.getName()
        return False
    
    def hashCode(self):
        return abs(hash(self.getName()))
    
    def __repr__(self):
        return self.name
