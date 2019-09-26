def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for num in range(2, n):
            if n % num == 0:
                return False
        return True


def prime(n):
    prime_list = []
    for num in range(1, n + 1):
        if is_prime(num):
            prime_list.append(num)
    return prime_list
