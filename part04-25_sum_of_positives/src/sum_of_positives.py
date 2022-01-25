# Write your solution here
def sum_of_positives(list):
    s = 0 
    for x in list:
       if x > 0:
           s = s + x
    return s

if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)