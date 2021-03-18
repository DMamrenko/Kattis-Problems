#Kattis: Final Exam @https://open.kattis.com/problems/finalexam2

questions = int(input())
answers = []
for i in range(questions):
    answers.append(input())

hanhs_answers = answers[1:]

correct = 0
for index, answer in enumerate(hanhs_answers):
    if answer == answers[index]:
        correct += 1

print(correct)