scores = input().split()
# put your python code here
lives = 3
score = 0

for answer in scores:
    if lives <= 0:
        break
    if answer == 'C':
        score += 1
    else:
        lives -= 1

print('You won' if lives > 0 else 'Game over')
print(score)
