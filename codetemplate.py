from appJar import gui #uncomment this for 100% submission


#Sample Team Project Extra Credit -- Shopping Application 110%
#Make sure to include the files for your team csv and .gif in your submission!
#include the app.Jar folder in the folder where your team files are stored

#Function to greet the user and ask for a category

import pandas
import tkinter #uncomment this for 100% submission
cart = ""
total = 0
bye = []
tdf=pandas.read_csv("threads.csv")
topslist = list(tdf.Tops)
pantslist = list(tdf.Pants)
shoeslist = list(tdf.Shoes)
def greet_user(greeting,sentinel,categoryq,readyq):
    canswer = ' '
    ranswer = sentinel
    print(greeting)
    while ranswer == sentinel:
        canswer = input(categoryq)
        ranswer = input(readyq)
    if canswer == "Tops":
        tops("Welcome to our Tops section! Here are your choices:",topslist,"Which Tops would you like or enter None? ")
    elif canswer == "Pants":
        pants("Welcome to our Pants section!  Here are your choices:",pantslist,"Which Pants would you like or enter None? ")
    elif canswer == "Shoes":
        shoes("Welcome to our Shoes section! Here are your choices:",shoeslist,"Which Shoes would you like or enter None? ")
    else:
        print('Sorry, we do not carry that category.  See you next time!')


#Function to ask user to pick a Main
def tops(greeting,selection,pickq):
    print(greeting)
    for item in selection:
        print(item)
    pantspick = input(pickq)
    if pantspick == "None":
        print("Goodbye")
    elif pantspick == "Tshirt":
        closing("Tshirt",40,"Enjoy your Tshirt!" )
    elif pantspick == "Hoodie":
        closing("Hoodie",35,"Enjoy your Hoodie!" )
    elif pantspick == "Sweatshirt":
        closing("Sweatshirt",90,"Enjoy your Sweatshirt!" )
    elif pantspick == "Long Sleeve":
        closing("Long Sleeve",60,"Enjoy your Long Sleeve!" )
    else:
        closing("Cardigan",20,"Enjoy your Cardigan!" )
    

#Function to ask user to pick a Side
def pants(greeting,selection,pickq):
    print(greeting)
    for item in selection:
        print(item)
    toppick = input(pickq)
    if toppick == "None":
        print("Goodbye")
    elif toppick == "Jeans":
        closing("Jeans",100,"Enjoy your jeans!" )
    elif toppick == "Joggers":
        closing("Joggers",80,"Enjoy your Joggers!" )
    elif toppick == "Cargos":
        closing("Cargos",90,"Enjoy your Cargos!" )
    elif toppick == "Sweatpants":
        closing("Sweatpants",70,"Enjoy your Sweatpants!" )
    else:
        closing("Shorts",40,"Enjoy your Shorts!" )
        
#Function to ask user to pick a Dessert
def shoes(greeting,selection,pickq):
    print(greeting)
    for item in selection:
        print(item)
    toppick = input(pickq)
    if toppick == "None":
        print("Goodbye")
    elif toppick == "Sneakers":
        closing("Sneakers",120,"Enjoy your Sneakers!")
    elif toppick == "Heels":
        closing("Heels",65,"Enjoy your Heels!")
    elif toppick == "Sandals":
        closing("Sandals",40,"Enjoy your Sandals!")
    elif toppick == "Boots":
        closing("Boots",100,"Enjoy your Boots!")
    else:
        closing("Loafer",110,"Enjoy your Loafer!")
        
#Function to give user total price of purchase
def closing(pickeditem,price,goodbye):
    global cart
    global total
    global bye
    cart = cart + " " + pickeditem
    bye.append(goodbye)
    total = total + price
    ttotal = total*1.09
    print("Your items so far:",cart)
    print("Your cost for the",pickeditem,"is $%.2f."%price)
    print("Your total cost is $%.2f."%total)
    print("Your total cost plus tax is $%.2f."%ttotal)
    more = input("Would you like to pick another item (y/n)?")
    if more == "y":
        greet_user("Great!", "n", "What category would you like to browse (Tops, Pants, Shoes)? ", "Ready to browse (y/n)? ")
    else:
        print("Please pay $%.2f!"%ttotal)
        print("Your cart:")
        for l in cart:
            print(l,end="")
        print()
        print("Happy Shopping!")
        for b in bye:
            print(b)


    
#make the code on line 119 a comment (use #) for 100% submission
        
#greet_user("Welcome to our store", "n", "What category would you like to browse (Tops, Pants, Shoes)? ", "Ready to browse (y/n)? ")



#Uncomment this section for 100% submission (remove the three quote marks from lines 123 and 183)
#This is the function that determines code executed when each button is pressed

#Each teammember should replace the Button name assigned to btn (see line 91 for an example) 
#in the if-elif statements below with
#a short title for his/her function.  Then place a call to the
#corresponding function on the next line



def press(btn):
    if btn == "Exit":
        app.stop()
    elif btn == "Hello":
        greet_user("Welcome to our store", "n", "What category would you like to browse (tops, pants, shoes)? ", "Ready to browse (y/n)? ")
    elif btn == "Tops":
        tops("Welcome to our tops section! Here are your choices:",topslist,"Which tops would you like or enter None? ")
    elif btn == "Pants":
         pants("Welcome to our pants section!  Here are your choices:",pantslist,"Which pants would you like or enter None? ")    
    elif btn == "Shoes":
         shoes("Welcome to our shoes section! Here are your choices:",shoeslist,"Which shoes would you like or enter None? ")   
    elif btn == "Close":
        app.infoBox("b1","Thank you for shopping!")   
    else:
        print('Pick a valid option')


#The code below defines the gui, adding buttons, labels, images, color, etc.
#
#Make changes to the title (line 163), image (line 169), and button
#names (lines 175 to 180)

#Edit 500x500 in line 159 to make your window bigger or smaller

app=gui("Main Menu","500x500")

#Replace "Welcome to Our Store's Main Menu" with your team's greeting in line 117

app.addLabel("title", "Welcome to Threads's Main Menu")
app.setLabelBg("title", "lavender")

#Find your team gif image, save to your project code folder, and replace k.gif
#with the image file name in line 166

app.addImage("decor","Threadslogo.gif")
app.setFont(18)

#change the first parameter of the addButton method in lines 172 to 177 with names aligning with your team functions
#make sure they match the Button names in the press function above

app.addButton("Hello", press)
app.addButton("Tops", press)
app.addButton("Pants", press)
app.addButton("Shoes", press)
app.addButton("Close", press)
app.addButton("Exit",press)
app.go() #displays the gui


