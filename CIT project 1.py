
#-------------------------------METHOD 1-----------------------------------------------------
import random
import PySimpleGUI as psg
l=['Happiness depends upon ourselves!',"One of the secrets of a happy life is continuous small treats.",
   "Success is not final, failure is not fatal: It is the courage to continue that counts.",
   "Don't let anyone tell you what you can't do. Follow your dreams and persist.",
   'Love all,trust a few,do wrong to none',"Have no fear of perfection,you'll neve reach it",
   "Smile :)),because of your smile, you make life more beautiful.",
   "Life is full of temporary people and permanent memories with pain","The future belongs those who beleive in the beauty of their dreams."]

while True:
    s=random.choice(l)
    print('')
    
    print('Todays quote-->',s)
    import pyttsx3
    engine=pyttsx3.init()
    engine.say(s)
    engine.runAndWait()
    print('')
    ch = psg.popup_yes_no("Do you want to Continue?",  title="YesNo")
    print ("You clicked", ch)
    ch = psg.popup_ok_cancel("Press Ok to HEAR next quote", "Press cancel to EXIT",  title="OkCancel")
    if ch=="OK":
        print ("You pressed Ok")
    if ch=="Cancel":
        print ("You pressed Cancel")
        break

#---------------------------------METHOD 2--------------------------------------------
import tkinter as tk
import random

# Define the list of quotes
quotes = [
    "Be yourself; everyone else is already taken. - Oscar Wilde",
    "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe. - Albert Einstein",
    "Be the change that you wish to see in the world. - Mahatma Gandhi",
    "If you tell the truth, you don't have to remember anything. - Mark Twain",
    "In three words I can sum up everything I've learned about life: it goes on. - Robert Frost"
]

# Define a function to generate a random quote
def generate_quote():
    # Get a random quote from the list
    quote = random.choice(quotes)
    # Update the label with the quote text
    quote_label.config(text=quote)

# Create the main window
root = tk.Tk()
root.title("Random Quote Generator")

# Create a label to display the quote
quote_label = tk.Label(root, text="", font=("Helvetica", 16))
quote_label.pack(pady=20)

# Create a button to generate a new quote
generate_button = tk.Button(root, text="Generate Quote", command=generate_quote)
generate_button.pack(pady=10)

# Run the main loop to display the window
root.mainloop()
  





