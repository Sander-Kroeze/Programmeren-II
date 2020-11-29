#
# Voorbeeldprogramma voor een lus voor gebruikersinteractie
#  (een variant van de versie van het college)
#
import math

def menu():
    """A function that simply prints the menu"""
    print()
    print("(0) Voer een nieuwe lijst in")
    print("(1) Druk de huidige lijst af")
    print("(2) Bepaal de gemiddelde prijs")
    print("(3) Bepaal de standaardafwijking")
    print("(4) Bepaal het minimum en de bijbehorende dag")
    print("(5) Bepaal het maximum en de bijbehorende dag")
    print("(6) Je TR-investeringsplan")
    print("(9) Stoppen! (einde)")
    print()


def predict(L):
    """Predict ignores its argument and returns
       what the next element should have been.
    """
    return 42


def find_min(L):
    """find min uses a loop to return the minimum of L.
       Argument L: a nonempty list of numbers.
       Return value: the smallest value in L.
    """
    result = L[0]
    for x in L:
        if x < result:
            result = x
    return result


def find_min_loc(L):
    """find min loc uses a loop to return the minimum of L
            and the location (index or day) of that minimum.
        Argument L: a nonempty list of numbers.
        Results:  the smallest value in L, its location (index)
    """
    min_val = L[0]
    min_loc = 0

    for i in list(range(len(L))):
        if L[i] < min_val:  # een kleinere gevonden!
            min_val = L[i]
            min_loc = i

    return min_val, min_loc


def main():
    """The main user-interaction loop"""
    secret_value = 4.2

    L = [30, 10, 20]  # een beginlijst

    while True:     # de lus voor gebruikersinteractie
        print("\n\nDe lijst is", L)
        menu()
        choice = input("Maak een keuze: ")

        #
        # De invoer van de gebruiker "opschonen en controleren"
        # 
        try:
            choice = int(choice)   # omzetten naar een int!
        except:
            print("Ik begreep de invoer niet! Verder gaan...")
            continue

        # de gekozen menu-optie uitvoeren
        #
        if choice == 9:    # We willen stoppen
            break          # De hele while-lus afbreken

        elif choice == 0:  # Geeft de gebruiker de mogelijkheid om een nieuwe lijst in te voeren
            numString = input("Enter a new list: ")
            L = makeList(numString)

        elif choice == 1: # De lijst wordt weergegeven
            printList(L) # De functie printList wordt aangeroepen

        elif choice == 2: # Geeft de gemiddelde prijs weer
            print("De gemiddelde prijs is: ", averagePrice(L)) # Roept de funcite avaragePrice aan met de list: L

        elif choice == 3: # Geeft de standaardafwijking weer
            print("De standaardafwijking is: ", standardDev(L)) # Roept de functie stanardDev aan

        elif choice == 4: # Geeft de minimum aan op een bepaalde dag
            ans = minDay(L) # Roept de functie minDay aan
            print("De minimum is ", ans[0], " op dag ", ans[1])

        elif choice == 5: # Geeft het maximum aan op een bepaalde dag
            ans = maxDay(L) # Roept de functie maxDay aan
            print("De maximum", ans[0], " op dag ", ans[1])

        elif choice == 6: # Geeft het hele TTPlan weer
            ans = TTPlan(L) # Roept de functie TTPlan aan
            print("Je TRI investeringsstrategie is om")
            print("")
            print(" Te kopen op dag ", ans[0], " voor prijs ", L[ans[0]])
            print(" Te verkopen op dag ", ans[1], " voor prijs ", L[ans[1]])
            print(" Dit geeft een totale winst van ", ans[2])

        else:
            print(choice, " ?      Dat staat niet op het menu!")

    print("")
    print("Tot gisteren!")

def makeList(numString):
    """
        Functie die een lijst maakt
    """
    numString = numString.replace('[', '')
    numString = numString.replace(']', '')
    numList = numString.split(',')

    L = []
    for x in numList:
        L.append(float(x.strip()))

    return L

def printList (L):
    """
        Functie om de hele lijst te printen
    """
    print("")
    print( "Dag  Prijs")
    print( "---  -----")
    for x in range(len(L)):
        print ("%3d %5.2f" %(x, L[x]))
    print("")

def averagePrice (L):
    """
        Functie om het gemiddelde te berekenen
    """
    s = 0.0
    for x in L:
        s += x

    return s / len(L)

def minDay (L):
    """
        Functie om het minimum te berekenen
    """
    minV = 1 << 30
    index = 0
    for x in range(len(L)):
        if L[x] < minV:
            minV = L[x]
            index = x

    return [minV, index]

def standardDev (L):
    ave = averagePrice(L)
    s = 0.0
    for x in L:
        s += (x - ave)**2

    return math.sqrt(s / len(L))

def maxDay (L):
    """
        Functie om de max te berekenen
    """
    maxV = -(1 << 30)
    index = 0
    for x in range(len(L)):
        if L[x] > maxV:
            maxV = L[x]
            index = x

    return [maxV, index]

def TTPlan (L):
    """
        Functie om het plan weer te geven
    """
    maxV = -(1 << 30)
    ans = []
    for x in range(len(L)):
        for y in range(1, len(L)):
            if L[y] - L[x] > maxV:
                maxV = L[y] - L[x]
                ans = [x, y, maxV]

    return ans
