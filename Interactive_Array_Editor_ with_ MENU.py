import random

_min = 0
_max = 101
lst = []

#Execute next line to create list integers in range 0 - 100
#lst = list(range(_min, _max))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Type a numbers in range 0 - 100:")
print("(Type \"n\" to move to next step)")

try:
    while True:
        my_input = int(input(""))
        if my_input > _max - 1 or my_input < _min:
            print("Error! Input number in range 0-100!")
            continue
        else:
            lst.append(my_input)
            print("Your list is:", lst)
except ValueError:
    pass

main_counter = 0
while main_counter >= 0:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Initial list is:\n", lst)
    print("""
    Type an action's number from the list:
    1 - Min. and Max
    2 - Add / Remove
    3 - Sort by min-max / max-min
    4 - Average
    5 - Index of the element
    6 - Qty of the same element in the list
    7 - Missed numbers
    8 - Clear the list and add 50 random numbers
    9 - Show results and finish
    """)

    selection = int(input("Selected action's number is:"))

    #1 - Min. and Max
    if selection == 1:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Initial List:",lst)
        print("Min is:", min(lst), ",Max is:", max(lst))

        main_counter = 1
        next_action = input("Type any key to continue:")
        continue

    #2 - Add / Remove
    elif selection == 2:
        counter2 = 0
        while counter2 >= 0:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Initial List:", lst)
            print("""
            Type an action's number from the list:
            1 - Add
            2 - Remove
            3 - Main menu
            """)
            selection2 = int(input("Selected action's number is:"))

            if selection2 == 1:
                appended_num = int(input("Type a new number:"))
                lst.append(appended_num)
                counter2 = 1
                print(appended_num, "appended...")
                print(lst)

            elif selection2 == 2:
                try:
                    removed_num = int(input("Type a number to remove:"))
                    lst.remove(removed_num)
                    counter2 = 1
                    print(removed_num, "removed...")
                    print(lst)
                except ValueError:
                    print(removed_num, "not in list!")
                    pass
            elif selection2 == 3:
                counter2 = -1
                print("Going back...")

            else:
                print("Error! Wrong input!")
                counter2 = 1
        continue

    #3 - Sort by min-max / max-min
    if selection == 3:
        counter3 = 0
        while counter3 >= 0:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Initial List:", lst)
            print("""
            Type an action's number from the list:
            1 - Sort min-max
            2 - Sort max-min
            3 - Main menu
            """)
            selection3 = int(input("Selected action's number is:"))

            if selection3 == 1:
                print("Sorted min-max...")
                lst.sort()
                counter3 = 1
                print(lst)

            elif selection3 == 2:
                print("Sorted max-min...")
                lst.sort(reverse=True)
                counter3 = 1
                print(lst)

            elif selection3 == 3:
                counter3 = -1
                print("Going back...")

            else:
                print("Error! Wrong input!")
                counter3 = 1
        continue

    #4 - Average
    if selection == 4:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Initial List:", lst)
        print("Average is:", sum(lst) / len(lst))

        main_counter = 1
        next_action = input("Type any key to continue:")
        continue

    #5 - Index of the element
    elif selection == 5:
        counter5 = 0
        while counter5 >= 0:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Initial List:", lst)
            print("""
            Type an action's number from the list:
            1 - Find Index of the element
            2 - Main menu
            """)
            selection5 = int(input("Selected action's number is:"))

            if selection5 == 1:
                index_num = int(input("Type number:"))
                print("The index of number:", index_num, " is:", "[", lst.index(index_num), "]")
                counter5 = 1

            elif selection5 == 2:
                counter5 = -1
                print("Going back...")

            else:
                print("Error! Wrong input!")
                counter5 = 1
        continue

    #6 - Qty of the same element in the list
    elif selection == 6:
        counter6 = 0
        while counter6 >= 0:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Initial List:", lst)
            print("""
            Type an action's number from the list:
            1 - Count Qty of the same element in the list
            2 - Main menu
            """)
            selection6 = int(input("Selected action's number is:"))

            if selection6 == 1:
                qty_num = int(input("Type number:"))
                n = 0
                for elem in lst:
                    if qty_num == elem:
                        n += 1
                print("Qty of number", qty_num, "in the list is:", n)
                counter6 = 1

            elif selection6 == 2:
                counter6 = -1
                print("Going back...")

            else:
                print("Error! Wrong input!")
                counter5 = 1
        continue

    #7 - Missed numbers
    elif selection == 7:
        counter7 = 0
        while counter7 >= 0:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Initial List:", lst)
            print("""
            Type an action's number from the list:
            1 - Find Missed numbers
            2 - Main menu
            """)
            selection7 = int(input("Selected action's number is:"))

            if selection7 == 1:
                lst100 = list(range(0, 101))
                for elem in lst:
                    try:
                        lst100.remove(elem)
                    except:
                        pass
                print("Missed numbers are:", lst100)
                counter7 = 1

            elif selection7 == 2:
                counter7 = -1
                print("Going back...")

            else:
                print("Error! Wrong input!")
                counter7 = 1
        continue

    #8 - Clear the list and add 50 random numbers
    elif selection == 8:
        counter8 = 0
        while counter8 >= 0:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Initial List:", lst)
            print("""
            Type an action's number from the list:
            1 - Clear the list and add 50 random numbers
            2 - Main menu
            """)
            selection8 = int(input("Selected action's number is:"))

            if selection8 == 1:
                lst.clear()
                for i in range(0, 50):
                    lst.append(random.randint(0, 100))
                    i += 1
                counter8 = 1

            elif selection8 == 2:
                counter8 = -1
                print("Going back...")

            else:
                print("Error! Wrong input!")
                counter8 = 1
        continue

    #9 - Show results and finish
    if selection == 9:
        print("Final list is:", lst, "\n------------------END----------------")
        main_counter = -1
        break

    else:
        print("Error! Wrong main input!")
        main_counter = 1
        continue
