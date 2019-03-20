import math, sys
sys.path.insert(0, './helper_functions')

def q41():
    from My_functions import is_pandigital_from_digits
    from sieve import primes_up_to_n_using_sieve
    n = primes_up_to_n_using_sieve(8000000)
    ns = []
    for i in n:
        if is_pandigital_from_digits(i):
            ns.append(i)

    return max(ns)


def q42():
    from My_functions import gen_tri_number
    f = open("triangle_words.txt", "r")
    words = sorted(f.read().replace('"', '').split(","), key=str)

    ns = gen_tri_number(10000)

    value = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6,
             "g": 7, "h": 8, "i": 9, "j": 10, "k": 11,
             "l": 12, "m": 13, "n": 14, "o": 15, "p": 16,
             "q": 17, "r": 18, "s": 19, "t": 20, "u": 21,
             "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}

    count = 0
    for word in words:
        sums = 0
        for letter in word:
            sums += value[letter.lower()]
        if sums in ns:
            count += 1

    return count


def q43():
    from itertools import permutations
    def div(x,start,end,d):
        n = int(x[start:end+1])
        return (n % d == 0)

    def satisfies(x):
        cond = (x[0] != '0') and (int(x[3]) % 2 == 0) and (int(x[5]) % 5 == 0)
        cond = cond and div(x,2,4,3) and div(x,4,6,7) and div(x,5,7,11)
        cond = cond and div(x,6,8,13) and div(x,7,9,17)
        return cond

    def string_permutations(xs):
        return ("".join(x) for x in permutations(xs))

    return sum(int(s) for s in string_permutations("0123456789")
                      if satisfies(s))

    # sums = 0
    # for x in permutations("0123456789"):
    #     x = "".join(list(x))
    #
    #     if x[0] == "0":
    #         pass
    #     elif int(x[3]) % 2 != 0:
    #         pass
    #     elif int(x[5]) % 5 != 0:
    #         pass
    #     elif div(x,2,4,3):
    #         pass
    #     elif div(x,4,6,7):
    #         pass
    #     elif div(x,5,7,11):
    #         pass
    #     elif div(x,6,8,13):
    #         pass
    #     elif div(x,7,9,17):
    #         pass
    #     else:
    #         sums += int(x)
    #         print "".join(x)
    #
    # return sums


def q44():
    def isPentagonal (x):
        penTest = (math.sqrt(1 + 24 * x) + 1.0) / 6.0
        return (penTest % 1 == 0)

    result = 0
    notFound = True
    i = 1

    while notFound:
        for j in xrange(1, i):
            a = i*(3*i-1)/2
            b = j*(3*j-1)/2
            if isPentagonal(a+b) and isPentagonal(a-b):
                result = a-b
                notFound = False
                break
        i += 1

    return result


def q45():
    from My_functions import isTriangle, isPentagonal, isHexagonal

    i = 286
    while True:
        Triangle = (i * (i + 1)) / 2
        if isPentagonal(Triangle) and isHexagonal(Triangle):
            return Triangle
        i += 1


def q46():
    from My_functions import isPrime
    number = 3
    primes = [2]

    while True:
        if isPrime(number):
            primes.append(number)
        else:
            for i in primes:
                if math.sqrt(((number-i)/2)) == int(math.sqrt(((number-i)/2))):
                    break
            else:
                return number

    number += 2


def q47():
    from My_functions import npf
    j = 2 * 3 * 5 * 7

    while True:
        if npf(j) == 4:
            j += 1
            if npf(j) == 4:
                j += 1
                if npf(j) == 4:
                    j += 1
                    if npf(j) == 4:
                        return j - 3
                        break
        j += 1


def q48():
    i = 10405071317
    for j in xrange(11, 1001):
        i += j ** j
    return str(i)[-10:]


def q49():
    from itertools import permutations
    from sieve import primes_up_to_n_using_sieve

    def create(b):
        for i in xrange(len(b)):
            for j in xrange(i + 1, len(b)):
                difference = b[j] - b[i]
                if b[j] + difference in b:
                    return str(b[i]) + str(b[j]) + str(b[j] + difference)
        return False

    primes = primes_up_to_n_using_sieve(10000)
    primes = [x for x in primes if x > 1487]

    for i in primes:
        p = permutations(str(i))
        a = [int(''.join(x)) for x in p]
        a = list(set([x for x in a if x in primes]))
        a.sort()
        if len(a) >= 3:
            if create(a):
                return create(a)


def q50():
    from sieve import primes_up_to_n_using_sieve
    from My_functions import is_prime

    prime_sieve = primes_up_to_n_using_sieve(1000000)
    list_of_primes = []
    number = 0

    while True:
        for i in prime_sieve[3:]:
            number += i
            if is_prime(number):
                list_of_primes.append(number)
            if number > 1000000:
                break
        break

    return list_of_primes[-1]
