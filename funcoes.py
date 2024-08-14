import math
# FUNCOES LN

def ln1f(x):
    return x * math.log(x) - 1

def ln1df(x):
    return math.log(x) + 1

#FUNCOES EXP

def exp1f(x):
    return pow(x,4)-x-5

def exp1df(x):
    return 4*pow(x,3)-1


