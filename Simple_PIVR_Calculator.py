# PIVR (Power, Current, Voltage, Resistance) calculator
import math as mt


def msg():
    print('what parameter is not given ?')


def try_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a numerical value.")


def zero_error(test, parameter, in_put):
    while test == 0:
        print(parameter, "cannot be 0 in this case")
        test = try_input(in_put)

    return test


def checker(in_put):
    in_put = in_put.lower()
    in_put = in_put.strip()
    if in_put == 'p' or in_put == 'i' or in_put == 'v' or in_put == 'r':
        pass
    else:
        print('invalid prompt')


while True:
    print("For power calculations input 'power' \nFor voltage calculations input 'voltage' \nFor current calculations "
          "input 'current' \nFor resistance calculations input 'resistance'\n ")
    #Checking for calculation type
    CalculationType = input("What Calculation Do You Want To Perform ? ")
    CalculationType = CalculationType.strip()
    CalculationType = CalculationType.lower()

    if CalculationType == "resistance":
        msg()
        Null = input('input P for power, I for current, V for voltage: ')
        checker(Null)
    elif CalculationType == "voltage":
        msg()
        Null = input('input P for power, I for current, R for resistance: ')
        checker(Null)
    elif CalculationType == "current":
        msg()
        Null = input('input P for power, V for voltage, R for resistance: ')
        checker(Null)
    elif CalculationType == "power":
        msg()
        Null = input('input I for current, V for voltage, R for resistance: ')
        checker(Null)
    else:
        print("invalid input")

    #collecting data and conditions
    ## for voltage calculations
    if CalculationType == "voltage" and Null == "p":
        curr = try_input("Enter current (I): ")
        rst = try_input("Enter resistance (R): ")
        v = curr * rst
        print("voltage =", format(v, ".2f"), "V")
    elif CalculationType == "voltage" and Null == "r":
        power = try_input("Enter power (P): ")
        curr = zero_error(try_input("Enter current (I): "), "current", "Enter current (I): ")
        v = power / curr
        print("voltage =", format(v, ".2f"), "V")
    elif CalculationType == "voltage" and Null == "i":
        power = try_input("Enter power (P): ")
        rst = try_input("Enter resistance (R): ")
        v = (mt.sqrt(power * rst))
        print("voltage =", format(v, ".2f"), "V")

    ## for resistance calculations
    if CalculationType == "resistance" and Null == "p":
        volt = try_input("Enter voltage (V): ")
        curr = zero_error(try_input("Enter current (I): "), "current", "Enter current (I): ")
        r = volt / curr
        print("resistance =", format(r, ".2f"), "Ω")
    elif CalculationType == "resistance" and Null == "i":
        volt = try_input("Enter voltage (V): ")
        power = zero_error(try_input("Enter power (P): "), "Power", "Enter power (P): ")
        r = (mt.pow(volt, 2)) / power
        print("resistance =", format(r, ".2f"), "Ω")
    elif CalculationType == "resistance" and Null == "v":
        power = try_input("Enter power (P): ")
        curr = zero_error(try_input("Enter current (I): "), "current", "Enter current (I): ")
        r = power / (mt.pow(curr, 2))
        print("resistance =", format(r, ".2f"), "Ω")

    ## for current calculations
    if CalculationType == "current" and Null == "r":
        power = try_input("Enter power (P): ")
        volt = zero_error(try_input("Enter voltage (V): "), "Voltage", "Enter voltage (V): ")
        i = power / volt
        print("current =", format(i, ".2f"), "A")
    elif CalculationType == "current" and Null == "p":
        volt = try_input("Enter voltage (V): ")
        rst = zero_error(try_input("enter resistance (R): "), "resistance", "Enter resistance (R): ")
        i = volt / rst
        print("current =", format(i, ".2f"), "A")
    elif CalculationType == "current" and Null == "v":
        power = try_input("Enter power (P): ")
        rst = zero_error(try_input("enter resistance (R): "), "resistance", "Enter resistance (R): ")
        i = mt.sqrt((power / rst))
        print("current =", format(i, ".2f"), "A")

    #for power calculations
    if CalculationType == "power" and Null == "r":
        volt = try_input("Enter voltage (V): ")
        curr = try_input("Enter current (I): ")
        p = volt * curr
        print("power =", format(p, ".2f"), "W")
    elif CalculationType == "power" and Null == "v":
        rst = try_input("Enter resistance (R): ")
        curr = try_input("Enter current (I): ")
        p = rst * mt.pow(curr, 2)
        print("power =", format(p, ".2f"), "W")
    elif CalculationType == "power" and Null == "i":
        volt = try_input("Enter voltage (V): ")
        rst = zero_error(try_input("enter resistance (R): "), "resistance", "Enter resistance (R): ")
        p = (mt.pow(volt, 2)) / rst
        print("power =", format(p, ".2f"), "W")

    print("\n")
    close = input('Do you want to stop calculations ? If yes write in "y" or press any key to continue : ')
    close = close.strip()
    close = close.lower()
    if close == "y":
        break

