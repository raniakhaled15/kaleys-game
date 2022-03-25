j = 0
player = 1
list = []
n = int(input("Enter a number : "))
for i in range(1, n+1):
    list.append(i)
print(f"the numbers are :{list}")
while True:
    p1 = int(input(f"player{player} remove 1 or 2  numbers?"))
    # choosing how many numbers he wants to remove
    if p1 == 1:
        print("choose the number")
        n1 = int(input())
    # choosing the number he wants to remove
        del list[n1 - 1]
    # deleting the number from the list
        list.insert(n1 - 1, '')
    # replacing the number with empty space
        print(list)
    if p1 == 2:
        print("choose the numbers")
        n1 = int(input())
        n2 = int(input())
        # choosing the number he wants to remove
        del list[n1 - 1]
        list.insert(n1 - 1, '')
        del list[n2 - 1]
        list.insert(n2 - 1, '')
        # deleting the numbers from the list
        # replacing the numbers with empty space
        print(list)
    # checking if the list is empty
    for i in list:
        if i == '':
            j += 1
    # diseding the winner
    if j == len(list):
        print(f"player{player} wins")
        break
    # changing the turns of the players
    if player == 1:
        player = 2
    elif player == 2:
        player = 1
