from __future__ import division
from math import *
import __builtin__
from sieve import primes_up_to_n_using_sieve

def prod(iterable):
    import operator
    return reduce(operator.mul, iterable, 1)

#----------------------------------Primes-------------------------------------------
def is_prime(n):
    biggest = int(round(sqrt(n)))
    if n < 2:
        return False
    elif n == 2 or n == 3:
        return True
    else:
        for f in xrange(2,biggest+1):
            if n % f == 0:
                return False
        return True


def isPrime(n):
    if n % 2 == 0:
        return False
    else:
        for i in xrange(3, int(n**0.5+1),2):
            if n % i == 0:
                return False
        return True


'''Checks if number n is prime or not'''
def isprime(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    max = int(round(sqrt(n)))
    for f in xrange(2, max + 1):
        if n % f == 0:
            return False
    return True


'''returns the largest prime factor of a number n'''
def prime_factor(n, f=2):
    while True:
        if f > n:
            raise ValueError("f > n")
        elif f == n:
            return f
        elif n % f == 0:
            n = n / f
        else:
            f_next = 3 if f == 2 else f + 2
            f = f_next


'''Returns the number of prime factors for argument x'''
def npf(number):
    i = 2
    a = set()
    while i < number ** 0.5 or number == 1:
        if number % i == 0:
            number = number / i
            a.add(i)
            i -= 1
        i += 1
    return (len(a) + 1)


def primes(n):
    primes = [2]
    attempt = 3
    while len(primes) < n:
        if trial_division_indicates_prime(primes, attempt):
            primes.append(attempt)
        attempt += 2
    return primes[-1]


''' Easiests to see if an integer n, the integer to be factored,
    can be divided by each number in turn that is less than n'''
def trial_division_indicates_prime(primes, number):
    max = round(sqrt(number))
    for p in primes:
        if p > max:
            return True
        elif number % p == 0:
            return False
    return True


def sum_of_primes():
    prime_list = primes_up_to_n_using_sieve(2000000)
    result = 0
    for i in prime_list:
        result += i
    return result


def truncatable_possibilities(n):
    n = str(n)
    left,right = n, n
    left_pop = []
    right_pop = []
    for i in range(1,len(n)+1):
        left_pop.append(int(left))
        right_pop.append(int(right))
        left = left[1:]
        right = right[:len(right)-1]

    return list(set(list(left_pop+right_pop)))


def eight_prime_family(prime, rd):
    c=0
    for digit in '0123456789':
        n = int(str.replace(prime, rd, digit))
        if (n>100000 and is_prime(n)):
            c=c+1
    return c==8



#-----------------------------------Factorize---------------------------------------
''' Return the prime factorisation of n.
    e.g. factorise(24) -> [2,2,2,3] '''
def factorise(n):
    return go(n, 2, [])

def go(n, f, answer):
    if n == 1:
        return answer
    elif n % f == 0:
        return go(n / f, f, answer + [f])
    else:
        return go(n, f + 1, answer)


'''Find the greatest common divisor of two numbers a and b'''
from fractions import gcd
def lcm(a, b):
    return a * b // gcd(a, b)


'''Calculate all factors of n'''
'''     factors(28) -> [1,2,4,7,14,28]'''
def factors(n):
    fact = [1,n]
    check = 2
    rootn = sqrt(n)
    while check < rootn:
        if n%check== 0:
            fact.append(check)
            fact.append(n/check)
        check += 1
    if rootn == check:
        fact.append(check)
    fact.sort()
    return fact



#----------------------------------Sequences----------------------------------------
    # -------------------------Fibonacci and Tribonacci-----------------------------
def fibs_up_to(n):
    a, b = 1, 2
    while a < n:
        yield a
        a, b = b, a + b


'''Find the nth term of a Tribonacci sequence with a, b and c as its seeds
       e.g. tribonacci (10) -> 89857 with seeds 20,17,2017 '''
def tribonacci(n):
    a, b, c = 17, 20, 17
    i = 3
    while i < n:
        #    print a
        a, b, c = b, c, a + b + c
        i += 1
    return c


'''Find the smallest n digit of a Tribonacci sequence with a, b and c as its seeds
    e.g. trbonacci (100) -> 140 
    - the smallest three digit tribinacci with seeds 6,20,17 '''
def smallest_tribs(n):
    a, b, c = 6, 20, 17
    while a < n:
        a, b, c = b, c, a + b + c
    return a


'''Takes one argument n and returns the index of the first number 
    that reaches length n in the fibonacci'''
'''takes the the seed 1 and 1'''
def fibs_length_index(n):
    a, b = 1, 1
    fibs = [a]
    while len(str(fibs[-1])) < n:
        a, b = b, a + b
        fibs.append(a)
    for index, fib in enumerate(fibs, 1):
        if len(str(fib)) >= n:
            return index



    #-------------------------------Collatz Chain-----------------------------------
''' The Collatz conjecture is  named after Lothar Collatz. 
    The sequence starts with a positive integer n.
    If the previous term is even, the next term is one half the previous term. 
    Otherwise, the next term is 3 times the previous term plus 1.'''
def next_collatz(n):
    if n % 2 == 0:
        return n/2
    else:
        return n*3 + 1


def collatz_chain_length(n):
    count = 1
    while n > 1:
        count += 1
        n = next_collatz(n)
    return count


def longest_collatz():
    max = None
    number = None
    for n in xrange(1000000):
        length = collatz_chain_length(n)
        if max == None or length > max:
            max = length
            number = n
    return number



    #--------------------------triangle numbers--------------------------------------
def gen_tri_number(s):
    ns = []
    for i in xrange(s):
        n = 0.5*i*(i+1)
        ns.append(n)
    return ns


def isTriangle(x):
    n = (sqrt(1 + 8 * x) - 1.0) / 2.0
    return (n % 1 == 0)


def isPentagonal(x):
    n = (sqrt(1 + 24 * x) + 1.0) / 6.0
    return (n % 1 == 0)


def isHexagonal(x):
    n = (sqrt(1 + 8 * x) + 1.0) / 4.0
    return (n % 1 == 0)



#------------------------Number of pathways in a x times y grid---------------------
num_paths_cache = {}

def num_paths(x,y):
    global num_paths_cache
    if x == 0 or y == 0:
        return 1
    elif x < y:
        return num_paths(y,x)
    elif (x,y) in num_paths_cache:
        return num_paths_cache[(x,y)]
    else:
        result = num_paths(x-1,y) + num_paths(x,y-1)
        num_paths_cache[(x,y)] = result
        return result



#-------------------------------Abundant Numbers------------------------------------
'''gives a list of all abundant numbers from range x to n-1'''
def abundant_numbers_from(x, n):
    abundant_numbers = []
    for i in xrange(x, n):
        number_temp = factors(i)
        number_temp.remove(i)
        total = 0
        map(float, number_temp)
        for j in range(len(number_temp)):
            total += number_temp[j]
            if total > i:
                abundant_numbers.append(i)
                break
    return abundant_numbers



#-------------------------------Permutations----------------------------------------
'''return the nth sequence in the permutations of string r'''
from itertools import permutations
def perms(r,n):
    r = ["".join(p) for p in permutations(str(r))]
    sort = sorted(r)
    return sort[n]


'''A kind of permutations where it returns a list for number abc as
        -> set([abc,bca,cab]) in order'''
def rotations(n):
    from collections import deque
    d = deque(n)
    rlist = []
    for i in xrange(len(d)):
        rlist.append(int(''.join(map(d.rotate(1), d))))
    return set(rlist)



#----------------------------------Recurring Decimals-------------------------------
'''returns d of the longest recurring decimal 1 / d where d is less than n'''
from sieve import primes_up_to_n_using_sieve

def recurring(n):
    if n < 8:
        return 7
    for d in primes_up_to_n_using_sieve(n)[::-1]:
        period = 1
        while __builtin__.pow(10,period,d) != 1:
            period += 1
        if d-1 == period:
            break
    return d


'''inspired by a Dr.Dawe lesson as well as the function above, 
   I decided to write a function that returns the period and 
   cycle of 1/n when called upon'''
from sieve import primes_up_to_n_using_sieve

def cycle_of(n):
    if is_terminating(n):
            return "1/" + str(n) + " is not a recurring decimal"
    else:
        if n in primes_up_to_n_using_sieve(n+1):
            return prime_cycle(n)
        else:
            pass

def is_terminating(n):
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        elif n % 5 == 0:
            n = n / 5
        else:
            return False
    return True;

def prime_cycle(n):
    import decimal
    period = 1
    while __builtin__.pow(10,period,n) != 1:
        period += 1
    decimal.getcontext().prec = period
    return period,str(decimal.Decimal(1) / decimal.Decimal(n))


'''to convert decimals into rational fractions, 
   allowing input to be set manually to recurring decimals '''
def decimal_to_fraction(n,recurring=False, digits=None):
    """NOTE: if the decimal is meant to be recurring,
    you might need to give a long repetition of it for accurate results"""
    from fractions import Fraction
    import math
    n = float(n)
    if recurring:
        frac, whole = math.modf(n)
        dig = len(digits)*10
        x = frac * dig
        if whole == 0:
            return str(Fraction((x - frac) / (dig - 1)).limit_denominator())
        else:
            return str(int(whole)) + " " + \
                   str(Fraction((x - frac) / (dig - 1)).limit_denominator())
    else:
        return Fraction(n).limit_denominator()



#-------------------------------Quadratic Equation----------------------------------
'''returns [how many primes produced, a, b, a*b] for the quadratic equation of
   (n**2 + a*n + b) with the range of of |a| and |b| as an input.
   Tests every combination for a and b that can gives the largest amount of 
   primes possible for every consecutive values of n, starting from n = 0.'''
def longestPrimeQuadratic(alim, blim):
    def isPrime(k): # checks if a number is prime
        if k % 2 == 0 or k < 2: return False
        elif k == 2: return True
        else:
            for x in range(3, int(sqrt(k)+1), 2):
                if k % x == 0: return False

        return True

    longest = [0, 0, 0, 0] # length, a, b, a*b

    for a in xrange((alim * -1) + 1, alim):
        for b in xrange(2, blim):
            if isPrime(b):
                count = 0
                n = 0
                while isPrime((n**2) + (a*n) + b):
                    count += 1
                    n += 1

                if count > longest[0]:
                    longest = [count, a, b, a*b]

    return longest



#----------------------------------Palindromes--------------------------------------
def is_palindromes(n):
    return str(n) == str(n)[::-1]


def palindromes_below_n(n):
    p = [x for x in xrange(n+1) if is_palindromes(x)]
    return p



#------------------------------------Pandigital-------------------------------------
def is_pandigital(s):
    return sorted(s) == sorted("123456789")


def is_pandigital_from_digits(n):
    s = str(n)
    return sorted(s) == sorted("123456789")[:len(s)]



#-------------------------------------Geometry---------------------------------------
def pythagorean_trio_from_perimeter(n):
    def _right_a(p):
        for b in range(1, p // 2):
            a = (2 * b * p - p ** 2) / (2 * (b - p))
            if a % 1:
                continue
            a = int(a)
            yield a, b, p - a - b

    return len({tuple(sorted(i)) for i in _right_a(n)})



#-------------------------------------Simple Maths Func-------------------------------
def nCr(n,r):
    f = factorial
    return f(n) / f(r) / f(n-r)





