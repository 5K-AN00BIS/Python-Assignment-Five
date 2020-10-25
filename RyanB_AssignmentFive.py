# Ryan Bachman
# University of Advancing Technology
# CSC235, Python 1, Fall 2020, Online 2
# Lists, indexing, dictionaries and other common data structures. (Week Two)

# Start Program
again = bool(True); # Boolean variable to track whether the program will run again or not.

# WHILE LOOP
# While statement that covers the whole program so it can run again if the user wants.
while (again == bool(True)):
    nestedAgain = bool(True); # Boolean variable to track whether specific calls will run again or not.

    # Begin print statements
    print() # Skips a line
    # Print out the header.
    print("'''---___---''' Ryan's Ultra Awesome First Python Program Tutorial '''---___---'''")
    print() # Skips a line
    # Collect user data and store as a variable.
    name = input("What is your name?: ") # Collect and store user name. STRING INPUT
    age = input("How old are you?: ") # Collect and store age. NUM INPUT
    pi = input("What are the first 3 digits of pi?: ") # Collect and store pi digits (3.14). FLOAT INPUT

    # Create a dictionary to hold the user entered data. DICTIONARY
    userDict = {
        "Name": name,
        "Age": age,
        "Pi Value": pi
    }

    if pi == "3.14":
        print(pi + " is correct!")
    else:
        print(pi + " is incorrect. It should be 3.14!")

    print() # Skips a line.
    # Print out a greeting with the above inputs. OUTPUT
    if pi == "3.14":
        print("Hello " + name + " who is " + age + " years old. It's nice to meet you!")
    else:
        print("Hello " + name + " who is " + age + " years old and doesn't know what pi is. It's nice to meet you!")
    print() # Skips a line.

    firstTime = input("Is this your first time programming? (Yes or No): ") # Collect and store whether it's their first time programming. BOOL INPUT
    print() # Skips a line

    # If statement used to create a list of IDE's and ask a user what they're favorite is.
    if firstTime == "no" or firstTime == "No":
        # Create a list of IDE's. LIST
        ideList = ["Visual Studio", "Notepad++", "JetBrains Products", "XCode", "Eclipse", "Atom", "Unlisted"]

        # FOR lOOP
        # For statement used to loop through the IDE list to give the user choices.
        print("List of IDE's:")
        for x in ideList:
            print(x)

        print() # Skips a line.

        # Ask user for input on which is their favorite in the list?
        favoriteIDE = input("Which IDE from the above list is your favorite? If not found, please select Unlisted: ")
        userDict["Favorite IDE"] = favoriteIDE

        # Nested if statement that will add a new IDE to the ideList list.
        if favoriteIDE == "Unlisted" or favoriteIDE == "unlisted":
            # Ask for user input for new IDE that's unlisted.
            favoriteIDE = input("Please enter your favorite IDE: ")
            # Append the user input into the ideList list.
            ideList.append(favoriteIDE)
            # Add as favorite IDE in the dictionary.
            userDict["Favorite IDE"] = favoriteIDE

    print() # Skips a line
    # Print out instructions for printing in Python.
    print("In today's lesson, we will talk about how to print a line in Python.")
    print("In order to print a new line, type the following:")
    print("print('This is an example.')")
    print("Believe it or not, that's it!")
    print("Now you try typing it: ")

    # WHILE lOOP
    # While statement used to ensure the user is typing the correct response.
    while (nestedAgain == bool(True)):
        printVal = input() # Ask for user input and store in printVal variable. INPUT
        print("You entered: " + printVal) # Prints out what the user entered. OUTPUT

        if printVal != "print('This is an example.')":
            print("Incorrect response. Please try again.")
            nestedAgain = bool(True)
        else:
            nestedAgain = bool(False)

    # Print out separation line.
    print("--------------------------------------------------------------------------")
    print() # Skips a line
    # Print out instructions for commenting in Python
    print("Now let's talk about commenting your code.")
    print("In order to comment a section, just add a #. Simple as that!")
    print("For example:")
    print("# print('This is an example.')")
    print("The line above will not print anything to PowerShell, it's simply a way to comment your code!")
    print("Now you try typing it: ")

    nestedAgain = bool(True) # Set nestedAgain back to true so the below While statement works again.
    # WHILE lOOP
    # While statement used to ensure the user is typing the correct response.
    while (nestedAgain == bool(True)):
        printVal2 = input() # Ask for user input and store in printVal variable. INPUT
        print("You entered: " + printVal2) # Prints out what the user entered. OUTPUT

        if printVal2 != "# print('This is an example.')":
            print("Incorrect response. Please try again.")
            nestedAgain = bool(True)
        else:
            nestedAgain = bool(False)

    # Print out separation line.
    print("--------------------------------------------------------------------------")
    print() # Skips a line
    print("This concludes my first tutorial and thus ends the assignment. Whew!")
    print() # Skips a line
    print("Please see a set of your responses below: ")

    # Below line replaced in favor of a dictionary for the assignment.
    data = {name, age, pi, firstTime, printVal, printVal2, favoriteIDE} # Place all input data into a Set data structure. SET
    # FOR LOOP
    # Use a for loop to print out the Set data structure.
    for x in data:
        print(x)

    print() # Skips a line
    print("Please see your user data below: ")
    # FOR LOOP
    # Use a for loop to print out the Set data structure.
    for x, y in userDict.items():
        print(x, ":", y)

    print() # Skips a line
    # Ask the user whether they want the program to run again or not
    tryAgain = input("Would you like to try again? (Y or N): ")
    print() # Skips a line
    # if statement that will decide whether the program will run again or not.
    if (tryAgain == 'Y' or tryAgain == 'y' or tryAgain == 'Yes' or tryAgain == 'yes'):
        again = bool(True)
        # Restart Program
    else:
        again = bool(False)
        # End Program
else:
    print("Ending program...")
    print()
