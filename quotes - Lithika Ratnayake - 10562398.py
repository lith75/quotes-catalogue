# Name: Lithika Ratnayake
# Student Number: 10562398


import tkinter # imports the necessary modules needed in the program
import tkinter.messagebox
import json

class ProgramGUI: # constructer for the gui

    def __init__(self):
        self.main = tkinter.Tk()
        self.main.title("Quote Catalogue") # creates a heading in the gui
        self.main.geometry('350x500') # size of the window is been given


        self.bottom = tkinter.Frame(self.main, padx = 8, pady = 4) # A frame is being created

        
        try:
            file = open('data.txt', 'r') #opens the file in read mode
            self.data = json.load(file) # loads the file into a variable
            file.close() # closes the file

        except:
            tkinter.messagebox.showerror("Error", "Missing/Invalid file") # shows an error message if the file is missing or contains invalid details
            command = self.main.destroy() # destroys the window
            return 

        self.current_quote = 0 # sets current quote to 0

        self.quote = tkinter.Label(self.main, wraplength=300, justify='center', font = (14)) # creates a label to display the quote 
        self.quote.pack() # packs the label

        self.author = tkinter.Label(self.main, font = ('Times New Roman', 12, "bold italic"))  # creates a label to display the author
        self.author.pack()

        self.skip = tkinter.Button(self.bottom, text = 'skip', bg = 'orange', fg = 'black', command=lambda: self.rate_quote("skip"))# creates a button to skip the quote
        self.skip.pack(side = 'left') # packs the button on the left side of the window

        self.likes = tkinter.Button(self.bottom, text = 'like', bg = 'light green', fg = 'black', command=lambda: self.rate_quote("likes")) # creates a button to like the quote
        self.likes.pack(side = 'left') 

        self.loves = tkinter.Button(self.bottom, text = 'love', bg = 'yellow', fg = 'black', command=lambda: self.rate_quote("loves")) # creates a button to love the quote
        self.loves.pack(side = 'left')

        self.bottom.pack()

        self.show_quote()

        tkinter.mainloop()
 


    def show_quote(self):
        details = self.data[self.current_quote] # refers to the quote in the data list
        key = "year"
        if key in details: # if year is in the quote 
            quote = ('"' + details['quote'].rstrip('\n') + "." + '"') # prints the quote
            self.quote.configure(text = quote) # displays the quote in the gui 

            author = '-' + details['author'] + "," + details['year'] # prints the year
            self.author.configure(text = author) # displays the author's name in the gui


        else: # if year is not present in the quote, only quote and author's name are shown in the gui
            quote_2 = ('"' + details['quote'].rstrip('\n') + "." + '"')
            self.quote.configure(text = quote_2)

            author_2 = '-' + details['author']
            self.author.configure(text = author_2)


    def show_rating(self): # function that writes the data to the file
        f = open('data.txt', 'w') # opens the file
        data = json.dump(self.data, f, indent = 4) # dumps the data to the file
        f.close() # closes the file



    def rate_quote(self, rating):
        likes = 0
        loves = 0
        if rating == "likes": # if likes button is clicked
            self.data[self.current_quote][rating]
            self.data[self.current_quote]['likes'] = self.data[self.current_quote]['likes'] + 1 # adds one to likes

            self.show_rating() # calls the function to write the data to the file

            tkinter.messagebox.showinfo("Rating Recorded", "Your rating has been recorded") # shows a message


        elif rating == "loves": # if the loves button is clicked
            self.data[self.current_quote][rating]
            self.data[self.current_quote]['loves'] = self.data[self.current_quote]['loves'] + 1 # adds one to loves

            self.show_rating()

            tkinter.messagebox.showinfo("Rating Recorded", "Your rating has been recorded")


        else:
            tkinter.messagebox.showinfo("Rating Skipped", "You have skipped rating this quote") # shows this message if the skip button is clicked



        if self.data[self.current_quote] == self.data[-1]:
            tkinter.messagebox.showinfo("End of quotes", "That was the last quote, the program will now end.") # shows this message once the last quote in the list is displayed
            command = self.main.destroy() # destroys the windows

           
        else:
            self.current_quote = self.current_quote + 1 # adds one to current_quote so the next quote is displayed

            self.show_quote() # displays the quote
            

gui = ProgramGUI()


# If you have been paid to write this program, please delete this comment.
