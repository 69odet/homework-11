def encrypt(n):
    first_digit = n
    result = ''
    for i in range(1, first_digit + 1):
        for j in range(i + 1, n):
            if i != j:
                if n % (i + j) == 0:
                    result += f'{i}{j}'

    return result


for i in range(3, 21):
    print(f'{i}: {encrypt(i)}')




