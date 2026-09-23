def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
n = int(input("Сколько учеников?"))
for i in range(n):
    score = float(input(f"Введите баллы учеников {i+1}:"))
    print(get_grade(score))

#===================================================================================

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
n = int(input("Сколько учеников? "))
total = 0
best = 0
worst = 100
count_A = 0
count_B = 0
count_C = 0
count_D = 0
count_F = 0
for i in range(n):
    score = float(input(f"Введите баллы ученика {i+1}: "))
    m = total + score
    if score > best:
        best = score
    if score < worst:
        worst = score
    average = m / n
    grade = get_grade(score)
    if grade == "A":
        count_A = count_A + 1
    elif grade == "B":
        count_B = count_B + 1
    elif grade == "C":
        count_C = count_C + 1
    elif grade == "D":
        count_D = count_D + 1
    else:
        count_F = count_F + 1
print("Средний балл:", average)
print("Лучший результат:", best)
print("Худший результат:", worst)
print("Оценок A:", count_A)
print("Оценок B:", count_B)
print("Оценок C:", count_C)
print("Оценок D:", count_D)
print("Оценок F:", count_F)