#  Задайте список из n чисел последовательности
#  $(1+\frac 1 n)^n$ и выведите на экран их сумму.

n = int(input('введите чило n => '))
summ = 0 
answer = list()
for i in range(1, n + 1):
    summ += ((1+1/i)**i)
    answer.append(round(((1+1/i)**i), 2))
print(answer)
print(round(summ, 1))
