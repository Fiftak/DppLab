from enum import Enum

class Status(Enum):
    Dziecko=1,
    Nastolatek=2,
    Dorosly=3

def printFileName():
    print("Status")