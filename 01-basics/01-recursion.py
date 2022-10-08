# factorial numbers
def factorial(num):
  assert num >= 0 and int(num) == num, 'func take only positive integer number'

  if num <= 1:
    return 1
  
  return num * factorial(num - 1)

# Fibonacci numbers
def fibonacci(num):
  assert num >= 0 and int(num) == num, 'func take only positive integer number'
  if num in [0, 1]:
    return num
  return fibonacci(num - 2) + fibonacci(num - 1)


# sum of digit of positive integer numbers
def sum(num):
  assert num >= 0 and int(num) == num, 'func take only positive integer number'
  if num <= 9:
    return num
  
  return num % 10 + sum(num // 10)

# power of a number
def power(base, exponent):
  if exponent <= 1:
    return 1
  return base * power(base, exponent - 1)

# Greatest common divisor of two numbers
def gcd(num1, num2):
  num1 = abs(num1)
  num2 = abs(num2)

  if num2 == 0:
    return num1

  return gcd(num2, num1 % num2)

# from decimal to binary
def decimalToBinary(num):
  if num == 0 :
    return 0
  return num % 2 + 10 * decimalToBinary(num // 2)

# capitalize words

def capitalizeWords(str):
  if len(str) <= 1:
    return str.upper()
  
  if str[-2] == ' ' :
    str = str[0:-1] + str[-1].upper()
  
  return capitalizeWords(str[0:-1]) + str[-1] 
