#
# wk7ex1c.py - uniekheid controleren  (voor de random-number generator in Hmmm)
#    De functie test(s) staat hier al in (onderaan).
#
# Naam: Sander Kroeze & Chris Wibbelink
#
# Je plakt je 100 getallen in deze triple-quoted string:
NUMBERS = """
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
"""




def unique(lst):
    """
        This should be your uniqueness-tester, written for week 7
        Usually, it uses the recursive pattern:

        if ...      # handle base case
        elif ...    # check whether L[0] re-appears
        else ...    # otherwise...
    """

    if len(lst) == 1: 
        return True
    elif lst[0] in lst[1:]: 
            return False
    else:
        return unique(lst[1:])


def test(s):
    """test accepts a triple-quoted string, s,
       containing one number per line. Then, test
       returns True if those numbers are all unique
       (or if s is empty); otherwise it returns False
    """
    s = s.strip()                 # haal alle spaties aan het begin en eind van s weg
    list_of_strings = s.split()   # splits s op elke spatie en nieuwe regel
    # print("list_of_strings is", list_of_string)
    list_of_integers = [int(s) for s in list_of_strings]  # converteer ze allemaal naar ints
    # print("list_of_integers is", list_of_integers)
    return unique(list_of_integers)


# Uitproberen!
result = test(NUMBERS)
print("\nTest op uniekheid:  Het resultaat is", result)
