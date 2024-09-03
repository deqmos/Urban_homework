def ancient_cipher(n):
    password = ''
    for i in range(1, (n + 1) // 2):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                password += f"{i}{j}"

    return password


for k in range(3, 21):
    print(f"password for {k}: {ancient_cipher(k)}")