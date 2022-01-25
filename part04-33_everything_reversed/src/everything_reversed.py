# Write your solution here
def everything_reversed(list):
    x = []
    for i in list:
        x.append(i[::-1])
    return x[::-1]
     
if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)