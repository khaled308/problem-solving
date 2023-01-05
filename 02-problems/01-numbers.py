# count digits
def countDigits(num):
    count = 0

    while num != 0:
        count += 1
        num = int(num / 10)

    return count


# plaindrome number
def isPlaindrome(num):
    num_cp = num
    rev_num = 0

    while num != 0:
        rev_num = rev_num * 10 + num % 10
        num = int(num / 10)

    return rev_num == num_cp


# factorial
def factorial(num):
    res = 1

    while num > 1:
        res *= num
        num -= 1

    return res


# trailing Zeros in factorial
def trailingZerosInFactorial(num):
    # res = num / 5 + num / 25 + num / 125 + ...
    i = 5
    res = 0

    while i <= num:
        res = res + num / i
        i *= 5

    return res


# greatest cummon factor
def greatestCummonDivisor(a, b):
    divisor = a if a < b else b

    while divisor > 0:
        if a % divisor == 0 and b % divisor == 0:
            return divisor

        divisor -= 1

    return 1


# lowest cummon factor
def lowestCummonFactor(a, b):
    num = a if a > b else b

    while num % a != 0 or num % b != 0:
        num += 1

    return num


# prime number
def isPrime(num):
    if num % 2 == 0 or num == 1:
        return False

    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1

    return True


# prime factor of number
def primeFactor(num):
    # when multiply factors we get the original numbers
    primeFactors = []

    for i in range(2, num):
        j = 2
        x = i

        while j * j <= i:
            if i % j == 0:
                break

            j += 1

        while num % x == 0 and j * j > i:
            x = x * i
            primeFactors.append(i)

    return primeFactors


# All divisors of a number
def allDivisors(num):
    divisors = []

    i = 1
    while i * i <= num:
        if num % i == 0:
            divisors.append(i)

        i += 1

    # to get the second divisor which is: num / i
    while i >= 1:
        if num % i == 0:
            divisors.append(int(num / i))

        i -= 1

    return divisors


# binary to decimal
def binaryToDecimal(num):
    res = 0
    base = 1

    while (num > 0):
        last_digit = num % 10
        res += last_digit * base
        base *= 2
        num = int(num / 10)

    return res


# decimal to binary
def decimalToBinary(num):
    res = 0
    base = 1

    while (num > 0):
        last_digit = num % 2
        res += base * last_digit
        base *= 10
        num = int(num / 2)

    return res
