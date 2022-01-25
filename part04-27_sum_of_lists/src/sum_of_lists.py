# Write your solution here
def list_sum(a, b):
    zipped_lists = zip(a, b)
    sum = [x + y for (x, y) in zipped_lists]
    return sum

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]

"""Suggested solution
def list_sum(list1: list, list2: list):
    results = []
    for i in range(len(list1)):
        results.append(list1[i] + list2[i])
 
    return results
# Another solution would be use zip-function,
# which creates new list by combining items in two or more lists
# for item1, item2 in zip(list1, list2):
#   results.append(item1 + item2)
# Write your solution here
"""