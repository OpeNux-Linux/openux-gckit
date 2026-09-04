import os
import sys
import importlib.util
from datetime import datetime

def log(txt,status):
    if status.lower() == "log":
        status = "LOG"
    elif status.lower() == "warn":
        status = "WARN"
    elif status.lower() == "err":
        status = "ERR"
    elif status.lower() == "dep":
        status = "DEP"

    print(f"[{status}]: {txt}")

def loadc(dir,sm=False):
    if not os.path.exists(dir):
        if not sm:
            cpath = os.path.abspath(dir)
            mf = os.path.basename(cpath)
            log(f"{mf} not Found!",'warn')
        return
    cpath = os.path.abspath(dir)
    mf = os.path.basename(cpath)
    for fn in os.listdir(dir):
        if fn.endswith(".py") and not fn.startswith("__"):
            mn = os.path.splitext(fn)[0]
            fp = os.path.join(dir,fn)
            sc = importlib.util.spec_from_file_location(mn,fp)
            m = importlib.util.module_from_spec(sc)
            sc.loader.exec_module(m)
            if mf == "plugins":
                if hasattr(m,"plugininit"):
                    m.plugininit()
                    if not sm: log(f"Plugin {mn} loaded..",'log')
                elif hasattr(m,"init"):
                    m.init()
                    if not sm: log(f"Plugin {mn} loaded..",'log')
            elif mf == "gckcode":
                if hasattr(m,"init"):
                    m.init()
                    if not sm: log(f"Code {mn} loaded..",'log')
