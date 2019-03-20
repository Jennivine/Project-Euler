import sys
sys.path.insert(0, './helper_functions')

def q31():
    target = 200
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [1] + [0]*target

    for coin in coins:
        for i in range(coin, target+1):
            ways[i] += ways[i-coin]

    return ways[target]


def q32():
    from Euler_external_func import is_pandigital
    p = set()
    for i in range(2, 60):
        start = 1234 if i < 10 else 123
        for j in range(start, 10000 // i):
            if is_pandigital(str(i) + str(j) + str(i * j)): p.add(i * j)

    return sum(p)


def q33():
    import fractions
    p = fractions.Fraction(1,1)
    for a in xrange(11,100):
        for b in xrange(a+1,100):
            if (a or b) % 10 == 0 or a == b: continue
            La, Lb = [a/10, a%10], [b/10, b%10]
            if any(i in Lb for i in La) and not all(i in Lb for i in La):
                if La[0] in Lb: x = La[0]
                else: x = La[1]
                La.remove(x)
                Lb.remove(x)
                if a*Lb[0] == b*La[0]: p *= fractions.Fraction(La[0],Lb[0])
    return p


def q34():
    from math import factorial
    F = [factorial(i) for i in range(0,10)]
    answer = 0
    for i in xrange(3,2540160):
        a = sum([F[int(j)] for j in str(i)])
        if a == i: answer += i
    return answer


def q35():
    from sieve import primes_up_to_n_using_sieve
    from My_functions import rotations

    n = set(primes_up_to_n_using_sieve(1000000))
    ans = set()
    for i in n:
        j = rotations(str(i))
        if j.issubset(n):
            ans.update(j)
            n.discard(j)
    return len(ans)


def q36():
    from My_functions import is_palindromes
    from My_functions import palindromes_below_n
    x = palindromes_below_n(1000000)
    ans = 0
    for i in x:
        if is_palindromes(bin(i)[2:]):
            ans += i

    return ans


def q37():
    from My_functions import primes_up_to_n_using_sieve
    from My_functions import truncatable_possibilities
    from My_functions import is_prime
    x = filter(lambda x: int(str(x)[::-1]) % 2 != 0,
               primes_up_to_n_using_sieve(1000000)) + primes_up_to_n_using_sieve(100)
    x = sorted(list(set(x)))[4:]
    ans = []
    for i in x:
        if all(is_prime(j) for j in truncatable_possibilities(i)):
            ans.append(i)

    return sum(ans),ans


def q38():
    from My_functions import is_pandigital

    def get_products(base, n):
        return [base*i for i in xrange(1,n+1)]

    def pandigital_number(ns):
        s = ""
        for n in ns:
            s += str(n)
            if len(s)<9:
                pass
            elif len(s) == 9:
                if is_pandigital(s):
                    return int(s)
                else:
                    return None
            else:
                return None

    ns = []
    for base in xrange(1,9999):
        products = get_products(base,10)
        pn = pandigital_number(products)
        if pn:
            ns.append(pn)
            print base, pn

    return max(ns)


def question_38():
    from My_functions import is_pandigital
    def pandigital_from_base(base):
        num_s = ""
        for s in (str(base*i) for i in xrange(1,11)):
            num_s += s
            if len(num_s) < 9:
                pass
            elif len(num_s) == 9:
                if is_pandigital(num_s):
                    return int(num_s)
            else:
                return None

    ns = []
    for base in xrange(1,9999):
        ns.append(pandigital_from_base(base))

    return max(ns)


def q39():
    from My_functions import pythagorean_trio_from_perimeter

    ns = []
    for i in xrange(1,1001):
        n = pythagorean_trio_from_perimeter(i)
        ns.append(tuple([n,i]))

    return max(ns)
    # ans = (solution,perimeter)


def q40():
    from My_functions import prod

    def make_number():
        number = "0."
        for i in xrange(1,200000):
            number += str(i)
        return number

    n = make_number()
    n_list = [n[2],n[11],n[101],n[1001],n[10001],n[100001],n[1000001]]
    ans = prod(map(int,n_list))
    return n_list,ans
