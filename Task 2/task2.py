games: list[str] = ["Fortnite", "Grand theft Auto V", "The Elder Scrolls V: Skyrim", "Dark Souls", "Overwatch"]

#Task a
print("List of games with min 9 letters:", list(filter(lambda x: True if len(x) > 8 else False, games)))
#Task b
print("List of games starts with F:", list(filter(lambda x: True if x.startswith("F") else False, games)))
#Task c
print("List of games with exactly 2 words:", list(filter(lambda x: True if len(x.split()) == 2 else False, games)))
#Task d
print("List of games contains V letter:", list(filter(lambda x: True if "l" in x.lower() else False, games)))
#Task e
print("List of games contains special chars:", list(filter(lambda x: any(i in x for i in "!@#$%^&*:"), games)))
#Task f
games: list[str] = [["Fortnite", 2017],["Grand theft Auto V", 2013],["The Elder Scrolls V: Skyrim", 2011], ["Dark Souls", 2011], ["Overwatch", 2016]]
ga2014: list[str] = list(filter(lambda x: True if int(x[-1]) > 2014 else False, games))
print(f"List of games released after 2014: {ga2014}")