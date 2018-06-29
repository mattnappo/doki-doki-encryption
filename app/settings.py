def init():
    global globals
    globals = []
def test():
    global globals
    globals.append("GLOBALS!!")
def destroy():
    global globals
    globals = None
