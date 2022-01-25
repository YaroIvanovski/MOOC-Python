# Write your solution here
def most_common_character(list):
    counter = 0
    x = list[0]
     
    for i in list:
        curr_frequency = list.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            x = i
 
    return x

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))
    
    second_string = "exemplaryelementary"
    print(most_common_character(second_string))

"""Suggested solution
def most_common_character(my_string: str):
    most_common = my_string[0]
    for character in my_string:
        if my_string.count(character) > my_string.count(most_common):
            most_common = character
 
    return most_common
"""