# Write your solution here
def formatted(list):
    listN = []
    for i in list:
        listN.append(f"{i:.2f}")
    return listN

if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)