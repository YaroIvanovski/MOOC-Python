# Write your solution here
def no_shouting(list):
    x = []
    for i in list:
        if not i.isupper():
            x.append(i)
    return x

if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)
