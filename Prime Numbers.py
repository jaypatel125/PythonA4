# I Jay Patel, 000881881, certify that this work is my own effort and that I have not allowed anyone else to copy from it.
def prime_generator(number):
    primes = [True] * (number + 1)
    primes[0], primes[1] = False, False  # 0 and 1 are not prime numbers

    for p in range(2, int(number**0.5) + 1):
        if primes[p]:
            for i in range(p * p, number + 1, p):
                primes[i] = False

    result = [p for p in range(2, number + 1) if primes[p]]
    return result

# Get user input for the number
number = int(input("Enter Number: "))

# Call the function and print the result
result = prime_generator(number)
print("Prime numbers up to", number, "are:", result)
