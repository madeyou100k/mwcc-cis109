temperatures = []

while (True):
    print ("select an option from the following menue")
    menu = """"
        1. add temperature
        2. list temperatures
        3. calculate average temperature
        4. exit
        """
    print (menu)
    selection = input("enter a selcetion: ")

    if (selection == "1"):
        temperature = input ("enter a temperture: ")
        temperatures.append(float(temperature))

    elif (selection == "2"):
        print (temperatures)
        input("hit [enter] to continue...")

    elif (selection == 3):
        total = 0
        for temperature in temperatures:
            total += temperature
        average = total / len(temperatures)
        print(f"average temp: {average}")
        input("hit [enter] to continue...")

    elif (selection == "4"):
        print ("goodbye!")
        exit ()