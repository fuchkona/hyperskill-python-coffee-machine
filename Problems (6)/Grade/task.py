student_score = int(input())
max_score = int(input())

student_percent = (student_score * 100) / max_score

if 90 <= student_percent:
    print('A')
elif 80 <= student_percent:
    print('B')
elif 70 <= student_percent:
    print('C')
elif 60 <= student_percent:
    print('D')
else:
    print('F')
