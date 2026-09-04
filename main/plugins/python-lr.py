# Python LangRead
import ast
from gckcode import utils

OPP = 1
OPS = 2

def ctprg(scd:str) -> list[tuple[int,int,int,int]]:
    livingtree = ast.parse(scd)
    prgtk = []
    for idknode in livingtree.body:
        # :P
        if isinstance(idknode,ast.Assign):
            if isinstance(idknode.value,ast.Constant) and isinstance(whynode.value.value,int):
                prgtk.append((OPS,1,node.value.value,0))
        # XD
        elif isinstance(whynode,ast.Expr) and isinstance(whynode.value,ast.Call):
            if getattr(whynode.value.func,'id','') == 'print':
                for arg in whynode.value.args:
                    if isinstance(arg,ast.Constant) and isinstance(arg.value,int):
                        prgtk.append((OPP,0,arg.value,0))
    return prgtk

def plugininit():
    pass
