#
# wk10ex1.py
#
# naam: Sander Kroeze & Chris Wibbelink
#

# Eerst de klassedefinitie
# Hieronder definiëren we een aantal handige objecten van het type Date
#  +++ bewaar die en/of voeg je eigen toe! +++


class Date(object):
    """A user-defined data structure that
       stores and manipulates dates.
    """

    # de constructor heet altijd __init__ !
    def __init__(self, day, month, year):
        """Construct a Date with the given day, month, and year."""
        self.day = day
        self.month = month
        self.year = year

    # de "afdruk"-functie heet altijd __repr__ !
    def __repr__(self):
        """This method returns a string representation for the
           object of type Date that calls it (named self).

           ** Note that this function _can_ be called explicitly, but
              it more often is used implicitly via the print statement
              or simply by expressing self's value.
        """
        s = "{:02d}-{:02d}-{:04d}".format(self.day, self.month, self.year)
        return s

    # Hier is een voorbeeld van een "methode" van de klasse Date:
    def is_leap_year(self):
        """Returns True if the calling object is
           in a leap year; False otherwise."""
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False
    
    def copy(self):
        """
            Returns a new object with the same day, month, year
            as the calling object (self).
        """
        dnew = Date(self.day, self.month, self.year)
        return dnew

    def equals(self, d2):
        """Decides if self and d2 represent the same calendar date,
        whether or not they are the in the same place in memory.
        """
        if self.year == d2.year and self.month == d2.month and self.day == d2.day:
            return True
        else:
            return False
    
    def __eq__(self, d2):
        """Overrides the == operator so that it declares two of the same dates
            in history as ==.  This way, we don't need to use the awkward
            d.equals(d2) syntax...
        """
        if self.year == d2.year and self.month == d2.month and self.day == d2.day:
            return True
        else:
            return False

    def __lt__(self, d2):
        """"
            Met deze functie kun je heel makkelijk kijken of de daten voor de orginele datum komt.
            Gebruik in de command line: d < d2
        """
        if d2.year != self.year:
            return self.year < d2.year

        if d2.month != self.month:
            return self.month < d2.month
    def __gt__(self, d2):
        """
            Met deze functie kun je heel makkelijk kijken of de datum na de orginele datum komt.
            Gebruik in de command line: d > d2
        """
        if d2.year != self.year:
            return self.year > d2.year

        if d2.month != self.month:
            return self.month > d2.month

        return self.day > d2.day

    def __iadd__(self, n):
        """
            Met deze functie kun je heel makkelijk dagen bij een datum optellen.
            Gebruik in de command line: d += 1
        """
        self.day += n
        # print(self) # print de uitkomst gelijk, kan ook uit staan

    def __isub__(self, n):
        """
            Met deze functie kun je heel makkelijk dagen van een datum aftrekken.
            Gebruik in de command line: d -= 1
        """
        self.day -= n
        # print(self) # print de uitkomst gelijk, kan ook uit staan

    def is_before (self, d2):
        """"
            Deze functie kijkt of d2 voor de orginele datum is.
        """
        if d2.year != self.year:
            return self.year < d2.year

        if d2.month != self.month:
            return self.month < d2.month

        return self.day < d2.day

    def is_after (self, d2):
        """"
            Deze funcite kijkt of d2 na de orginele datum is.
        """
        if d2.year != self.year:
            return self.year > d2.year

        if d2.month != self.month:
            return self.month > d2.month

        return self.day > d2.day
    
    def tomorrow(self):
        """"
            Geeft de datum van een dag later weer van de orginele datum.
        """
        fdays = 28 + self.is_leap_year()
        DIM = [0,31,fdays,31,30,31,30,31,31,30,31,30,31]
        self.day += 1
        if self.day > DIM[self.month]:
            self.day = 1
            self.month += 1
            if self.month == 13:
                self.year += 1
                self.month = 1
    
    def yesterday(self):
        """
            Geeft de datum van gister weer van de orginele datum.
        """
        fdays = 28 + self.is_leap_year()
        DIM = [0,31,fdays,31,30,31,30,31,31,30,31,30,31]
        self.day -= 1
        if self.day < 1:
            self.month -= 1
            if self.month < 1:
                self.year -= 1
                self.month = 12
            self.day = DIM[self.month]
    
    def add_n_days(self, n):
        """
            Voegt n aantal dagen toe aan de orinele datum.
        """
        for i in range(n):
            self.tomorrow()
            # print(self) #gebruik deze regel om de dagen vooruit te printen
    
    def sub_n_days(self, n):
        """
            Haalt n aantal dagen van de orginele datum af.
        """
        for i in range(n):
            self.yesterday()
    
    def diff (self, d):
        """
            Geeft het verschil in dagen weer tussen twee datums.
        """
        cnt = 0
        d1 = self.copy()
        d2 = d.copy()
        while d1.is_before(d2):
            d1.tomorrow()
            cnt -= 1
        while d1.is_after(d2):
            d1.yesterday()
            cnt += 1
        return cnt

    def dow (self):
        """
            Geeft de dag weer van een bepaalde datum.
        """
        weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return weekday[((3 + self.diff(Date(11, 12, 2014)))%7+7)%7] 


#
# vergeet niet je code voor de klasse Date HIERBOVEN toe te voegen; in de klassedefinitie
#


#
# een aantal datums om mee te werken...
#
# Het handige van ze hier plaatsen is dat ze elke keer dat de software uitgevoerd
#   wordt ze opnieuw gedefinieerd worden (en dat is nodig om te testen!)
#

d = Date(2, 12, 2020)    # Vandaag?
d2 = Date(21, 12, 2020)   # Kerstvakantie
ny = Date(1, 1, 2021)   # Nieuwjaar
nd = Date(1, 1, 2030)   # Nieuw decennium
nc = Date(1, 1, 2100)   # Nieuwe eeuw
graduation = Date(12, 7, 2024)   # Pas dit zelf aan!
vacation = Date(19, 7, 2021)     # Dit ook ~ zomervakantie!
sm1 = Date(28, 10, 1929)    # Krach aandelenbeurs
sm2 = Date(19, 10, 1987)    # Nog een beurskrach: Maandagen in okt. zijn gevaarlijk...
