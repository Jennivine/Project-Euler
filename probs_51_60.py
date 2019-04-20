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

def q54():
    pass

def q55():
    from My_functions import reverse_add_palindrome as rap
    ans = 0
    for i in range(1, 10000):
        iteration = 0
        num = i
        palindrome = False
        while iteration < 50:
            num = rap(num)
            if str(num) == str(num)[::-1]:
                # is palindrome
                palindrome = True
                break
            iteration += 1
        if not palindrome:
            ans += 1
    return ans

def q56():
    largest_sum = 0
    for a in range(100):
        for b in range(100):
            num = a**b
            s = 0
            while num:
                s += num%10
                num //= 10
            if s > largest_sum:
                largest_sum = s
    return largest_sum

def q57():
    pass

def q58():
    pass

def q59():
    from itertools import permutations
    
    with open("`p059_cipher.txt") as f:
        # remains the same even when trying to decipher
        message = map(int, f.readline().strip().split(","))
        length = len(message)
        
    possible_keys = permutations(range(97, 123), 3)

    for key in possible_keys:
        new_message = ""
        counter = 0
        for i in range(length):
            new_message +=  chr(message[i]^key[counter])
            counter = (counter + 1) % 3
        if " the " in new_message:
            decrypted = new_message
            break

    #found the decryption, now answering the euler question
    ascii = 0
    for i in decrypted:
        ascii += ord(i)
        
    return ascii
    
def q60():
    pass
