
from datetime import datetime

d = int(input("Day: "))
m = int(input("Month: "))
y = int(input("Year: "))

birth = datetime(y, m, d)
mil = datetime(1999, 12, 31)

if mil > birth:
    print(f"You were {(mil - birth).days} days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")
