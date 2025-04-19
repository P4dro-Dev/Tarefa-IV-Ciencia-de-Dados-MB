palavra = "banana"
frequencia = {}

for letra in palavra:
    if letra in frequencia:
        frequencia[letra] += 1
    else:
        frequencia[letra] = 1

print(frequencia)  # Saída: {'b': 1, 'a': 3, 'n': 2}