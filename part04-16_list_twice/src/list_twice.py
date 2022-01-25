# Write your solution here
my_list = []
while True:
    num = int(input("New item: "))
    if num == 0:
        break
    my_list.append(num)
    in_order = sorted(my_list)
    print("The list now:", my_list)
    print("The list in order:", in_order)
print("Bye!")