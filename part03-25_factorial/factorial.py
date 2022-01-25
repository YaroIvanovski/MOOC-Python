# Write your solution here
while True:
    num = int(input("Please type in a nuber:"))
    if num <= 0:
        print("Thanks and bye!")
        break

    fact = 1
    
    for i in range(1, num + 1):
        fact = fact * i
        
    print (f"The factorial of the number {num} is ",end="")
    print (fact)