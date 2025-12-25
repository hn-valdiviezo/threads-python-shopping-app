from appJar import gui 

import pandas
import tkinter
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

app=gui("Main Menu","500x500")

app.addLabel("title", "Welcome to Threads's Main Menu")
app.setLabelBg("title", "lavender")

app.addImage("decor","Threadslogo.gif")
app.setFont(18)

app.addButton("Hello", press)
app.addButton("Tops", press)
app.addButton("Pants", press)
app.addButton("Shoes", press)
app.addButton("Close", press)
app.addButton("Exit",press)
app.go()


