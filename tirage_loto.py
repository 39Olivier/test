import random

b = list(range(1, 50))
print(b)

for k in range(49):
    hasard = random.randint(0, 48)
    b[k], b[hasard] = b[hasard], b[k]

print(b[:6])

# comments


