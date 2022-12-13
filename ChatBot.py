#
#
# I M P O R T S
#
#


import pwinput # pwinput for hidding passwords
import time # time for waiting for x time
import webbrowser # webbrowser for opening a website link
import hashlib # hashlib for hashing the users password
import sys # sys for custom Loading message


#
#
# Global Variables
#
#




global filename
filename = "Users.txt" # create Users.txt if the file does not exsit
open(filename, 'a+')
open(filename, 'a+').close()
global infile # make infile a global variable for creating accounts
infile = open(filename, 'r')
global lines # make lines a global variable for creating accounts
lines = infile.readlines() # read the lines in the file


global Data # Data.txt for storing data about users usage of the chat bot
Data = "Data.txt" # create Data.txt if the file does not exsit
open(filename, 'a+')
open(filename, 'a+').close()
global Data_infile # make Data_infile a global variable for storing data
Data_infile = open(filename, 'r')
global Data_lines # make Data_lines a global variable for creating accounts
Data_lines = infile.readlines() # read the lines in the file


global LOGGEDIN
LOGGEDIN = False #Check if a user is logged in or not


#
#
# def Variables
#
#



def FIND_USER(username, password):
    # Find a user with FIND_USER(username, password) and return it
    lineNumber = -1
    for line in open('Users.txt',"r").readlines(): # Read the lines
        lineNumber += 1
        user_info = line.split() # Split on the space, and store the results in a list of strings
        #print(cust_info)
        if user_info == None: # EOF reached
            return[False]
        if username == user_info[0]: # check username is equal to data in the file
            if password == user_info[1]: # check password is equal to data in the file
                return [True, user_info[0], user_info[1], lineNumber] # return the data back with the line number in the file
#
#
#
def CREATE_ACCOUNT():
    #Create an account if you don't have one already
    username = input(f"\n\n_______CREATE_______\n\nWhat would you like your username to be?\n>>")
    if ' ' in username: # check username does not contain spaces
        print(f"Usernames cannot contain spaces, please try again!\n")
        ACCOUNT_MENU() # take user back to account menu 
    if len(username) < 1: # check length of username if greater than 1
        print(f"Usernames must be at least 1 character, please try again!\n")
        ACCOUNT_MENU() # take user back to account menu
    for line in lines: # get all lines in the file
        sline = line.split() # split file lines to check for taken usernames
        #print(sline[0])
        if username != sline[0]: # ignore is username is not taken
            pass
        elif username == sline[0]:# check if username is already taken
            print(f"This username is already taken, use another!\n")
            time.sleep(1.2) # wait 1.2 seconds
            CREATE_ACCOUNT() # take user back to create account if username if taken
    password = pwinput.pwinput(prompt='What would you like your password to be?\n>>', mask='●') # hide user password input with a dot
    if ' ' in password: # check password does not contain spaces
        print(f"Passwords cannot contain spaces, please try again!")
        ACCOUNT_MENU() # take user back to account menu
    if len(password) < 1: # check password is more than 1 character
        print(f"Passwords must be at least 1 character, please try again!\n")
        ACCOUNT_MENU() # take user back to account menu

    
    HashdPassword = hashlib.sha512(password.encode('utf8')).hexdigest() #HASH the password
    newAccount = f"{username} {HashdPassword}\n" #Save the username to the file
    appendFile = open(filename, "a") # open the file to append data
    appendFile.write(newAccount) # write to the file with the new account data
    appendFile.close() # close the file
    time.sleep(0.3) # wait 0.3 seconds
    print(f"\nAccount created! Please login with your new account!\n") # print that the account has been created
    time.sleep(1) # wait 1 second
    MAIN_DISPLAY() # take user to the main display

def LOGIN_ACCOUNT():
    #Login to an existing account
    global username
    username = input(f"\n\n_______LOGIN_______\n\nWhat is your username?\n>>")
    password = pwinput.pwinput(prompt='What is your password?\n>>', mask='●') # hide user password input with a dot
    password = hashlib.sha512(password.encode('utf8')).hexdigest() #Check the hashd password

    CheckUserData = FIND_USER(username, password) # call the function to check username and password
    if CheckUserData == None: # None if the details are incorrect
        print("\nChecking details please wait...")
        time.sleep(1.3) # wait 1.3 seconds
        print("\nIncorrect username or password!\n")
        time.sleep(1.4) # wait 1.4 seconds
        ACCOUNT_MENU() # take user to account menu
    print("\nChecking details please wait...")
    time.sleep(1.4) # wait 1.4 seconds
    print("Account found!\n\n")
    time.sleep(0.9) # wait 0.9 seconds
    global LOGGEDIN # make loggedin a global variable
    LOGGEDIN = True # make logged in to true to show they are logged in
    MAIN_DISPLAY() # take user back to main display

def ACCOUNT_MENU():
    #First menu to be shown to a user to either login or create an account
    userInput = input(f"To login type login\nTo create an account type create\n>>") # ask user to type login or create
    userInput = userInput.lower() # lowercase user input
    while userInput != "login" and userInput != "create": # if user input is not login or create
            userInput = input(f"To login type login\nTo create an account type create\n>>")
    if userInput == "login": # check if user input is login
        load()
        LOGIN_ACCOUNT() # take user to login page
    elif userInput == "create": # check if user input is create
        load()
        CREATE_ACCOUNT() # call create account function

def STORE_DATA(data):
    lineNumber = -1
    for line in open('Data.txt',"r").readlines(): # Read the lines
        lineNumber += 1
        user_info = line.split() # Split on the space, and store the results in a list of strings
        if user_info == None: # EOF reached
            newData = f"{username} {data}\n" #Save the username to the file
            appendFile = open(Data_filename, "a") # open the file to append data
            appendFile.write(newData) # write to the file with the new account data
            appendFile.close() # close the file
        elif username == user_info[0]: # check username is equal to data in the file
            #return [True, user_info[0], lineNumber] # return the data back with the line number in the file
            print("user has existing data stored")

def CHATBOT_MENU():
    #Food Type Question
    print("=======================================================\n")
    print("    ---- What type of food do you want to eat? ----    \n")
    print("                    1. FastFood")
    print("                    2. Chinese")
    print("                    3. Pizza")
    print("                    4. Indian")
    print("                    5. Dessert")
    print("\n=======================================================\n")

    foodChoice = input(">>")
    foodChoiceInputs = ["1","2","3","4","5"] # vaild options from 1-5
    while foodChoice not in foodChoiceInputs: # check input is valid from 1-5
        print("Unknown input\n")
        foodChoice = input(">>")
    foodChoiceOptions = {"1": "FastFood","2": "Chinese","3": "Pizza","4": "Indian","5": "Desert"} # get the names of the options
    foodChoice = foodChoiceOptions[foodChoice]
    
    STORE_DATA(foodChoice)

    load() # display loading animation

    #Location Question
    print("=======================================================\n")
    print("    ---- What location do you want to look in? ----    \n")
    print("                    1. Havant")
    print("                    2. Waterlooville")
    print("                    3. Southsea")
    print("                    4. Petersfield")
    print("\n=======================================================\n")

    global locationChoice # make locationChoice a global variable
    locationChoice = input(">>")
    locationChoiceInputs = ["1","2","3","4"] # vaild options from 1-4
    while locationChoice not in locationChoiceInputs: # check input is valid from 1-4
        print("Unknown input\n")
        locationChoice = input(">>")
    locationChoiceOptions = {"1": "Havant","2": "Waterlooville","3": "Southsea","4": "Petersfield"} # get the names of the options
    locationChoice = locationChoiceOptions[locationChoice]
    load() # display loading animation

    #Budget Question
    print("=======================================================\n")
    print("    ---- What is your budget? ----    \n")
    print("             1. £5-£10")
    print("             2. £10-£20")
    print("             3. £20-£30")
    print("             4. £40-£50")
    print("             5. Over £50")
    print("\n=======================================================\n")

    budgetChoice = input(">>")
    budgetChoiceInputs = ["1","2","3","4","5"] # vaild options from 1-5
    while budgetChoice not in budgetChoiceInputs: # check input is valid from 1-5
        print("Unknown input\n")
        budgetChoice = input(">>")
    budgetChoiceOptions = {"1": "5-10","2": "10-20","3": "20-30","4": "40-50","5": "50"} # get the names of the options
    budgetChoice = budgetChoiceOptions[budgetChoice]
    load() # display loading animation

    #global RestaurantFound
    RestaurantFound = False
    searchfile = open("Restaurants.txt", "r") # open the file for reading
    for line in searchfile: # for every line in the file
        if f"{foodChoice} {locationChoice} {budgetChoice}" in line: # search the file for a restaurant matching the inputs

            RestaurantFound = True

            data = line.split() # split the data from the file

            global nameofRestaurant
            nameofRestaurant = data[3] # get name of restaurant from file data pos 2
            nameofRestaurant = nameofRestaurant.replace("_", " ") # replace any _ in the name of restaurant with a space

            print("=======================================================\n")
            print("    ---- Restaurant Found! ----    \n")
            print(f"      Food Type: {foodChoice}")
            print(f"      Name: {nameofRestaurant}")
            print(f"      Location: {locationChoice}")
            print(f"      Budget: £{budgetChoice}")
            print(f"      Website: {data[4]}\n")
            print(f"    Do you want this restaurant?\n")
            print(f"         1. Yes / 2. No\n")
            print("\n=======================================================\n")

            userInput = input(">>") # get user input
            userInputChoices = ["1","2"] # vaild options from 1-2
            while userInput not in userInputChoices: # check input is valid from 1-2
                print("Unknown input\n")
                userInput = input(">>")

            if userInput == "1": #check if user wants to select this restaurant
                webbrowser.open(data[4]) # open website from the file in position 3
                REVIEW_DISPLAY()
            else:
                MAIN_DISPLAY() # send user back to main display
    if RestaurantFound == False:
        time.sleep(0.9) # wait 0.9 seconds
        print("======================================\n")
        print("    ---- No Restaurant Found! ----    \n")
        print("======================================")
        load()
        MAIN_DISPLAY() # take user back to main display

    searchfile.close() # close the file after looking for a restaurant


def MAIN_DISPLAY():
    print("=============================================\n") # Welcome to chatbot messgae
    print("    ---- Welcome to the SñS ChatBot! ----    ")
    print("\n=============================================")
    time.sleep(0.3) # wait 0.3 seconds
    load()
    if LOGGEDIN == False: # check to see if the user is logged in from the global variable LOGGEDIN
        ACCOUNT_MENU() # if not logged in send user to account menu
    else:
        CHATBOT_MENU() #if user is logged in send user to chatbot menu

def REVIEW_DISPLAY():
    load()
    print("=======================================================\n")
    print("                   ---- Review! ----                   \n")
    print(f"       Do you want to leave a review for the restaurant?\n")
    print(f"                   1. Yes / 2. No\n")
    print("\n=======================================================\n")
    userInput = input(">>") # get user input
    userInputChoices = ["1","2"] # vaild options from 1-2
    while userInput not in userInputChoices: # check input is valid from 1-2
        print("Unknown input\n")
        userInput = input(">>")

    if userInput == "1": #check if user wants to select this restaurant
        REVIEW_RESTAURANT()
    else:
        MAIN_DISPLAY() # send user back to main display

def REVIEW_RESTAURANT():
    load()
    print("=====================================================================\n")
    print("                ---- Review! ----                \n")
    print(f"   How many stars do you want to rate the restaurant?\n")
    print("                     0 Stars                \n")
    print(f"  1. 1 Star / 2. 2 Stars / 3. 3 Stars / 4. 4 Stars / 5. 5 Stars\n")
    print("\n=====================================================================\n")
    userInput = input(">>") # get user input
    userInputChoices = ["1","2","3","4","5"] # vaild options from 1-5
    while userInput not in userInputChoices: # check input is valid from 1-5
        print("Unknown input\n")
        userInput = input(">>")

    load()
    print("=======================================================\n")
    print("              ---- Review! ----              \n")
    print(f"     You have rated the restaurant {userInput} stars.\n")
    print(f"                  {userInput} Stars                ")
    print("\n=======================================================\n")
    load()

    print("==========================================================\n")
    print("                ---- Review! ----                \n")
    print(f"        What did you think of the restaurant?\n")
    print("\n==========================================================\n")
    userReview = input(">>")
    load()
    print("================================================\n")
    print("              ---- Review! ----              \n")
    print(f"                 {userInput} Stars                ")
    print(f"                Your Review:                ")
    print(f"{userReview}")
    print("\n================================================")
    load()

    #save to file
    RestaurantName = nameofRestaurant
    RestaurantName = RestaurantName.replace(" ", "_")
    userReview = userReview.replace(" ", "_")
    newSavedData = f"{locationChoice} {RestaurantName} {userInput} {userReview}\n" #Save the username to the file
    appendFile = open("Reviews.txt", "a") # open the file to append data
    appendFile.write(newSavedData) # write to the file with the new account data
    appendFile.close() # close the file
    print("================================================\n")
    print("              ---- Data Saved ----              ")
    print("\n================================================")
    load()
    MAIN_DISPLAY() # send user back to main display


def load():
    print("\t")
    animation = [
        f'|', f'/',
        f'-', f'\\',
        f'|', f'/',
        f'-', f'\\',
        f'|', f'/',
        f'-', f'\\',
        f'|', f'/',
        f' \n\n'
    ]
    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r" + f"Loading... " +
                         animation[i % len(animation)])
        sys.stdout.flush()


#
#
# M A I N   C O D E
#
#


MAIN_DISPLAY() # run the main display function