# Write your solution here
sign = input("Whom should I sign this to: ")
save = input("Where shall I save it: ")

with open(save, "w") as file:
    file.write(f"Hi {sign}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")