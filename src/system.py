import math

from interpreter import *
from syntax import Syntax, Variable

class System:
    LineNumber, CurrentLine, CurrentCode = 0, None, []
    IfEnd = None

    Variables = {}
    Labels = {}

    BuiltIn = {
        f"%{k}": v
        for (k, v) in {
            "pi": Variable(math.pi, "float"),
            "phi": Variable((1+5**0.5)/2, "float"),
            "tau": Variable(math.tau, "float"),
            "e": Variable(math.e, "float")
        }.items()
    }

    @staticmethod
    def Run(code):
        System.CurrentCode = code
        while System.LineNumber<len(System.CurrentCode):
            System.CurrentLine = System.CurrentCode[System.LineNumber]
            System.LineNumber+=1
            if System.IfEnd!=None and System.LineNumber==System.IfEnd:
                System.Labels = {k:System.Labels[k] for k in System.Labels if System.Labels[k].Global}
                System.IfEnd = None
            if not len(System.CurrentLine.strip()) or System.CurrentLine.strip()[0]==Syntax.Comment: 
                continue
            Interpreter.Interprete(System.CurrentLine)