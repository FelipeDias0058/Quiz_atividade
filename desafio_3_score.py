score = 0

print(''' De quem é a música 'Hey Jude'?
a - Os Beatles
b - Iron Maiden
c - Rolling Stones
''')

resposta = input().lower()

if resposta == "a":
    print(" Parabéns, você acertou! ")
elif resposta == "b" or "c":
    print(" Tente novamente... ")
else:
    print("Responda com a, b ou c, por favor.")
if resposta == "a":
    score = score + 1

print(''' De quem é a música 'Paint it Black'?
a - Os Beatles
b - Iron Maiden
c - Rolling Stones
''')

resposta = input().lower()

if resposta == "c":
    print(" Parabéns, você acertou! ")
elif resposta == "a" or "b":
    print(" Tente novamente... ")
else:
    print("Responda com a, b ou c, por favor.")
if resposta == "c":
    score = score + 1

print(''' De quem é a música 'Fear of the Dark'?
a - Os Beatles
b - Iron Maiden
c - Rolling Stones
''')

resposta = input().lower()

if resposta == "b":
    print(" Parabéns, você acertou! ")
elif resposta == "a" or "c":
    print(" Tente novamente... ")
else:
    print("Responda com a, b ou c, por favor.")
if resposta == "b":
    score = score + 1

print(score)
