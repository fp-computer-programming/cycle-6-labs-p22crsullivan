# Author: CRS 11/12/21
colors = ["Red", "Orange", "Yellow", "Green"]
print(colors)

colors.extend(["Blue", "Indigo", "Violet"])
print(colors.count("Yellow"))

colors.insert(3, "Black")
print(colors)

colors.clear()
print(colors)

print(colors.count("Red"))
