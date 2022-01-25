# Write your solution here
def length_of_longest(list):
   list_len = [len(i) for i in list]
   return (max(list_len))

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = length_of_longest(my_list)
    print(result)

    """Suggested solution
    def length_of_longest(names: list):
    longest = 0
 
    for name in names:
        if len(name) > longest:
          longest = len(name)
 
    return longest
    """