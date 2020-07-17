def is_prime(number):
    if number <= 1:
        return False
    for i in range(number - 1, 2, -1):
        if number % i == 0:
            return False
    return True


print('This number is prime' if is_prime(int(input())) else 'This number is not prime')
