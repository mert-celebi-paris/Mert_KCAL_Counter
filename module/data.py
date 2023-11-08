import json
import sys

print(sys.path)
with open("module/data/combo.json") as f:
    combos = json.load(f) ["combos"]


with open("module/data/meals.json") as f:
    meals =json.load(f)["meals"]

# print(combos)
# combos = {combo["id"]:combo for combo in combos}
# meals = {meal ["id"]: meal for meal in meals}