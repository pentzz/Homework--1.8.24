fruits: list[str] = ["Apple", "Banana", "Orange", "Banana", "Strawberry", "Pineapple", "Grapes", "Watermelon"]

#Task a
print(list(map(lambda x: x[::-1], fruits)))
#Task b
print(list(map(lambda x: x[0], fruits)))
#Task c
print(list(map(lambda x: x.upper(), fruits)))
#Task d
print(list(map(lambda x: len(x), fruits)))
#Task e
print(list(map(lambda x: x + "!" if x[-1] == "s" else x, fruits)))
#Task f
fruits: list[str] = [["Apple", 52], ["Banana", 89], ["Orange", 47], ["Banana", 89], ["Strawberry", 32], ["Pineapple", 50], ["Grapes", 69], ["Watermelon", 30]]
#Task f1
cal: list[int] = list(map(lambda x: x[-1], fruits))
print(cal)
#Task f2
joinf: list[str] = list(map(lambda x: x[0] + str(x[1]), fruits))
print(joinf)
#Task f3
joinf2: list[str] = list(map(lambda x: x[0] + str(x[1]) + "!" if x[1] > 50 else x[0] + str(x[1]), fruits))
print(joinf2)