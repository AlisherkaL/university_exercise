y=[]
p=[]
n=int(input("Введите длину вашего списка: "))

for i in range(n):
    y = [input()]
    p=p+y

for i in range(n):
        for x in range(n - 1):
            if p[x] > p[x + 1]:
                p[x], p[x + 1] = p[x + 1], p[x]

print(p)