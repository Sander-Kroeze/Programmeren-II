#
# wk7ex5.py - Aan de slag met lussen!
#
# Naam: Sander Kroeze & Chris Wibbelink
#

import random

def fac(n):
    """Loop-based factorial function
       Argument: a nonnegative integer, n
       Return value: the factorial of n
    """
    result = 1                 # beginwaarde; lijkt op een basisgeval
    for x in range(1, n + 1):  # herhaal van 1 tot en met n
        result = result * x    # pas het resultaat aan door keer x te doen
    return result              # merk op dat dit NA de lus is!

#
# Tests voor de lus-versie van de faculteit
#
assert fac(0) == 1
assert fac(5) == 120


def power (b, p):
    """"
        deze functie is een lus-versie van machtsverheffen
    """
    ans = 1
    for i in range(p):
        ans *= b
    return ans

assert power(2, 5) == 32
assert power(42, 0) == 1

# test!
# print("power(2, 5): is 32 ==", power(2, 5))
# print("power(5, 2): is 25 ==", power(5, 2))
# print("power(42, 0): is 1 ==", power(42, 0))
# print("power(0, 42): is 0 ==", power(0, 42))
# print("power(0, 0): is 1 ==", power(0, 0))

def summed(L):
    """
      Een loop-functie die een lijst met nummers terug geeft
    """
    result = 0
    for e in L:
        result = result + e 
    return result

# tests!
assert summed([4, 5, 6]) == 15
assert summed(range(3, 10)) == 42

def summed_odds(L):
    ans = 0
    for i in range(len(L)):
        ans += L[i] if L[i] % 2 == 1 else 0
    return ans

# tests!
assert summed_odds([4, 5, 6]) == 5
assert summed_odds(range(3, 10)) == 24

def unique(L):
  """Returns whether all elements in L are unique.
     Argument: L, a list of any elements.
     Return value: True, if all elements in L are unique,
                or False, if there is any repeated element
  """
  if len(L) == 0:
    return True
  elif L[0] in L[1:]:
    return False
  else:
    return unique(L[1:])  # in deze functie mag je WEL recursie gebruiken!

def until_a_repeat(high):
    """
        Deze functie gaat door tot dat de waardes in L wel uniek zijn
    """
    L = []
    cnt = 0
    while unique(L):
        L.append(random.choice(range(0, high)))
        cnt += 1
    return cnt


