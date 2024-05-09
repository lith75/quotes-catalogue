# Name: Lithika Ratnayake
# Student Number: 10562398

import json

def input_int(prompt):
    while True:
        try:
            num = input(prompt) # asks user to enter a number
            number = int(num) # converts the number into an integer

            if number >= 1:
                return number # returns the number if it is greater than or equal to zero

        except ValueError:
            print('Invalid input') # prints this if user enters something other than an integer


def input_something(prompt):
    while True:
        text = str(input(prompt))
        if text.isspace(): # checks for whitespace
            continue

        else:
            text.strip() # removes whitespace
            return text
    

def save_data(data):
    f = open('data.txt', 'w') # opens the file
    data = json.dump(data, f, indent = 4) # dumps the data to the file
    f.close() # closes the file


try:
    file = open('data.txt', 'r') #opens the file in read mode
    data = json.load(file) # loads the file into a variable
    file.close() # closes the file

except:
    data = [] # creates an empty list

print('Welcome to the "Quote Catalogue" Admin Program.')

while True:
    print('\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.') # prompts user to choose a option
    choice = input('> ').lower() # converts the choice to lowercase
    
    if choice == 'a':
        quote = input_something("Enter the quote:") # calls the function to enter input
        author = input_something("Enter the author's name:")
        year = input_something("Enter the year (leave blank if unknown):")
        likes = 0
        loves = 0
        details = {"quote": quote, "author": author, "year": year, "likes": likes, "loves": loves} # stores the details entered by the user in a dictionary

        if year == "":
          del details["year"] # deletes year key from dictionary if the user does not add an year

        details_copy = details.copy() # copies the details from the dictionary into a variable
        data.append(details_copy) #appends the details into the list created earlier
        save_data(data) # calls in the function that writes the data to the text file in JSON format
        file = open('data.txt', 'r')
        content = json.load(file)
        file.close()
        print("Quote added!")
        

    elif choice == 'l':
        if data == []:
            print("No quotes saved") # shows this message if the data list is empty

        else:
            print("List of quotes:")
            for index, details in enumerate(data, 1): # goes through all the details in the list
                key = "year"
                short_text = details["quote"][0:40] # slices the quote

                # prints the quote, author and the year based on the given requirements 
                if len(details["quote"]) >= 40 and key not in details:  
                   print('  ' + str(index) + '.) ' + '"' + short_text.rstrip('\n') + "..." + '"' + "-", details["author"])

                elif len(details["quote"]) >= 40:
                   print('  ' + str(index) + '.) ' + '"' + short_text.rstrip('\n') + "..." + '"' + "-", details["author"] + ",", details["year"]) 

                elif key in details:
                   print('  ' + str(index) + '.) ' + '"' + details["quote"].rstrip('\n') + "." + '"' + "-", details["author"] + ",", details["year"]) 

                elif key not in details:
                   print('  ' + str(index) + '.) ' + '"' + details["quote"].rstrip('\n') + "." + '"' + "-", details["author"])

               

    elif choice == 's':
        if data == []:
            print("No quotes saved") 

        else:
            search = input_something("Enter a search term:").lower() # asks the user to enter a search term
            print ("Search results:")
            key = "year"
            for index, details in enumerate(data, 1): 

             short_text = details["quote"][0:40]

             if search in details["quote"].lower() or search in details["author"].lower(): # checks whether the given search terms are in the quote or the author

                 # prints the quote, author and the year based on the given requirements 
                 if len(details["quote"]) >= 40 and key not in details:
                   print(str(index) + '.) ' + '"' + short_text.rstrip('\n') + "..." + '"' + "-", details["author"])

                 elif len(details["quote"]) >= 40:
                   print(str(index) + '.) ' + '"' + short_text.rstrip('\n') + "..." + '"' + "-", details["author"] + ",", details["year"])

                 elif key in details:
                   print(str(index) + '.) ' + '"' + details["quote"].rstrip('\n') + "." + '"' + "-", details["author"] + ",", details["year"]) 

                 elif key not in details:
                   print(str(index) + '.) ' + '"' + details["quote"].rstrip('\n') + "." + '"' + "-", details["author"])

               

    elif choice == 'v':
        try:
            if data == []:
                print("No quotes saved") # prints this if the data list is empty

            else:
                value = input_int("Quote number to view:") # asks the user to enter a quote number to view
                value = value - 1 # subracts one from the number entered by the user
                text = data[value] # stores the number
                key = "year"
                if key in text: # checks if the year is in the quote
                    print('"' + text["quote"].rstrip('\n') + "." + '"' + "\n" , "-", text["author"] + ",", text["year"])
                    print("\n" + "This quote has received", text["likes"], "likes and", text["loves"], "loves.")

                else:
                    print('"' + text["quote"].rstrip('\n') + "." + '"' + "\n" , "-", text["author"])
                    print("\n" + "This quote has received", text["likes"], "likes and", text["loves"], "loves.")


        except: # prints this if the user enters a number that is not in the data list
            print("Invalid index number")
 

    elif choice == 'd':
        try:
            if data == []:
                print("No quotes saved")

            else:
                delete = input_int("Quote number to delete:")
                delete = delete - 1
                del data[delete] # deletes the number that the user enters
                print("Quote deleted!")

        except:
            print("Invalid index number")
           

        save_data(data) # writes the updated version of the data to the file
        
                

    elif choice == 'q':
        print ("Goodbye!") # prints this if user enters q
        break



    else:
        print ("Invalid choice") # prints this if the user enters something that is not given in the choices 



# If you have been paid to write this program, please delete this comment.
