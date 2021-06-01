"""
Authored By: Emily Gauvreau

This answer key contains the completed version of the Cafe Menu Ordering system.
It includes two additional functions when compared to the student version: `ask_for_tea()` and `ask_for_cookie()`.
It demonstrates that there are always many ways to alter a program to make it more complex and to make it your own!
There is more commenting then you might see in a normal program but this will help explain why each step works the way it does and why it is important!
"""


def ask_about_coffee():
    """
    This function is responsible for prompting the user to select what size of coffee they would like.
    As well it will ask if the user would like a flavour shot and how many pumps of it they would like if they answer yes.
    Using the information the user provides, the total cost and a list of the coffee items will be recorded and returned to be added to the master list
    """

    # We store both the sizes and flavours in a dictionary as each one has a specific cost associated to it.
    # We create an empty list to append the coffee items ordered to it.
    coffeeSizes = {"small": 2.00, "medium": 3.00, "large": 4.00}
    flavours = {"vanilla": 0.30, "caramel": 0.30, "peppermint": 0.30, "hazelnut": 0.30}
    coffeeType = ["regular", "decaf"]
    coffeeOrder = []

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
        # Here we prompt for the size the user would like, we need separate conditionals since a user could enter s or small as a size, and we need to match it to our dictionary key
        coffeePrompt = input("\nType the name of the size you would like: ")
        if coffeePrompt == "s" or coffeePrompt == "small":
            coffeePrompt = "small"
            tryAgain = False
        elif coffeePrompt == "m" or coffeePrompt == "medium":
            coffeePrompt = "medium"
            tryAgain = False
        elif coffeePrompt == "l" or coffeePrompt == "large":
            coffeePrompt = "large"
            tryAgain = False
        else:
            print("Please enter one of the sizes provided!")

    coffeeTypePrompt = input("\nWould you like regular or decaf? ")

    # Add the price of the size to the total price
    totalCoffeePrice = coffeeSizes[coffeePrompt]

    # Collect user input for whether they would like a flavour shot added to their coffee
    flavourPrompt = input("Would you like a flavour shot added to your coffee? Type y for yes OR n for no: ")
    if flavourPrompt == "y" or flavourPrompt == "yes":
        tryAgain = True
        while tryAgain:
        # Since they selected yes, you must now find out what kind of flavour they want
            flavourShot = input("Type the name of the flavour you would like: ")
            if flavourShot in flavours.keys():
                flavourPrice = flavours[flavourShot]
                tryAgain = False
            else:
                print("Please enter one of the flavours provided!")

        # We must also prompt the user to find the number of pumps they would like
        numOfFlavours = int(input("How many pumps of the flavour would you like? "))
        # Multiple the price of the flavour by the number of pumps
        flavourCost = round((numOfFlavours * flavourPrice), 2)
        # We can then add the flavour cost to the total price we started earlier
        totalCoffeePrice = totalCoffeePrice + flavourCost

        # We will then append the item that they bought in addition to the number of shots and flavour to the list of items
        coffeeOrder.append(coffeeTypePrompt + " " + coffeePrompt + " coffee with " + str(numOfFlavours) + "x " + flavourShot + " flavour shot(s): \t$" + str(totalCoffeePrice))

    else:
        # We will then append the item that they bought to the list of items
        coffeeOrder.append(coffeeTypePrompt + " " + coffeePrompt + " coffee: \t$" + str(totalCoffeePrice))

    # Both the total price for the coffee and the list of coffees are returned, the first variable as an int, the second as a list
    return totalCoffeePrice, coffeeOrder

def ask_about_tea():
    """
    This function is responsible for prompting the user to select what size and flavour of tea they would like.
    The flavours do not incur an extra charge so they are a list not a dictionary, since there is no charge to associate it to.
    Using the information the user provides, the total cost and a list of the items will be recorded and returned to be added to the master list
    """

    # A dictionary contains the keys the user can choose as well as their price as a key-value pair
    # A list holds the flavour options available but since they don't incur an additional charge they don't have a key-value pair
    # An empty list stores the items the user orders
    teaSizes = {"small": 1.50, "medium": 2.50, "large": 3.50}
    teaFlavours = ["peppermint", "earl grey", "green", "camomille", "english breakfast", "citrus"]
    teaOrder = []

    # we iterate through the keys of the list and print it so the user knows the flavour options
    for i in range(len(teaFlavours)):
        print(str(i) + ". " + teaFlavours[i] + " tea")

    # While the loop equals true it will continue, this allows the user to try again if they type an invalid option
    tryAgain = True
    while tryAgain:
        # Here we prompt for the size the user would like, we need separate conditionals since a user could enter s or small as a size, and we need to match it to our dictionary key
        teaPrompt = input("\nType the name of the size you would like: ")
        if teaPrompt == "s" or teaPrompt == "small":
            teaPrompt = "small"
            tryAgain = False
        elif teaPrompt == "m" or teaPrompt == "medium":
            teaPrompt = "medium"
            tryAgain = False
        elif teaPrompt == "l" or teaPrompt == "large":
            teaPrompt = "large"
            tryAgain = False
        else:
            print("Please enter one of the sizes provided!")

    # Then we set the price of the tea using the dictionary values and we prompt the user to select a flavour.
    totalTeaPrice = teaSizes[teaPrompt]
    teaFlavourPrompt = int(input("What flavour would you like your tea to be? Enter the number that corresponds to the selection you would like to make: "))
    # We append their choice to the list that will be provided back to the calculate_total() function
    teaOrder.append(teaPrompt + " " + teaFlavours[teaFlavourPrompt] + "tea: \t$" + str(totalTeaPrice))

    # Both the total price for the tea and the list of tea are returned, the first variable as an int, the second as a list
    return totalTeaPrice, teaOrder


def ask_about_muffin():
    """
    This function is responsible for prompting the user to select what kind of muffin they would like and how many
    Using the information the user provides, the total cost and a list of the items will be recorded and returned to be added to the master list
    """

    # A dictionary contains the keys the user can choose as well as their price as a value pair
    # An empty list stores the items the user orders
    muffinOptions = {"chocolate": 2.00, "blueberry": 2.50, "carrot": 2.00, "fruit mix": 3.00}
    muffinOrder = []

    # we iterate through the keys of a dictionary and print it so the user knows the options
    print("These are the flavours available: ")
    for key in muffinOptions.keys():
        print(key)

    # While the loop equals true it will continue, this allows the user to try again if they type an invalid option
    tryAgain = True
    while tryAgain:
        # Here we prompt the user for the name of their selection and halt the loop if they give a valid answer
        muffinPrompt = input("\nType the name of the muffin you would like: ")
        if (muffinPrompt == "chocolate") or (muffinPrompt == "blueberry") or (muffinPrompt == "carrot") or (muffinPrompt == "fruit mix"):
            tryAgain = False
        else:
            print("Please enter one of the options provided!")

    # We then prompt for what number of muffins
    numOfMuffins = int(input("How many of these muffins would you like? "))

    # Then we can set prices and add the items they order to a list.
    totalMuffinPrice = muffinOptions[muffinPrompt] * numOfMuffins
    muffinOrder.append(str(numOfMuffins) + "x " + muffinPrompt + " muffin: \t$" + str(totalMuffinPrice))

    # Both the total price for the muffins and all the muffins order are returned, the first as an int, the second as a list
    return totalMuffinPrice, muffinOrder


def ask_about_cookie():
    """
    This function is responsible for prompting the user to select what kind of cookie they would like and how many
    Using the information the user provides, the total cost and a list of the items will be recorded and returned to be added to the master list
    """

    # A dictionary contains the keys the user can choose as well as their price as a value pair
    # An empty list stores the items the user orders
    cookieOptions = {"oatmeal": 1.00, "chocolate chip": 1.50}
    cookieOrder = []

    # we iterate through the keys of a dictionary and print it so the user knows the options
    print("These are the flavours available: ")
    for key in cookieOptions.keys():
        print(key)

    # While the loop equals true it will continue, this allows the user to try again if they type an invalid option
    tryAgain = True
    while tryAgain:
        # Here we prompt the user for the name of their selection and halt the loop if they give a valid answer
        cookiePrompt = input("\nType the name of the cookie you would like: ")
        if (cookiePrompt == "oatmeal") or (cookiePrompt == "chocolate chip"):
            tryAgain = False
        else:
            print("Please enter one of the options provided!")

    # We then prompt for what number of cookies
    numOfCookies = int(input("How many of these cookies would you like? "))

    # Then we can set prices and add the items they order to a list.
    totalCookiePrice = cookieOptions[cookiePrompt] * numOfCookies
    cookieOrder.append(str(numOfCookies) + "x " + cookiePrompt + " cookie: \t$" + str(totalCookiePrice))

    # Both the total price for cookies and all the cookies order are returned, the first as an int, the second as a list
    return totalCookiePrice, cookieOrder


def calculate_total():
    """
    This function is responsible for combining all of the information provided by the user for all items on our menu board.
    It will take the lists and prices created by each individual function (where each is responsible for one item) and combine it for the main function
    Here the user will be prompted to continue entering items until they specify their order is done.
    """

    # Here we are instantiating the orderTotal and orderItems so that we can add prices and items to them as the user picks them!
    orderTotal = 0
    orderItems = []

    # While the user wants to keep adding more to their order, continuePicking will be True, once it is False the loop will stop
    continuePicking = True
    while continuePicking:

        menuOptions = ["Coffee", "Tea", "Muffins", "Cookies"]

        # This for loop will do a loop the length of the number of items in the menuOptions list
        # For each item print the it's index+1 followed by the name of the item.
        for i in range(len(menuOptions)):
            print(str(i + 1) + ". " + menuOptions[i])

        # Since the loop associates a number to each item, the user can make their selection with that number
        menuPrompt = int(input("What would you like to order? Enter the corresponding number from above to make your selection: "))

        # The if conditional will check what number was picked and call the appropriate function
        if menuPrompt == 1:
            coffeePrice, coffeeOrder = ask_about_coffee() # We set the function equal to the two variables that it will return
            orderTotal += coffeePrice # We add the coffeePrice to the overall orderTotal
            orderItems.extend(coffeeOrder) # We add the items the user selected to the master list

        elif menuPrompt == 2:
            teaPrice, teaOrder = ask_about_tea()
            orderTotal += teaPrice
            orderItems.extend(teaOrder)

        elif menuPrompt == 3:
            muffinPrice, muffinOrder = ask_about_muffin()
            orderTotal += muffinPrice
            orderItems.extend(muffinOrder)

        elif menuPrompt == 4:
            cookiePrice, cookieOrder = ask_about_cookie()
            orderTotal += cookiePrice
            orderItems.extend(cookieOrder)

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
    """
    This is the main function. It holds the root of our program that initiates the entire menu board.
    We will call any functions necessary to start the program here and we wil print the final menu here.
    """

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
