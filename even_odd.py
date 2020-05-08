import random

a = []

for i in range(10):
    n = random.randint(1, 100)
    a.append(n)

print(a)

even = 0
odd = 0

for i in a:
    if i%2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Even:", even)
print("Odd:", odd)