


def one():
    a, b, c = 3, 5, 3 * 5
    la, lb, lc = 999 // a, 999 // b, 999 // c
    ans = a * la * (la + 1) + b * lb * (lb + 1) - c * lc * (lc + 1)
    print(la, lb, lc)
    return ans / 2


def two():
    limit = 4000000
    sum = 0
    a = 1
    b = 1
    while b < limit:
        if b % 2 == 0: sum += b
        h = a + b
        a, b = b, h
    return sum


def three():
    from sympy import factorint
    n = 6879686969
    return 1 if n == 1 else max(factorint(n))  # factorint do the prime factorization
    '''other method'''
    if n == 1:
        return 1
    if n % 2 == 0:
        return max(2, fun(n // 2))
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return max(i, fun(n // i))
    return n


def four():
    n = 3
    # all even digit palindrome numbers are divisible by 11
    if n == 1: return 9
    for z in range(2, 2 * (9 * 10 ** n) - 1):
        left = 10 ** n - z
        right = int(str(left)[::-1])
        if z ** 2 - 4 * right < 0:
            continue
        else:
            root_1 = 1 / 2 * (z + (z ** 2 - 4 * right) ** 0.5)
            root_2 = 1 / 2 * (z - (z ** 2 - 4 * right) ** 0.5)
            if root_1.is_integer() or root_2.is_integer():
                return (10 ** n * left + right)


def five():
    '''LCM of {1,2,3,4,5,6} = 60. The primes up to 6 are 2, 3 and 5. floor(log(6)/log(2)) = 2 so the exponent of 2 is 2.
      floor(log(6)/log(3)) = 1 so the exponent of 3 is 1.floor(log(6)/log(5)) = 1 so the exponent of 5 is 1. Therefore, a(6) = 2^2 * 3^1 * 5^1 = 60.'''
    from math import gcd, floor, log
    from itertools import accumulate
    def lcm(a, b): return a * b // gcd(a, b)

    def aupton(nn): return [1] + list(accumulate(range(1, nn + 1), lcm))

    primelist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    n, s = 20, 1
    new_primel = [i for i in primelist if i <= n]
    for i in new_primel:
        s = s * (i ** (floor(log(n) / log(i))))
    return s, aupton(20)


def six():
    n = 100
    s = ((n * (n + 1)) / 2) * (((n * (n + 1)) / 2) - ((2 * n + 1) / 3))
    return s


def seven():
    ''' P(n)=n^{2}+n+41} is a polynomial equation which we get about 40 primes and 40th prime give a square number'''
    n = 6
    i = 2

    def isprime(k):
        if k <= 1:
            return 0
        if k == 2 or k == 3:
            return 1
        if k % 2 == 0 or k % 3 == 0:
            return 0
        '''All prime number can be represented in form of (6*k + 1) or(6*k - 1)'''
        for j in range(5, 1 + int(k ** 0.5), 6):
            if k % j == 0 or k % (j + 2) == 0:
                return 0

        return 1

    while n > 0:
        if isprime(i):
            n -= 1
        i += 1
    i -= 1
    return i


def eight():
    m = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
    n, k = str(m), 13
    s = ''
    for i in range(0, len(n) - 12):
        # while '0' in s:
        if '0' in s:
            i = i + s.index('0')
        s = n[i:i + 13]

        print(s)


def nine():
    for i in range(1, 500):
        if 1000 * (500 - i) % (1000 - i) == 0:
            a,b= i, 1000 * (500 - i) / (1000 - i)
            break
    return a*b*(1000-a-b)
def ten():
    import sympy
    '''that the number of primes up to a given number x is approximately x/log x.'''
    return  sum(sympy.primerange(2, 2000000))

def o11():
    s=[[8, 2, 22, 97, 38, 15, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
        [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0],
        [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
        [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
        [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
        [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
        [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
        [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
        [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
        [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95],
        [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
        [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57],
        [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
        [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
        [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
        [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
        [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
        [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
        [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
        [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]]
    

