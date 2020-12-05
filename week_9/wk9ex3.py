# door: Sander Kroeze & Chris wibbelink

def next(a):
    a = str(a)
    k = 1
    last = a[0]
    result = ''
    for i in range(1,len(a)):
        if last == a[i]:k +=1
        else:
            result = result + str(k) + last
            k = 1
        last = a[i]
    result = result + str(k) + last
    return int(result)

# tests voor de functie next(a)
assert next(21) == 1211
assert next(2222) == 42
assert next(312211) == 13112221

def read_it(n):
    num = 1
    for i in range(n):
        print(num)
        num = next(num)