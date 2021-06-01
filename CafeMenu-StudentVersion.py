"""
Authored By: Emily Gauvreau

Today we will work through a project where you ask a user to pick what they would like from a menu and return the total cost.

It will utilize all of the concepts we learned earlier in the workshop and will allow us to make sure we understand how they all fit together. We will use:
- print statements
- return values
- dictionaries and lists
- for and while loops
- user input
- type casting
- functions

Each function will have a summary above, written as comments, to describe what we expect the function to do. Using this description and the hints left in the function outlines you will be able to fill in the missing information using "fill-in-the-blanks" style.

The purpose of each function is to perform one specific task, this makes our program easier to read and much more efficient. For example, each item on our menu board will have one specific function dedicated to asking the user for their selection.
It will record what they pick and save it in a list that we will then combine with all the other lists to create one master list. The master list will be created in a function specific to combining the users options and prices together.

Let's get started!
"""


def ask_about_coffee():
    """
    This function is responsible for prompting the user to select what size of coffee they would like.
    As well it will ask if the user would like a flavour shot and how many pumps of it they would like if they answer yes.
    Using the information the user provides, the total cost and a list of the coffee items will be recorded and returned to be added to the master list
    """

    # Create a dictionary that contains the sizes small, medium and large, where the keys are $2, $3, $4 respectively.
    coffeeSizes = {}

    # Create a dictionary that contains the flavours vanilla, caramel, peppermint and hazelnut and each are $0.30
    flavours = {}

    # Create a list that contains regular and decaf
    coffeeType = []

    # This is an empty list that we will add the users order to
    # Create an empty list called "coffeeOrder"
    # DELETE THIS LINE AND PUT LIST HERE


    # We must iterate through both of the dictionaries to provide our user with the available options
    print("These are the available sizes: ")
    for key in coffeeSizes.keys():
        print(key)

    print("\nThese are the available flavours: ")
    for key in flavours.keys():
        print(key)

    # While the loop equals true it will continue, this allows the user to try again if they type an invalid option
    tryAgain = True
    while tryAgain:
        # Prompt the user for the size of their coffee.
        coffeePrompt =

        # Create a conditional for each of the sizes where the user can enter either s or small for the small size option
        if ():
        # Save the size in a variable so that you can get the value associated to it in the dictionary later
        # End the loop by changing the boolean
        elif ():
        elif ():
        else:
        print("Please enter one of the sizes provided!")

    # Ask the user if they would like regular or decaf and get their answer
    coffeeTypePrompt =

    # Using the key you saved above access the price of the size from the dictionary and save it to the total cost.
    totalCoffeePrice =

    # Prompt the user for whether they would like a flavour shot added to their coffee (y or yes for the yes option)
    flavourPrompt =
    if flavourPrompt == "y" or flavourPrompt == "yes":
        tryAgain = True
        while tryAgain:
        # Prompt them to find out the name of the flavour they want
        flavourShot =
        if ():
            # Break the loop if the condition is met (similar to the size statements above)
        else:
            print("Please enter one of the flavours provided!")

        # Prompt the user to find the number of pumps they would like hint: type cast
        numOfFlavours =

        # Multiply the price of the flavour by the number of pumps
        # Hint: You will need to access the price using key:value
        flavourCost =

        # Add the flavour cost to the total price we started earlier
        totalCoffeePrice +=

        # Create a string that would read like: "regular small coffee with: 2x vanilla flavour shot(s): $2.60"
        # Hint use concatenation with strings you wrote as well as variables that are saved
        coffeeString = ""

        # Append the string to the coffeeOrder list
        coffeeOrder.append()

    else:
        # Create a string that would read like: "regular small coffee: $2.00"
        coffeeString = ""

        # Append the string to the list of items
        coffeeOrder.append()

    # Both the total price for the coffee and the list of coffees are returned, the first variable as an int, the second as a list
    return totalCoffeePrice, coffeeOrder


def ask_about_muffin():
    """
    This function is responsible for prompting the user to select what kind of muffin they would like and how many
    Using the information the user provides, the total cost and a list of the items will be recorded and returned to be added to the master list
    """


    # Create a dictionary that holds chocolate muffin $2, blueberry $2.5, carrot $2, fruit mix $3
    muffinOptions = {}

    # Create an empty list called "muffinOrder"
    # DELETE THIS LINE AND PUT LIST HERE

    # Using the .keys() function we iterate and print the available flavours
    print("These are the flavours available: ")
    for key in muffinOptions.keys():
        print(key)

    # While the loop equals true it will continue, this allows the user to try again if they type an invalid option
    tryAgain = True
    while tryAgain:
        # Prompt the user for the name of their selection
        muffinPrompt = input()
        # Write an if conditional so that if the name of their selection is valid (in the dictionary) the loop stops
        if ():
        # Halt the loop by changing the boolean
        else:
            print("Please enter one of the options provided!")

    # Prompt for what number of muffins they want
    numOfMuffins =

    # Set the total price of the muffin order to the muffin choice * number of muffins
    totalMuffinPrice =

    # Create a string that would read as "2x blueberry muffin(s): $5" if they chose two blueberry muffins
    muffinString

    # Append the string to the list.
    muffinOrder.append()

    # Both the total price for the muffins and all the muffins order are returned, the first as an int, the second as a list
    return totalMuffinPrice, muffinOrder


def calculate_total():
    """
    This function is responsible for combining all of the information provided by the user for all items on our menu board.
    It will take the lists and prices created by each individual function (where each is responsible for one item) and combine it for the main function
    Here the user will be prompted to continue entering items until they specify their order is done.
    """

    # Here we are defining two variables that will track the overall totals for the menu categories combined
    # Create a variable named "orderTotal" and set it equal to zero
    ## REPLACE THIS LINE WITH ORDERTOTAL

    # Create an empty list named "orderItems"
    ## REPLACE THIS LINE WITH ORDERITEMS

    # While the user wants to keep adding more to their order, continuePicking will be True, once it is False the loop will stop
    continuePicking = True
    while continuePicking:

        # Create a list that contains our two menu options, coffee and muffins
        menuOptions = []

        # This for loop will do a loop the length of the number of items in the menuOptions list
        # For each item, print the its index+1 followed by the name of the item.
        for i in range(len(menuOptions)):
            print(str(i + 1) + ". " + menuOptions[i])

        # Since the loop associates a number to each item, the user can make their selection with that number
        menuPrompt = int(input("What would you like to order? Enter the corresponding number from above to make your selection: "))

        # The if conditional will check what number was picked and call the appropriate function
        if menuPrompt == 1:
            coffeePrice, coffeeOrder = ask_about_coffee() # We set the function equal to the two variables that it will return
            orderTotal += coffeePrice # We add the coffeePrice to the overall orderTotal
            orderItems.extend(coffeeOrder) # We add the items the user selected to the master list

        ## ADD AN ELIF STATEMENT HERE FOR THE SECOND MENU OPTION MUFFINS
        elif ():
        else:
            print("That is not a valid option!")

        # We ask the user if they want to add more, if yes the loop is True and continues, otherwise it's false
        stillPicking = input("Would you like to add more to your order? Type y or yes to continue, n or no to end your order: ")
        if stillPicking == "y" or stillPicking == "yes":
            continuePicking = True
        else:
            continuePicking = False

    # We return the master list and total so that the main function can print them at the end!
    return orderTotal, orderItems


def main():
    # This is the main function. It holds the root of our program that initiates the entire menu board.
    # We will call any functions necessary to start the program here and we wil print the final menu here.
    print("Welcome to our Cafe!")
    print("You can pick any combination of things and we will let you know the total!")

    # Our calculate_total() function returns two variables, one is the total price of the order, the other is a list of items.
    total, orderItems = calculate_total()
    print("\nOrder Total\n")

    # We iterate through the list of items, printing each one for the user to see what they selected at the end!
    for item in orderItems:
        print(item)
    print("The total cost for your order is: $", total)

if __name__ == "__main__":
    main()
