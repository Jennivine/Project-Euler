import math, sys
sys.path.insert(0, './helper_functions')

def q21():
    amicable_pairs = []

    def d(number):
        sums = 0
        for i in xrange(1, int(round(math.sqrt(number))) + 1):
            if number % i == 0:
                sums += i + (number / i)
        return sums - number

    for i in range(2, 10000):
        da = d(i)
        db = d(da)
        if db == i:
            if (da, db) not in amicable_pairs and (db, da) not in amicable_pairs and da != db:
                amicable_pairs.append((da, db))

    result = [i for sub in amicable_pairs for i in sub]
    return sum(result)


def q22():
    f = open("names.txt", "r")
    names = sorted(f.read().replace('"', '').split(","), key=str)

    value = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6,
             "g": 7, "h": 8, "i": 9, "j": 10, "k": 11,
             "l": 12, "m": 13, "n": 14, "o": 15, "p": 16,
             "q": 17, "r": 18, "s": 19, "t": 20, "u": 21,
             "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}

    total = 0

    for index, val in enumerate(names):
        result = 0
        for letter in val:
            result += value[letter.lower()]
        total += result * (index + 1)

    return total


def q23():
    from My_functions import abundant_numbers_from

    MAX = 28123
    result = [False] * (MAX + 1)
    abundant_numbers = abundant_numbers_from(12, 28124)
    for i in range(len(abundant_numbers)):
        for j in range(i, len(abundant_numbers)):
            s = abundant_numbers[i] + abundant_numbers[j]
            if s > MAX:
                break
            result[s] = True

    return sum(i for i, x in enumerate(result) if not x)


def q24():
    from My_functions import perms

    return perms("0123456789", 999999)


def q25():
    from My_functions import fibs_length_index

    return fibs_length_index(1000)


def q26():
    from My_functions import recurring

    return recurring(1000)


def q27():
    def longestPrimeQuadratic(alim, blim):

        def isPrime(k):  # checks if a number is prime
            if k % 2 == 0 or k < 2:
                return False
            elif k == 2:
                return True
            else:
                for x in range(3, int(math.sqrt(k) + 1), 2):
                    if k % x == 0: return False
            return True

        longest = [0, 0, 0, 0]  # length, a, b, a*b

        for a in xrange((alim * -1) + 1, alim):
            for b in xrange(2, blim):
                if isPrime(b):
                    count = 0
                    n = 0
                    while isPrime((n ** 2) + (a * n) + b):
                        count += 1
                        n += 1
                    if count > longest[0]:
                        longest = [count, a, b, a * b]

        return longest

    return longestPrimeQuadratic(1000, 1000)[-1]


def q28(n):
    alist = [1]
    blist = [1]
    for i in xrange(1, n):
        alist.append((alist[-1] + 2 * i))

    for j in xrange(2, n, 2):
        blist.append((blist[-1] + 2 * j))
        blist.append((blist[-1] + 2 * j))

    ans = alist + blist
    return sum(ans) - 1


def q29():
    result = set()
    for a in xrange(2, 101):
        for b in xrange(2, 101):
            result.add(a ** b)
    return len(result)


def q30():
    numbers = []

    def is_equal_to_fifth_power(n):
        global numbers
        l = [int(d) for d in str(n)]
        ans = 0
        for i in l: ans += i ** 5
        if n == ans:
            numbers.append(n)

    # number of digits for the sum must have the same number of digits as a candidate
    # the largest the sum can be for a seven digits candidate (9999999) will be (9**5)*7
    # which is 413343, therefore no answer will be found in this range
    # after some time going through the thread, I can reduce upper limit from the original 999999 to this equation below:
    L = 9 ** 5 * (5 - 1)

    for i in xrange(10, L):
        is_equal_to_fifth_power(i)

    return sum(numbers)
