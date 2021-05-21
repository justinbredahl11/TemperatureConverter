def main():
    userChoice = 0

    print("Welcome to my temperature conversion program!")

    while userChoice != 3:
        showMenu()

        userChoice = int(input("Enter your choice here: "))

        if userChoice == 1:
            ftemp, ctemp = fahrToCels()
            print("Fahrenheit: ", ftemp, "Celsius: ", ctemp)

        elif userChoice == 2:
            ftemp, ctemp = celsToFahr()
            print("Fahrenheit: ", ftemp, "Celsius: ", ctemp)

    print("Program Over")

def fahrToCels():
    ftemp = float(input("Enter the Fahrenheit temperature here: "))
    ctemp = (ftemp - 32) * 5/9
    return ftemp, ctemp

def celsToFahr():
    ctemp = float(input("Enter the Celsius temperature here: "))
    ftemp = ctemp * (9/5) + 32
    return ctemp, ftemp

def showMenu():
    print("Press 1 to convert Fahrenheit to Celsius")
    print("Press 2 to convert Celsius to Fahrenheit")
    print("Press 3 to exit the program")

main()

