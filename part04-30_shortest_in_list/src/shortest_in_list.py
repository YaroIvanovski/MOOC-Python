# Write your solution here
def shortest(list):
    x = (min((word for word in list if word), key=len))
    return x

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = shortest(my_list)
    print(result)

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = shortest(my_list)
    print(result)

    """Suggested solution
    def shortest(names: list):
    result = ""
 
    for nimi in names:
        if result == "" or len(nimi) < len(result):
            result = nimi
 
    return result
    """