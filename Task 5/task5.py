cities: list[str] = ["Shanghai", "Dubai", "Sydney", "Try", "London", "Paris", "New york", "Tokyo"]

#Task a
print(list(sorted(cities, key=lambda namelen: len(namelen))))
#Task b
print(list(sorted(cities, key=lambda lastchar: lastchar[-1])))
#Task c
print(list(sorted(cities, key=lambda reverse: reverse[::-1])))
#Task d
cities: list[str] = [["Shanghai", 4920, "Asia"], ["Dubai", 1300, "Asia"], ["Sydney", 8780, "Australia"], ["London", 2240, "Europe"], ["Paris", 2050, "Europe"], ["New york", 4690, "North America"], ["Tokyo", 5760, "Asia"]]

#Taskd1
print(list(sorted(cities, key=lambda distance: distance[1])))
#Taskd2
print(list(sorted(cities, key=lambda biggerdistance: biggerdistance[1], reverse= True)))
#Taskd3
print(list(sorted(cities, key=lambda disbyland: disbyland[2])))
#Taskd4
print(list(sorted(cities, key=lambda  disbyland: (disbyland[2], disbyland[1]))))