# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Nahien Chowdhury, November 30, 2019, Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'Products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:
    properties:
        product_name: (string) with the products's name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Nahien Chowdhury, November 30, 2019, Modified code to complete assignment 8
    """
    pass
# Step 1
    # TODO: Add Code to the Product class
    # Step 1.1 - Initializing Product Name and Price
    def __init__(self, product_name: str, product_price: float):
        try:
            self.__product_name = str(product_name)
            self.__product_price = float(product_price)
        except Exception as e:
            raise Exception("Error setting initial Value: \n" + str(e))

    # Step 1.2 - Defining Properties for product name
    @property
    def product_name(self):
        return str(self.__product_name)

    @product_name.setter
    def product_name(self, Value: str):
        if str(Value).isnumeric():
            self.__product_name = Value
        else:
            raise Exception("Invalid. Please enter non numeric names.")

    # Step 1.3 - Defining Properties for product price
    @property
    def product_price(self):
        return float(self.__product_price)

    @product_price.setter
    def product_price(self, Value: float):
        if str(Value).isnumeric():
            self.__product_price = float(Value)
        else:
            raise Exception("Prices must be numbers")

    # Step 1.4 - Defining methods used for converting product data to string.
    def to_string(self):
        return self.__str__()
    def __str__(self):
        return self.product_name + "," + str(self.product_price)
# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
# Step 2
class FileProcessor:
    """Processes data to and from a file and a list of product objects:
    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Nahien Chowdhury, November 30, 2019, Modified code to complete assignment 8
    """
    pass

    # TODO: Add Code to process data from a file
    @staticmethod
    # Step 2.1 - Define Data Saving Method.
    def save_data_to_file(FileName: str, ProductObjectsList: list):
        Success = False
        try:
            file = open(FileName, "w")
            for product in ProductObjectsList:
                file.write(product.__str__() + "\n")
            file.close()
            Success = True
        except Exception as e:
            print("There was an error.")
            print(e, e.__doc__, type(e), sep='\n')
        return Success

    # TODO: Add Code to process data to a file
    @staticmethod
    # Step 2.2 - Define Data Reading Method.
    # Did this in methods per instruction instead of putting it in For Loop in the Main Body of Script.
    def read_data_from_file(FileName: str):
        ProductRowList = []
        try:
            file = open(FileName, "r")
            for line in file:
                data = line.split(",")
                row = Product(data[0], data[1])
                ProductRowList.append(row)
            file.close()
        except Exception as e:
            print("There was an error.")
            print(e, e.__doc__, type(e), sep='\n')
        return ProductRowList

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
# Step 3
    # TODO: Add docstring
class IO:
    """ A class for performing Input and Output Operations."""
    # TODO: Add code to show menu to user
    @staticmethod
    # Step 3.1 - Method for creating Menu Options for display to user.
    def OutputMenuItems():
        """
        Displaying a menu of choices to the user
        """
        print('''
        Menu of Options
        1) Show current data
        2) Add a new item.
        3) Save Data to File & Exit Program
        ''')
        print()  # Add an extra line for looks

    # TODO: Add code to get user's choice
    @staticmethod
    # Step 3.2 - Method for accepting the Choice from user.
    def InputMenuChoice():
        """ Gets the menu choice from a user
        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    # TODO: Add code to show the current data from the file to user
    @staticmethod
    # Step 3.3 - Method for showing the current data from file to user.
    def ShowCurrentItemsInList(RowList: list):
        """
        Showing user current items in list.
        """
        print("Your list of products entail: ")
        for row in RowList:
            print(row.product_name + " (" + str(row.product_price) + ")")
        print()  # Add an extra line for looks

    # TODO: Add code to get product data from user
    @staticmethod
    # Step 3.3 - Method for adding product data from user
    def User_Input_PD():
        """
        Gets user input data for a product object
        """
        try:
            Name = str(input("What's the Product Name? - ").strip())
            Price = float(input("What's the Price? - ").strip())
            print()  # Add an extra line for looks
            p = Product(product_name=Name, product_price=Price)
        except Exception as e:
            print(e)
        return p

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #

# TODO: Add Data Code to the Main body
# Step 4 - Process user's menu choice
while(True):
    IO.OutputMenuItems()  # Shows menu
    strChoice = IO.InputMenuChoice()  # Accepts the menu option choice
    # Step 4.1 - Show current data
    if (strChoice.strip() == '1'):
        IO.ShowCurrentItemsInList(lstOfProductObjects)  # Show current data in the list/table
        continue
    # Step 4.2 - Add New Data
    elif(strChoice.strip() == '2'):
        # Place IO code in a new function
        print()  # Add an extra line for looks
        # Place processing code in a new function
        lstOfProductObjects.append(IO.User_Input_PD())
        continue  # to show the menu
    # Step 4.3 - Save and Exit.
    elif(strChoice == '3'):
        # let user save current data to file and exit program
        # FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
        # break # and Exit
        # Step 3.4.a - Show the current items in the table
        if ("y" == str(input("Save this data to file? (Y / N) - ")).strip().lower()):  # Double-check with user
            # ToDo: Place processing code in a New function
            objFile = open(strFileName, "w")
            input("Data saved to file! Press the [Enter] key to exit.")
            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            break  # and Exit
        else:  # Let the user know the data was not saved
            input("New data was NOT saved, but previous data still exists. Press the [Enter] key to return to menu.")
            continue


# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program