import random

ranum: list[int] = [random.randint(-50, 50) for i in range(3)]
print(ranum)
#Task a
print(list(map(lambda x: x ** 3, ranum)))
#Task b
print(list(map(lambda x: x % 10 if x > 0 or x % 10 == 0 else 10 - x % 10, ranum)))
#Task c
print(list(map(lambda x: (x * 9 / 5 + 32), ranum)))
#Task d
print(list(map(lambda x: "positive" if x >= 0 else "negative", ranum)))
#Task e
print(list(map(lambda x: "max" if x == max(ranum) else x and "min" if x == min(ranum) else x, ranum)))
#Task f
print(list(map(lambda x: int((x % 10 * 10)) + x // 10 if x >= 0 else (int((x * -1 % 10 * 10)) + x * -1 // 10 ) * -1, ranum)))
#Task g
print(list(map(lambda x: abs(x), ranum)))
#Task h
exp: list[int] = [[7000, 10000], [5000, 300], [8000, 2000]]
exp2: list[int] = list(map(lambda x: x[0] - x[1], exp))
print(exp2)