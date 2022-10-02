"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def isPrime(n):
    if (n <= 0 or n==1):
        return False

    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


def primes(number_of_primes):
    if (number_of_primes <= 0):
        raise ValueError

    list = []

    number = 1
    while len(list) < number_of_primes:
        if isPrime(number):
            list.append(number)
        number += 1

    return list
