import math
#TODO write comment

def next_non_zero_index(numbers,index):
    while True:
        index = index + 1
        if index >= len(numbers) or numbers[index] != 0:
            return index

# Cross out (make zero) all elements of 'numbers' that are a multiple of 'step'
# beyond 'index'.
# e.g.
#   cross_out_multiples([0,1,2,3,4,5,6,7,8,9,10], 3, 2) causes the list to become
#                       [0,1,2,3,4,0,6,0,8,0,10]
# Return value is always None.
def cross_out_multiples(numbers, index, step):
    while True:
        index = index + step
        if index >= len(numbers):
            return None
        else:
            numbers[index] = 0

def primes_up_to_n_using_sieve(n):
    numbers = range(n+1)
    index = 1
    primes = []

    while True:
        index = next_non_zero_index(numbers,index)
        if index >= len(numbers):
            break
        number = numbers[index]
        primes.append(number)
        cross_out_multiples(numbers, index, number)

    return primes

# another sieve
def primes_sieve(n):
    prime_n = int(2 * n * math.log(n))
    sieve = [True] * prime_n
    count = 0

    for i in range(2, prime_n):
        if sieve[i]:
            count += 1
            if count == n:
                return i
                for j in range(2 * i, prime_n, i):
                    sieve[j] = False


#prime sieve
def sieve(n):
    is_prime = [True]*n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    # even numbers except 2 have been eliminated
    for i in xrange(3, int(n**0.5+1), 2):
        index = i*2
        while index < n:
            is_prime[index] = False
            index = index+i
    prime = [2]
    for i in xrange(3, n, 2):
        if is_prime[i]:
            prime.append(i)
    return prime