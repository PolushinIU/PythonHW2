#  Напишите программу, которая принимает на вход число N
#  и выдает набор произведений чисел от 1 до N.

n = int(input('введите число => '))
answer = list()
result = 1
for i in range(n):
    result = result * (i + 1)
    answer.append(result)
print(answer)