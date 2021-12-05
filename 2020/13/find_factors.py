def find_factors(N):
    i = 1
    while i <= N:
        if N % i == 0:
            print(i)
        i += 1

find_factors(1068781)