#SONARA GFormat
import os
import struct
from gckcode import utils
SNHeader = b"GCK1"
INSize = 12
# Note: just note, SONARA is file for .g files
def cgst(prgtk: list[tuple[int,int,int,int]]) -> bytes:
    dta = bytearray(SNHeader)
    for opc,trg,ar1,ar2 in prgtk:
        #Why NOT
        chnk = struct.pack("<HHII",opc,trg,ar1,ar2)
        dta.extend(chnk)
    return bytes(dta)

def pgst(dta: bytes) -> list[tuple[int,int,int,int]]:
    #YEAH PARSING
    if not dta.startswith(SNHeader):
        utils.log("BAD, VERY BAD!",'err')
        return []
    prgtk = []
    offst = len(SNHeader)
    while offst + INSize <= len(dta):
        chnk = dta[offst:offst+INSize]
        opc,trg,ar1,ar2 = struct.unpack("<HHII",chnk)
        prgtk.append((opc,trg,ar1,ar2))
        offst += INSize
    return prgtk
    
def writejeff(fpath: str, prgtk: list[tuple[int,int,int,int]]) -> bool:
    #Hi JEFF
    try:
        bindta = cgst(prgtk)
        with open(fpath,"wb") as f:
            f.write(bindta)
        utils.log(f"Writing the PG to {fpath}...",'log')
        return True
    except Exception as exc:
        utils.log(f"FAIL WRITE to {fpath}: {exc}",'err')
        return False

def readjeff(fpath: str) -> list[tuple[int,int,int,int]]:
    #Bye bye JEFF!
    if not os.path.exists(fpath):
        utils.log(f"JEFF not found the File: {fpath}",'err')
        return []
    try:
        with open(fpath,"rb") as fileforjeff:
            dta = fileforjeff.read()
        #TOKENS
        tkns =  pgst(dta)
        utils.log(f"Loaded {len(tkns)} PG insts fm {fpath}",'log')
        return tkns
    except Exception as excp:
        utils.log(f"JEFF Failed to Read GFF {fpath}: {excp}",'err')
        return  []

def init():
    pass
