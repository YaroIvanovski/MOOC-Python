# Write your solution here
def all_the_longest(list):  
    x = 0
    string = []
    for i in list:
        if len(i) > x:
            string = [i]
            x = len(i)
        elif len(i) == x:
            string.append(i)
    return string

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = all_the_longest(my_list)
    print(result) # ['eleventh']
    
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']

"""Suggested solution
def all_the_longest(names: list):
    result = []
 
    for name in names:
        if result == [] or len(name) > len(result[0]):
            result = [name]
        elif len(name) == len(result[0]):
            result.append(name)
 
    return result
"""