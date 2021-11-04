class Cinput:
    def getconstrainedint(lowerbound,upperbound,str):
        x=int(input(str))
        while not (lowerbound<x< upperbound):
            x=int(input(str))
        return x

    def getpostive(str):
        x=int(input(str))
        while  x<0:
            x=int(input(str))
        return x

    def getstr():
        try:
            x=input(str)
        except:
            return Cinput.getstr()
        return x

    def getint():
        try:
            x=int(input(str))
        except:
            return Cinput.getint()
        return x
