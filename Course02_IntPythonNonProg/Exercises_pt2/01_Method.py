class Student():
    scores = [65,75,85,95]

    def average_score(self):
        total = 0
        for number in self.scores:
            total += number
        average = total / len(self.scores)
        print(f"The student's average is {average}")

stu1 = Student()
stu1.average_score()

'''
scores = [50,60,70]
total = 0
for number in scores:
    total = total + number
average = total / len(scores)
print(total)
print(average)
'''
