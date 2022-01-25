# Write your solution here
def read_file(filename: str):
    with open(filename) as filename:
        lines = []
        for line in filename:
            lines.append(line)

    recipe = {}
    for i in range(0, lines.count("\n") + 1):
        recipe[i] = []

    i = 0
    for j in lines:
        if j == "\n":
            i = i + 1
            continue
        else:
            recipe[i].append(j.strip())

    return recipe

def search_by_name(filename: str, word: str):
    recipes = []
    for key, value in read_file(filename).items():
        if word.lower() in value[0].lower():
            recipes.append(value[0])
    return recipes

def search_by_time(filename: str, prep_time: int): 
    recipes = []
    for key, value in read_file(filename).items():
        if prep_time >= int(value[1]):
            recipes.append(f"{value[0]}, preparation time {value[1]} min")
    return recipes

def search_by_ingredient(filename: str, ingredient: str):
    recipes = []
    for key, value in read_file(filename).items():
        for ingredients in value[2:]:
            if ingredients == ingredient:
                recipes.append(f"{value[0]}, preparation time {value[1]} min")
    return recipes

if __name__ == "__main__":
    search = search_by_name("recipes1.txt", "cake")
    for recipe in search:
        print(recipe)

    search = search_by_time("recipes2.txt", 20)
    for recipe in search:
        print(recipe)

    search = search_by_ingredient("recipes2.txt","eggs")
    for recipe in search:
        print(recipe)

"""Suggested solution
def read_file(filename):
    with open(filename) as file:
        rows = []
        for row in file:
            rows.append(row.strip())
 
    recipes = []
    name_in_row = True
    prep_time_in_row = True
    new = { "ingredients": []}
    for row in rows:
        if name_in_row:
            new["name"] = row
            name_in_row = False
            prep_time_in_row = True
        elif prep_time_in_row:
            new["prep_time"] = int(row)
            prep_time_in_row = False
        elif len(row) > 0:
            new["ingredients"].append(row)
        else:
            recipes.append(new)
            name_in_row = True
            new = {"ingredients": []}
    recipes.append(new)
 
    return recipes
 
def search_by_name(filename: str, word: str):
    recipes = read_file(filename)
 
    found = []
    for recipe in recipes:
        if word.lower() in recipe["name"].lower():
            found.append(recipe["name"])
 
    return found
 
def search_by_time(filename: str, time: int):
    recipes = read_file(filename)
 
    found = []
    for recipe in recipes:
        if recipe["prep_time"] <= time:
            found.append(f"{recipe['name']}, preparation time {recipe['prep_time']} min")
 
    return found
 
def search_by_ingredient(filename: str, ingredient: str):
    recipes = read_file(filename)
 
    found = []
    for recipe in recipes:
        if ingredient.lower() in recipe["ingredients"]:
            found.append(f"{recipe['name']}, preparation time {recipe['prep_time']} min")
 
    return found
"""