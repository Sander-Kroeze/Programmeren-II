# wk8ex3.py
# Opgave Pi met pijltjes: lussen
#
# Naam: Sander Kroeze
#
import random
import math

def throw_dart():
    """
        Deze functie bepaalt of de dartpijl in het vierkant is gekomen.
        True als hij er binnen is, False als hij er buiten is.
    """
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)

    if x**2 + y**2 <= 1:
        return True
    return False

def for_pi(n):
    """
        Deze functie geeft als output wat hij gegooit heeft, n is hoeveel keer je mag gooien.
    """
    if n < 0:
        return 0.0
    hits = 0.0

    for i in range(n):
        hits += 1.0 if throw_dart() else 0.0
        print( hits, " raak van ", i + 1, " worpen dus pi is ", hits / (i + 1) * 4)
    return hits / n * 4

def while_pi(error):
    if error < 0:
        return 0.0

    numthrows = 0.0
    numhits = 0.0

    while numthrows == 0 or abs(numhits/numthrows*4 - math.pi) > error:
        numhits += 1.0 if throw_dart() else 0.0
        numthrows += 1
        print(numhits," raak van ", numthrows, " worpen dus pi is ", numhits/ (numthrows)* 4)

    return numthrows
    