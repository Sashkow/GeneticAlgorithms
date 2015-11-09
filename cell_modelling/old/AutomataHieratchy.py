class Automata(object):
    def __init__(self, name=None, orig=None):
        if orig==None:
            self.nonCopyConstructor(name)
        else:
            self.copyConstructor(orig)

    def nonCopyConstructor(self,name):
        self.name=name
        rint "nonCopyConstructor of Automata"

    def copyConstructor(self,orig):
        self.name=orig.name
        print "copyConstructor of Automata"

    def commonMethod(self):
        print "commonMethod"



class AutomataStructure(Automata):
    def __init__(self,name=None,orig=None, structureList=None):
        super(AutomataStructure,self).__init__(name,orig)

    def nonCopyConstructor(self,name):
        self.structureList=name
        print "nonCopyConstructor of AutomataStructure"

    def copyConstructor(self,orig):
        self.name=orig.name
        print "copyConstructor of AutomataStructure"

def main():
    aut=Automata(name="a1")

    print type(aut), aut.name

    autStru=AutomataStructure(orig=aut)

    print type(autStru), autStru.name






if __name__ == '__main__':
    main()
