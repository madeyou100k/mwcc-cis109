grocery_list = []

while(True):
    print (f""""
    'Welcome to Your Shopping List!
    
    Please make a selection from one of the following options:
    
    1. Add an item to the shopping list.
    2. Display the shopping list.
    3. Display the item count.
    4. Display the first item in the shopping list.
    5. Display the last item in the shopping list.
    6. Clear the shopping list.
    7. Exit the shopping list.

    """)
    selection = input("selection: ")

    grocery_list = ['apple', 'banana', 'cherry']

    if(selection == "1"):
        item = input("item to add: ")
        grocery_list.append(item)
        input("Hit [enter to continue...]")

    elif(selection == "2"):
        print(f"grocery liste: {grocery_list}")
        input("Hit [enter to continue...]")

    elif(selection == "3"):
        print(f'item count: {len(grocery_list)}')
        input("Hit [enter to continue...]")

    elif(selection == "4"):
        print(f"First item: {grocery_list[0]}")
        input("Hit [enter to continue...]")

    elif(selection == "5"):
        print(f"Last item: {grocery_list[-1]}")
        input("Hit [enter to continue...]")

    elif(selection =="6"):
        grocery_list = []
        print(f"The shopping list now empty!")
        input("Hit [enter to continue...]")

    elif(selection =="7"):
        print("Goodbye!")
        exit()

    else:
        print("You entered an invalid option.\nPlease try again.")