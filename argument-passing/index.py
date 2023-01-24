import sys

argument = sys.argv

def sum(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

if argument[1] == "sum":
    resp = sum(float(argument[2]), float(argument[3]))
elif argument[1] == "sub":
    resp = sub(float(argument[2]), float(argument[3]))

print(resp)