def filter_incorrect():
    correct_value = {}
    with open("lottery_numbers.csv") as filename:
        for lines in filename:
            week = lines.replace("\n", "").split(";")[0].replace("week ", "")
            lottery = lines.replace("\n", "").split(";")[1].split(",")
            try:
                if int(week) and int(week) >=1 and int(week) <= 52:
                    valid_num = 0
                    for i in lottery:
                        try:
                            if int(i) and int(i) >= 1 and int(i) <= 39 and lottery.count(i) == 1:
                                valid_num = valid_num + 1
                        except ValueError:
                                pass 
                    if valid_num == 7:
                        correct_value[week] = lottery
            except ValueError:
                pass 
 
    open("correct_numbers.csv", "w").close()
    with open("correct_numbers.csv", "w") as filename:
        for week, lottery in correct_value.items():
            content = "week " + week + ";"
            for i in lottery:
                content = content + i + ","
            content = content[:-1]
            filename.write(content + "\n")

"""Suggested solution
def filter_incorrect():
    with open("lottery_numbers.csv") as input_file, open("correct_numbers.csv", "w") as result_file:
        for row in input_file:
            parts = row.strip().split(";")
            if len(parts) != 2:
                continue
            week = parts[0].split(" ")
            error = False
            if len(week) != 2 or week[0] != "week":
                error = True
            try:
                x = int(week[1])
            except:
                error = True
            number_list = parts[1].split(",")
            if len(number_list) != 7:
                error = True
 
            # numbers already listed --> to find out duplicates
            listed = []
            for item in number_list:
                try:
                    number = int(item)
                    if number < 1 or number > 39 or number in listed:
                        error = True
                    listed.append(number)
                except:
                    error = True
            if not error:
                result_file.write(row)
"""