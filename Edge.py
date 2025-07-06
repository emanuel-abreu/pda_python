from Util import Util

class Edge:
    def __init__(self, c: str, pop: str, push: str):
        self.c = c
        self.pop = pop
        self.push = push

    def getC(self): return self.c
    def setC(self, c: str): self.c = c
    def getPop(self): return self.pop
    def setPop(self, _pop: str): self.pop = _pop
    def getPush(self): return self.push
    def setPush(self, _push: str): self.push = _push

    @staticmethod
    def instance(c: str, pop: str, push: str):
        return Edge(c, pop, push)
   
    def equals(self, e):
        if isinstance(e, Edge):
            return Util.testAB(self.c, e.getC()) and Util.testAB(self.push, e.getPush()) and Util.testAB(self.pop, e.getPop())
        return False
    
    def hashCode(self):
        hc = self.c.__hash__ if self.c != None else 0
        hc = 47 * hc + (self.pop.__hash__ if self.pop != None else 0)
        hc = 47 * hc + (self.push.__hash__ if self.push != None else 0)
        return hc
    
    def __repr__(self):
        return f'edge[{self.c}, {self.pop}, {self.push}]'




