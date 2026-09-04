# main.py just
from gckcode import utils,mcode

cdir = "./gckcode"
pldir = "./plugins"
sm = False

if __name__ == "__main__":
    utils.loadc(cdir,sm)
    mcode.load()
    utils.loadc(pldir,sm)
