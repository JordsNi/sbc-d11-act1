letra = ['Q', 'S', 'A', 'M', 'Z', 'R']
print(letra)
n = len(letra)
for i in range (0, n):
    for j in range(0, n-i-1):
        if letra[j] > letra[j + 1]:
            letra[j], letra[j + 1] = letra[j + 1], letra[j]
            print(letra)