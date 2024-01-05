def print_primes(limit):
    num = 2
    while num <= limit:
        is_prime = True
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            else:
                is_prime = False
                break
        if is_prime:
            print(num)
        num += 1


print_primes(10)

	
