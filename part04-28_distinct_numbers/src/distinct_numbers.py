# Write your solution here
def distinct_numbers(list):
    seen = set()
    y = [x for x in list if x not in seen and not seen.add(x)]
    return sorted(y)

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]


"""Suggested solution
def distinct_numbers(my_list: list):
    results = []
    for item in my_list:
        if item not in results:
            results.append(item)
 
    results.sort()
    return results
"""