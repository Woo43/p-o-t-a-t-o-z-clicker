from tkinter import *
import random
clicker = Tk()
clicker.title("a very p o t a t o z clicker")
clicks = 0
rutabagas = 0
carrots = 0
spotatoz = 0
holypotato = 0
def reset():
    global clicks
    global rutabagas
    global carrots
    global spotatoz
    global holypotato
    clicks = 0
    rutabagas = 0
    carrots = 0
    spotatoz = 0
    holypotato = 0
def clickplus():
    global clicks
    global rutabagas
    global carrots
    global spotatoz
    global holypotato
    clicks = clicks + 1 + rutabagas + carrots + carrots + carrots + spotatoz + spotatoz + spotatoz + spotatoz + spotatoz + spotatoz + spotatoz + spotatoz + spotatoz + spotatoz
    clicker.title("You have " + str(clicks) + " potatoz.")
    if rutabagas > 0:
        clicker.title("You have " + str(clicks) + " potatoz, and " + str(rutabagas) + " rutabagas.")
    if carrots > 0:
        clicker.title("You have " + str(clicks) + " potatoz, " + str(rutabagas) + " rutabagas, and " + str(carrots) + " carrots.")
    if spotatoz > 0:
        clicker.title("You have " + str(clicks) + " potatoz, " + str(rutabagas) + " rutabagas, " + str(carrots) + " carrots, " + str(spotatoz) + " sweet potatoz.")
    if holypotato > 0:
        clicker.title("You won. You got the holy potato. Do something else now.")
#    print("Your potatoz: " + str(clicks))
    if clicks == 1:
        print("1 potato? If you think this is impressive, you have a long way to go.")
    if clicks == 10:
        print("10 potatoz? It's a start.")
    if clicks == 100:
        print("100 potatoz. Now you're starting to get somewhere.")
    if clicks == 1000:
        print("Go get yourself some chips and an autoclicker. You deserve it.")
    if clicks == 10000:
        print("Wow, 10,000 potatoz? You're almost as good as Beatlefan10. Almost.")
    if clicks == 100000:
        print("Ok, go do something else. I know you're in this window because the dev hasen't added passive potatoz yet.")
    if clicks == 1000000:
        print("Go home, eat a baked potato. You win.")
    if clicks == 1000000000:
        print("THERE. THE END. HAPPY? CLOSE THIS WINDOW.")
    if clicks == 1000000001:
        print("No, go do something productive.")
    if clicks == 1000000002:
        print("I'm warning you, don't push that button.")
    if clicks > 1000000002:
        print("I warned you.")
        clicker.destroy()
the_thing = Button(clicker, text="Generate Potatoz", command=clickplus)
the_thing.pack()
def openshop():
    shop = Toplevel()
    global clicks
    global rutabagas
    global carrots
    global spotatoz
    shop.title("Shop")
    def buyrutabaga():
        global clicks
        global rutabagas
        global carrots
        global spotatoz
        if clicks - 500 < 1:
            print("Sorry, you don't have enough potatoz.")
        else:
            print("Cool. A rutabaga.")
            clicks = clicks - 500
            rutabagas = rutabagas + 1
        clicker.title("You have " + str(clicks) + " potatoz.")

    rutabagabuy = Button(shop, text="Buy Rutabaga for 500 Potatoz", command=buyrutabaga)
    rutabagabuy.pack()
    def buycarrot():
        global clicks
        global rutabagas
        global carrots
        global spotatoz
        if clicks - 1000 < 1:
            print("Sorry, you don't have enough potatoz.")
        else:
            randcarrot = random.randint(1, 5)
            if randcarrot == 1:
                print("Cool. A carrot.")
            if randcarrot == 2:
                print("Cool. A yellow carrot.")
            if randcarrot == 3:
                print("Cool. A white carrot.")
            if randcarrot == 4:
                print("Cool. A purple carrot.")
            if randcarrot == 5:
                print("Cool. A red carrot.")
            clicks = clicks - 1000
            carrots = carrots + 1
    carrotbuy = Button(shop, text="Buy 1 carrot for 1,000 potatoz", command=buycarrot)
    carrotbuy.pack()
    def buyspotato():
        global clicks
        global spotatoz
        if clicks - 2000 < 1:
            print("Sorry, you don't have enough potatoz.")
        else:
            clicks = clicks - 2000
            spotatoz = spotatoz + 1
    spotatobuy = Button(shop, text="Buy 1 sweet potato for 2,000 potatoz.", command=buyspotato)
    spotatobuy.pack()
    def buyholypotato():
        global clicks
        global holypotato
        if clicks - 10000 < 1:
            print("Sorry, you don't have enough potatoz.")
        else:
            if holypotato < 0:
                print("There can only be one.")
            else:
                clicks = clicks - 10000
                holypotato = holypotato + 1
                print("You got the holy potato!")
    holypotatobuy = Button(shop, text="Buy the holy potato for 10000 potatoz.", command=buyholypotato)
    holypotatobuy.pack()
    if holypotato > 0:
        resetbutton = Button(shop, text="RESET GAME", command=reset)
        resetbutton.pack()
shopbutton = Button(clicker, text="Shop", command=openshop)
shopbutton.pack()
clicker.mainloop()