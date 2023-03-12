import tkinter as tk
from tkinter import ttk
from tkinter import*
from PIL import Image, ImageTk
import random
from datetime import date
from datetime import datetime

prices = {
    "Cheese Pizza" : 10,
    "Peperoni Pizza" : 12,
    "Sausage Pizza" : 12,
    "Hawaiian Pizza" : 15,
    "MeatTrio Pizza" : 15,
    "Veggie Pizza" : 15,
}

root  = Tk()

root.title("Pizza Pizza")

# ------------------------------------functions---------------------------------------------#

#Create a function to genrate a random order_id
def ORDER_ID():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    order_id = "BIN_"
    random_letters = ""
    random_digits = ""
    for i in range(0,3):
        random_letters += random.choice(letters)
        random_digits += str(random.choice(numbers))

    order_id += random_letters + random_digits
    return order_id


#button to add item to order
def add():
    # update transaction label
    current_order = orderTransaction.cget("text")
    added_ = displayLabel.cget("text") + "...." + str(prices[displayLabel.cget("text")]) + "$ "
    updated_order = current_order + added_
    orderTransaction.configure(text=updated_order)

    # label for order total
    order_total = orderTotalLabel.cget("text").replace("TOTAL : ", "")
    order_total = order_total.replace("$", "")
    updated_total = int(order_total) + prices[displayLabel.cget("text")]
    orderTotalLabel.configure(text="TOTAL : " + str(updated_total) + "$")

#remove button from display label
def remove():
    _to_remove = displayLabel.cget("text") + "...." + str(prices[displayLabel.cget("text")])
    transaction_list = orderTransaction.cget("text").split("$ ")
    transaction_list.pop(len(transaction_list) - 1)

    if _to_remove in transaction_list:
        # update transaction label
        transaction_list.remove(_to_remove)
        updated_order = ""
        for item in transaction_list:
            updated_order += item + "$ "

        orderTransaction.configure(text = updated_order)

        #add up the transaction order total
        order_total = orderTotalLabel.cget("text").replace("TOTAL : ", "")
        order_total = order_total.replace("$", "")
        updated_total = int(order_total) - prices[displayLabel.cget("text")]
        orderTotalLabel.configure(text="TOTAL : " + str(updated_total) + "$")


# display button functions

# cheese pizza button
def displayCheesePizza():
    CheesePizzaFrame.configure(
        relief = "sunken",
        style = "Selected.TFrame"
    )
    SausagePizzaFrame.configure(style = "Frame.TFrame")
    VeggiePizzaFrame.configure(style= "Frame.TFrame")
    MeatTrioFrame.configure(style = "Frame.TFrame")
    HawaiianPizzaFrame.configure(style = "Frame.TFrame")
    PeperoniPizzaFrame.configure(style = "Frame.TFrame")

    displayLabel.configure(
        image = CheesePizzaImage,
        text = "Cheese Pizza",
        font=('Helvetica', 20,"bold"),
        foreground="white",
        compound = "bottom",
        padding = (5, 5, 5, 5),
    )

# peperoni pizza button
def displayPeperoniPizza():
    PeperoniPizzaFrame.configure(
        relief = "sunken",
        style = "Selected.TFrame"
    )
    SausagePizzaFrame.configure(style="Frame.TFrame")
    VeggiePizzaFrame.configure(style="Frame.TFrame")
    MeatTrioFrame.configure(style="Frame.TFrame")
    HawaiianPizzaFrame.configure(style="Frame.TFrame")
    CheesePizzaFrame.configure(style="Frame.TFrame")
    displayLabel.configure(
        text = "Peperoni Pizza",
        font = ('Helvetica', 20,"bold"),
        foreground = "white",
        image = PeperoniPizzaImage,
        compound = "bottom",
        padding=(5, 5, 5, 5),
    )

# sausage pizza button
def displaySausagePizza():
    SausagePizzaFrame.configure(
        relief = "sunken",
        style="Selected.TFrame"
    )
    CheesePizzaFrame.configure(style="Frame.TFrame")
    VeggiePizzaFrame.configure(style="Frame.TFrame")
    MeatTrioFrame.configure(style="Frame.TFrame")
    HawaiianPizzaFrame.configure(style="Frame.TFrame")
    PeperoniPizzaFrame.configure(style="Frame.TFrame")
    displayLabel.configure(
        text = "Sausage Pizza",
        font=('Helvetica', 20,"bold"),
        foreground="white",
        image = SausagePizzaImage,
        compound = "bottom",
        padding=(5, 5, 5, 5),
    )

# hawaiian pizza button
def displayHawaiian():
    HawaiianPizzaFrame.configure(
        relief = "sunken",
        style="Selected.TFrame"
    )
    SausagePizzaFrame.configure(style="Frame.TFrame")
    VeggiePizzaFrame.configure(style="Frame.TFrame")
    MeatTrioFrame.configure(style="Frame.TFrame")
    CheesePizzaFrame.configure(style="Frame.TFrame")
    PeperoniPizzaFrame.configure(style="Frame.TFrame")
    displayLabel.configure(
        text = "Hawaiian Pizza",
        font=('Helvetica', 20,"bold"),
        foreground="white",
        image = HawaiianPizzaImage,
        compound = "bottom",
        padding=(5, 5, 5, 5),
    )


# veggie pizza button
def displayVeggiePizza():
    VeggiePizzaFrame.configure(
        relief = "sunken",
        style="Selected.TFrame"
    )
    SausagePizzaFrame.configure(style="Frame.TFrame")
    CheesePizzaFrame.configure(style="Frame.TFrame")
    MeatTrioFrame.configure(style="Frame.TFrame")
    HawaiianPizzaFrame.configure(style="Frame.TFrame")
    PeperoniPizzaFrame.configure(style="Frame.TFrame")
    displayLabel.configure(
        text = "Veggie Pizza",
        font=('Helvetica', 20,"bold"),
        foreground="white",
        image = VeggiePizzaImage,
        compound = "bottom",
        padding=(5, 5, 5, 5),
    )


# meat trio pizza button
def displayMeatTrio():
    MeatTrioFrame.configure(
        relief = "sunken",
        style="Selected.TFrame"
    )
    SausagePizzaFrame.configure(style="Frame.TFrame")
    VeggiePizzaFrame.configure(style="Frame.TFrame")
    CheesePizzaFrame.configure(style="Frame.TFrame")
    HawaiianPizzaFrame.configure(style="Frame.TFrame")
    PeperoniPizzaFrame.configure(style="Frame.TFrame")
    displayLabel.configure(
        image = MeatTrioImage,
        text = "MeatTrio Pizza",
        font=('Helvetica', 20,"bold"),
        foreground="white",
        compound = "bottom",
        padding=(5, 5, 5, 5),
    )



# genrate a reciept when you press the order button
def order():
    new_receipt = orderIDLabel.cget("text")
    new_receipt = new_receipt.replace("ORDER ID : ","")
    transaction_list = orderTransaction.cget("text").split("$ ")
    transaction_list.pop(len(transaction_list) - 1)

    order_day = date.today()
    order_time = datetime.now()

    for item in transaction_list:
        item += "$ "

    with open(new_receipt, 'w') as file:
        file.write("Pizza Pizza")
        file.write("\n")
        file.write("________________________________________________________")
        file.write("\n")
        file.write(order_day.strftime("%x"))
        file.write("\n")
        file.write(order_time.strftime("%X"))
        file.write("\n\n")
        for item in transaction_list:
            file.write(item + "\n")
        file.write("\n\n")
        file.write(orderTotalLabel.cget("text"))

    orderTotalLabel.configure(text = "TOTAL : 0$")
    orderIDLabel.configure(text = "ODER ID: " + ORDER_ID())
    orderTransaction.configure(text = "")


#----------------------------------styling------------------------------------#

# style for frames
s = ttk.Style()
s.configure('MainFrame.TFrame', background = "#222")
s.configure('MenuFrame.TFrame', background = "#444")
s.configure('DisplayFrame.TFrame', background = "#777")
s.configure('OrderFrame.TFrame', background = "#888")
s.configure('Frame.TFrame', background = "#999", relief = "raised")
s.configure('Selected.TFrame', background = "#eee")
s.configure('MenuLabel.TLabel',
            background = "#0F1110",
            font = ("Arial", 13, "italic"),
            foreground = "white",
            padding = (1, 1, 1, 1),
            width = 25
            )
s.configure('orderTotalLabel.TLabel',
            background = "#0F1110",
            font = ("Arial", 10, "bold"),
            foreground = "white",
            padding = (2, 2, 2, 2),
            anchor = "w"
            )
s.configure('orderTransaction.TLabel',
            background = "#4A4A48",
            font = ('Helvetica', 12),
            foreground = "white",
            wraplength = 125,
            anchor = "nw",
            padding = (3, 3, 3, 3)
            )


# images for the display
# logo image
LogoImageObject = Image.open("test/images/pizza_pizza_logo.png").resize((150, 150))
LogoImage = ImageTk.PhotoImage(LogoImageObject)

# Banner image
TopBannerImageObject = Image.open("test/images/banner.jpeg").resize((550, 150))
TopBannerImage = ImageTk.PhotoImage(TopBannerImageObject)

# Menu image
displayDefaultImageObject = Image.open("test/images/main_display.jpg").resize((550, 400))
displayDefaultImage = ImageTk.PhotoImage(displayDefaultImageObject)

CheesePizzaImageObject = Image.open("test/images/menu/cheese_pizza.jpeg").resize((550, 400))
CheesePizzaImage = ImageTk.PhotoImage(CheesePizzaImageObject)

PeperoniPizzaImageObject = Image.open("test/images/menu/peperoni.jpeg").resize((550, 400))
PeperoniPizzaImage = ImageTk.PhotoImage(PeperoniPizzaImageObject)

SausagePizzaImageObject = Image.open("test/images/menu/sausage_pizza.jpeg").resize((550, 400))
SausagePizzaImage = ImageTk.PhotoImage(SausagePizzaImageObject)

HawaiianPizzaImageObject = Image.open("test/images/menu/hawaiian.jpeg").resize((550, 400))
HawaiianPizzaImage = ImageTk.PhotoImage(HawaiianPizzaImageObject)

MeatTrioImageObject = Image.open("test/images/menu/meat_trio.jpeg").resize((550, 400))
MeatTrioImage = ImageTk.PhotoImage(MeatTrioImageObject)

VeggiePizzaImageObject = Image.open("test/images/menu/veggie_pizza.jpeg").resize((550, 400))
VeggiePizzaImage = ImageTk.PhotoImage(VeggiePizzaImageObject)



#-----------------------------------widgets-----------------------------------------------#


# main frames

mainFrame = ttk.Frame(root, width = 400, height = 800, style = 'MainFrame.TFrame')
mainFrame.grid(row = 0, column = 0, sticky = "NSEW")

topBannerFrame = ttk.Frame(mainFrame)
topBannerFrame.grid(row = 0, column = 0, sticky = "NSEW", columnspan = 3)

menuFrame = ttk.Frame(mainFrame, style = 'MenuFrame.TFrame')
menuFrame.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = "NSEW")

displayFrame = ttk.Frame(mainFrame, style = "DisplayFrame.TFrame")
displayFrame.grid(row = 4, column = 0, padx = 75, pady = 20, sticky = "NSEW")

orderFrame = ttk.Frame(mainFrame, style = "OrderFrame.TFrame")
orderFrame.grid(row = 5, column = 0, padx = 0, pady = 20, sticky = "NSEW")

#  display menu Frames
CheesePizzaFrame = ttk.Frame(menuFrame, style = "Frame.TFrame")
CheesePizzaFrame.grid(row = 1, column = 0, sticky = "NSEW")

PeperoniPizzaFrame = ttk.Frame(menuFrame,style ="Frame.TFrame")
PeperoniPizzaFrame.grid(row = 1, column = 1, sticky ="NSEW")

SausagePizzaFrame = ttk.Frame(menuFrame, style ="Frame.TFrame")
SausagePizzaFrame.grid(row = 2, column = 0, sticky ="NSEW")

HawaiianPizzaFrame = ttk.Frame(menuFrame, style ="Frame.TFrame")
HawaiianPizzaFrame.grid(row = 2, column = 1, sticky ="NSEW")

MeatTrioFrame = ttk.Frame(menuFrame, style ="Frame.TFrame")
MeatTrioFrame.grid(row = 3, column = 0, sticky ="NSEW")

VeggiePizzaFrame = ttk.Frame(menuFrame, style ="Frame.TFrame")
VeggiePizzaFrame.grid(row = 3, column = 1, sticky ="NSEW")


# banner and logo
LogoLabel = ttk.Label(topBannerFrame, image = LogoImage, background = "#0F1110")
LogoLabel.grid(row = 0, column = 0, sticky = "W")

bannerLabel = ttk.Label(topBannerFrame, image = TopBannerImage, background = "#0F1110")
bannerLabel.grid(row = 0, column = 1, sticky = "NSEW")


# menu labels
MainMenuLabel = ttk.Label(menuFrame, text = "MENU ITEMS", style = "MenuLabel.TLabel")
MainMenuLabel.grid(row = 0, column = 0, padx = 0, sticky = "E")
MainMenuLabel.configure(
    anchor= "w",
    font = ("sans-serif", 20, "bold")
)

CheesePizzaLabel = ttk.Label(CheesePizzaFrame, text ="Cheese Pizza - $10", style ="MenuLabel.TLabel")
CheesePizzaLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

PeperoniPizzaLabel = ttk.Label(PeperoniPizzaFrame, text ="Peperoni Pizza - $12", style ="MenuLabel.TLabel")
PeperoniPizzaLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

SausagePizzaLabel = ttk.Label(SausagePizzaFrame, text ="Sausage Pizza - $12", style ="MenuLabel.TLabel")
SausagePizzaLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

HawaiianPizzaLabel = ttk.Label(HawaiianPizzaFrame, text ="Hawaiian Pizza - $15", style ="MenuLabel.TLabel")
HawaiianPizzaLabel.grid(row = 0, column = 0, padx =10, pady = 10, sticky = "W")

MeatTrioLabel = ttk.Label(MeatTrioFrame, text ="MeatTrio Pizza - $15", style ="MenuLabel.TLabel")
MeatTrioLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

VeggiePizzaLabel = ttk.Label(VeggiePizzaFrame, text ="Veggie Pizza - $15", style ="MenuLabel.TLabel")
VeggiePizzaLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")



# menu Buttons
CheesePizzaDisplayButton = ttk.Button(CheesePizzaFrame, text ="Display", command = displayCheesePizza)
CheesePizzaDisplayButton.grid(row = 0, column = 1, pady = 10, padx = 5)

PeperoniPizzaDisplayButton = ttk.Button(PeperoniPizzaFrame, text ="Display", command = displayPeperoniPizza)
PeperoniPizzaDisplayButton.grid(row = 0, column = 1, pady = 10, padx = 5)

SausagePizzaDisplayButton = ttk.Button(SausagePizzaFrame, text ="Display", command = displaySausagePizza)
SausagePizzaDisplayButton.grid(row = 0, column = 1, pady = 10, padx = 5)

HawaiianPizzaDisplayButton = ttk.Button(HawaiianPizzaFrame, text ="Display", command = displayHawaiian)
HawaiianPizzaDisplayButton.grid(row = 0, column = 1, pady = 10, padx = 5)

MeatTrioDisplayButton = ttk.Button(MeatTrioFrame, text ="Display", command = displayMeatTrio)
MeatTrioDisplayButton.grid(row = 0, column = 1, pady = 10, padx = 5)

VeggiePizzaDisplayButton = ttk.Button(VeggiePizzaFrame, text ="Display", command = displayVeggiePizza)
VeggiePizzaDisplayButton.grid(row = 0, column = 1, pady = 10, padx = 5)


# order configuration
orderTitleLabel = ttk.Label(orderFrame, text = "ORDER")
orderTitleLabel.configure(
    foreground="white", background="black",
    font=("Helvetica", 14, "bold"), anchor = "center",
    padding = (5, 5, 5, 5),
)
orderTitleLabel.grid(row = 0, column = 0, sticky = "EW")

orderIDLabel = ttk.Label(orderFrame, text = "ORDER ID : " + ORDER_ID())
orderIDLabel.configure(
    background = "black",
    foreground = "white",
    font = ("Helvetica", 11, "italic"),
    anchor = "center",
)
orderIDLabel.grid(row = 1, column = 0, sticky = "EW", pady = 1)

orderTransaction = ttk.Label(orderFrame, style = 'orderTransaction.TLabel')
orderTransaction.grid(row = 2, column = 0, sticky = "NSEW")

orderTotalLabel = ttk.Label(orderFrame, text = "TOTAL : 0$", style = "orderTotalLabel.TLabel")
orderTotalLabel.grid(row = 3, column = 0, sticky = "EW")

orderButton = ttk.Button(orderFrame, text = "ORDER", command = order)
orderButton.grid(row = 4, column = 0, sticky = "EW")



# display 
displayLabel = ttk.Label(displayFrame, image = displayDefaultImage)
displayLabel.grid(row = 0, column = 0 , sticky = "NSEW", columnspan = 2)
displayLabel.configure(background = "#0F1110")

addOrderButton = ttk.Button(displayFrame, text = "ADD TO ORDER", command = add)
addOrderButton.grid(row = 1, column = 0, padx = 2, sticky = "NSEW")

removeOrderButton = ttk.Button(displayFrame, text = "REMOVE", command = remove)
removeOrderButton.grid(row = 1, column = 1, padx = 2, sticky = "NSEW")


#-----------------------------grid layout-------------------------------------------#
mainFrame.columnconfigure(2, weight = 1)
mainFrame.rowconfigure(1, weight = 1)
menuFrame.columnconfigure(0, weight = 1)
menuFrame.rowconfigure(1, weight = 1)
menuFrame.rowconfigure(2, weight = 1)
menuFrame.rowconfigure(3, weight = 1)
menuFrame.rowconfigure(4, weight = 1)
menuFrame.rowconfigure(5, weight = 1)
menuFrame.rowconfigure(6, weight = 1)
orderFrame.columnconfigure(0, weight = 1)
orderFrame.rowconfigure(2, weight = 1)



root.mainloop()