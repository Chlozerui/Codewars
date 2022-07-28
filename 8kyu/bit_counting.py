def countBits(n):
    bits = 0

    while n > 0:
        if int(n) & 1:
            bits += 1

        n /= 2

    return bits

print(countBits(1234))