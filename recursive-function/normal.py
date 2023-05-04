def count_numbers(n):
    p = 0
    for num in range(n+1):
        if num%2 == 0:
            p += 1
    return p