import random
import statistics

ranum: list[int] = [random.randint(1,100) for i in range(50)]
print(ranum)
#Task a
print("Bigger than 50:", list(filter(lambda x: x > 50, ranum)))
#Task b
print("Divide by 7:", list(filter(lambda x: x % 7 == 0, ranum)))
#Task c - turn into string
print("Two digit numbers:", list(filter(lambda x: x >= 10 and x <= 99, ranum)))
#Task d
print("Equal digits:", list(filter(lambda x: x % 10 == x // 10, ranum)))
#Task e
print("Sum of digits is 9:", list(filter(lambda x: x % 10 + x // 10 == 9, ranum)))
#Task f
print("Numbers bigger than average:", list(filter(lambda x: x > statistics.mean(ranum), ranum)))
#Task g
print("Numbers bigger than bigger * 0.5:", list(filter(lambda x: x > 0.5 * max(ranum), ranum)))
#Task h
print("h:", list(filter(lambda x: x > sorted(ranum)[len(ranum) // 2], ranum)))
#Task i
newlist: list[int] = [int(input("Please enter a number: ")) for i in range(5)]
newlist2: list[int] = [x for x in newlist if x not in ranum]
print(newlist2)
#Task j
def primary(x: int = 0) -> bool:
    if x == 1:
        return False
    for i in range(2, x-1):
        if x % i == 0:
            return False
    return True
print(list(filter(lambda x: primary(x), ranum)))