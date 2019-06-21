from sieve import primes_up_to_n_using_sieve
import My_functions, sys

sys.path.insert(0, './helper_functions')

def q2():
    return sum(n for n in My_functions.fibs_up_to(4000000) if n % 2 == 0)


'''def prime_factor(n):
  i = 2
  while i*i <= n:
     while (n % i) == 0:
         n = n // i
     i += 1
  return n'''


def q4():
    palind = None
    for n in xrange(100, 1000):
        for m in xrange(100, 1000):
            prod = n * m
            if str(prod) == str(prod)[::-1]:
                if palind is None or prod > palind:
                    palind = prod
    return palind


def q5():
    from functools import reduce
    return reduce(My_functions.lcm, range(1, 20 + 1))


def q6(n):
    q = 0
    y = 0
    for i in range(1, n + 1):
        q = q + i ** 2
        y = y + i
    return y ** 2 - q


def q7():
    primes = primes_up_to_n_using_sieve(1000000)
    return primes[10000]


def q8(s, x):
    largestProduct = 0

    for i in range(0, len(s) - x):
        product = 1

        for j in range(i, i + x):
            product *= int(s[j])

        if product > largestProduct:
            largestProduct = product

    print largestProduct


def q9():
    for a in range(1, 1000):
        for b in range(a, 1000 - a * 2):
            c = 1000 - a - b
            if a ** 2 + b ** 2 == c ** 2:
                print(a, b, c)
                print("Product: {}".format(a * b * c))


def sum_of_primes():
    prime_list = primes_up_to_n_using_sieve(2000000)
    result = 0
    for i in prime_list:
        result += i
    return result
