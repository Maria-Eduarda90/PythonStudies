def count_numbers(n):
    if n == 0:
        return 1
    elif n%2 == 0:
        return 1 + count_numbers(n-1)
    else:
        return count_numbers(n-1)
