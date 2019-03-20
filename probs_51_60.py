import sys
sys.path.insert(0, './helper_functions')

def q51():
    from sieve import primes_up_to_n_using_sieve
    from My_functions import eight_prime_family

    sieve = primes_up_to_n_using_sieve(1000000)
    for prime in sieve:
        if prime > 100000:
            s = str(prime)
            lastDigit = s[5:6]
            if (s.count('0') == 3 and eight_prime_family(s, '0') \
             or s.count('1') == 3 and eight_prime_family(s, '1') \
             or s.count('2') == 3 and eight_prime_family(s, '2')):
                answer = s
    return answer


def q53():
    from My_functions import nCr

    ans = 0
    for n in xrange (1,101):
        for r in xrange (1, n+1):
            if nCr(n,r) > 1000000:
                ans += 1

    return ans
