import string
from datetime import datetime

def is_it_valid(pic: str):
    check_mark = "0123456789ABCDEFHJKLMNPRSTUVWXY"

    # Check the length of the SSN
    if len(pic) != 11:
        return False

    # Check the format of the birth date of the SSN
    for i in range(0, 6):
        if pic[i] not in string.digits:
            return False
        
    # Check the punctuation mark of the SSN
    if pic[6] not in ["+", "-", "A"]:
        return False
        
    # Check the validity of the birth date, means check the birth date and the punctuation mark of the SSN
    if pic[6] == "+":
        year = int("18" + pic[4] + pic[5])
    if pic[6] == "-":
        year = int("19" + pic[4] + pic[5])
    if pic[6] == "A":
        year = int("20" + pic[4] + pic[5])
    
    month = int(pic[2] + pic[3])
    date = int(pic[0] + pic[1])

    isValidDate = True
    try:
        datetime(year, month, date)
    except ValueError:
        isValidDate = False

    if not isValidDate:
        return False
    
    # Check the check mark of the SSN
    if check_mark[int(pic[0:6] + pic[7:10]) % 31] != pic[10]:
        return False
    
    return True 

if __name__ == "__main__":
    print(is_it_valid("081842-720N"))

"""Suggested solution
from datetime import datetime
 
def is_it_valid(pic: str):
    if len(pic) != 11:
        return False
    numbers = pic[:6]+pic[7:10]
    for x in numbers:
        if x not in "0123456789":
            return False
    century_marker = pic[6]
    if century_marker not in "+-A":
        return False
    day = int(pic[:2])
    month = int(pic[2:4])
    year = int(pic[4:6])
    if century_marker == "+":
        year += 1800
    if century_marker == "-":
        year += 1900
    if century_marker == "A":
        year += 2000
    try:
        test = datetime(year, month, day)
    except:
        return False
    characters = "0123456789ABCDEFHJKLMNPRSTUVWXYZ"
    index = int(numbers)%31
    return characters[index] == pic[-1]
"""