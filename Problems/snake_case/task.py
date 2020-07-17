sentence = input()
result = ''

for char in sentence:
    if char.islower():
        result += char
    else:
        result += '_' + char.lower()

print(result)
