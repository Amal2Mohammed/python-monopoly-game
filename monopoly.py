
#from PIL import Image, ImageTk
from cmath import isnan
import json
from msilib.schema import ListBox
from tkinter import *
import tkinter
import pandas
import random
from tkinter import messagebox
import math
#import Players


class Game():
    def __init__(self, root, players=[], tiles=[], cards=[]):
        self.window = root
        self.window['bg'] = 'white'
        self.players = players
        self.tiles = tiles
        self.cards = cards
        self.p1Money = StringVar(root, value='0')
        self.p2Money = StringVar(root, value='0')
        self.p3Money = StringVar(root, value='0')
        self.p4Money = StringVar(root, value='0')

        self.l1 = Label(root, text='WELCOME TO Amal Aldhafeeri MONOPOLY', font=('Arial', 20, 'bold'), bg='yellow')
        self.l1.grid(column=0, row=0, columnspan=5, pady=10)



        # player1
        self.l2 = Label(root, text='Player 1 Money', font=('Arial', 16), fg='red', bg='white', height=1)
        self.l2.grid(column=1, row=1, padx=11)
        self.l2_cl2 = Entry(root, state='readonly', textvariable=self.p1Money, justify="center")
        self.l2_cl2.grid(column=1, row=2)
        
        # properties1
        self.properties1 = Label(root, text='Properties', font=('Arial', 14), bg='white')
        self.properties1.grid(column=1, row=3)

        self.pList1 = Listbox(root, justify="center")
        self.pList1.grid(column=1, row=4, sticky=NSEW, padx=2)


        # Cards1
        self.c1 = Label(root, text='Cards', font=('Arial', 14), bg='white')
        self.c1.grid(column=1, row=5)

        self.cList1 = Listbox(root, justify="center")
        self.cList1.grid(column=1, row=6, sticky=NSEW, padx=2)





        # player2 Money
        self.l3 = Label(root, text='Player 2 Money', font=('Arial', 16), fg='blue', bg='white', height=1)
        self.l3.grid(column=2, row=1, padx=11)
        self.l3_cl3 = Entry(root, state='readonly', textvariable=self.p2Money, justify="center")
        self.l3_cl3.grid(column=2, row=2)

        # properties2
        self.p2 = Label(root, text='Properties', font=('Arial', 14), bg='white')
        self.p2.grid(column=2, row=3)

        self.pList2 = Listbox(root, justify="center")
        self.pList2.grid(column=2, row=4, sticky=NSEW, padx=2)
        
        # Cards2
        self.c2 = Label(root, text='Cards', font=('Arial', 14), bg='white')
        self.c2.grid(column=2, row=5)

        self.cList2 = Listbox(root, justify="center")
        self.cList2.grid(column=2, row=6, sticky=NSEW, padx=2)
        



        # player3 MoneyS
        self.l4 = Label(root, text='Player 3 Money', font=('Arial', 16), fg='green', bg='white', height=1)
        self.l4.grid(column=3, row=1, padx=11)
        self.l4_cl4 = Entry(root, state='readonly', textvariable=self.p3Money, justify="center")
        self.l4_cl4.grid(column=3, row=2)

        # properties3
        self.p3 = Label(root, text='Properties', font=('Arial', 14), bg='white')
        self.p3.grid(column=3, row=3)

        self.pList3 = Listbox(root, justify="center")
        self.pList3.grid(column=3, row=4, sticky=NSEW, padx=2)
        
        # Cards3
        self.c3 = Label(root, text='Cards', font=('Arial', 14), bg='white')
        self.c3.grid(column=3, row=5)

        self.cList3 = Listbox(root, justify="center")
        self.cList3.grid(column=3, row=6, sticky=NSEW, padx=2)




        # player Money4
        self.l5 = Label(root, text='Player 4 Money', font=('Arial', 16), fg='orange', bg='white', height=1)
        self.l5.grid(column=4, row=1, padx=11)
        self.l5_cl5 = Entry(root, state='readonly', textvariable=self.p4Money, justify="center")
        self.l5_cl5.grid(column=4, row=2)

        # properties4
        self.p4 = Label(root, text='Properties', font=('Arial', 14), bg='white')
        self.p4.grid(column=4, row=3)

        self.pList4 = Listbox(root, justify="center")
        self.pList4.grid(column=4, row=4, sticky=NSEW, padx=2)

        # Cards4
        self.c4 = Label(root, text='Cards', font=('Arial', 14), bg='white')
        self.c4.grid(column=4, row=5)

        self.cList4 = Listbox(root, justify="center")
        self.cList4.grid(column=4, row=6, sticky=NSEW, padx=2)







        # image
        self.canv = Canvas(root, bg='white', width=600, height=600)
        self.img = PhotoImage(file="monopoly_board2.png")
        self.image_object = self.canv.create_image(300, 300, image=self.img)
        self.canv.grid(row=2, column=0, rowspan=7)

        buttonRow = 8

        # button1
        self.rollDiceBtn = Button(root, text='Roll Dice', command=self.Roll_dice, fg='blue', height=3, width=10, border=7)
        self.rollDiceBtn.grid(row=buttonRow, column=1)
        # button2
        self.buyPropertyBtn = Button(root, text='Buy Property', command=self.Buy_Properties, height=3, width=10, border=7, fg='blue')
        self.buyPropertyBtn.grid(row=buttonRow, column=2)
        # button3
        self.buildHousesBtn = Button(root, text='Build Houses', height=3, width=10, border=7, fg='blue')
        self.buildHousesBtn.grid(row=buttonRow, column=3)
        # button4
        self.endTurnBtn = Button(root, text="End Turn", command=self.End_Turn, height=3, width=10, border=7, fg='blue')
        self.endTurnBtn.grid(row=buttonRow, column=4)





        self.turn = 0

        self.turnLabel = Label(root, text="Player 1 turn", font=('Arial', 16), bg='white', foreground='#78281F')
        self.turnLabel.grid(row=7, column=1, columnspan=4)

        self.statusLabel = Label(root, text= "", font=('Arial', 12), bg='white', foreground='#424949')
        self.statusLabel.grid(row=9, column=1, columnspan=4, pady=10)







        self.df1 = pandas.read_csv('monopoly_tiles.csv')
        self.df1.head()
        self.tiles_count = 40
        self.tiles = []
        for index, row in self.df1.iterrows():
            self.tiles.append(Tiles(row))

        self.df2 = pandas.read_csv('community.csv')
        self.df2.head()
        self.community_count = 16
        self.community = []
        for index, row in self.df2.iterrows():
            self.community.append(Cards(row))

        self.df3 = pandas.read_csv('chance.csv')
        self.df3.head()
        self.chance_count = 16
        self.chance = []
        for index, row in self.df3.iterrows():
            self.chance.append(Cards(row))

        ##########################################################################################
        # players
        self.players = []
        self.shift = [(-15, -20), (5, -20), (-15, 0), (5, 0)]
        self.color = ['red', 'blue', 'green', 'orange']
        self.size = 20
        self.totalDoubles = 0
        
        for i in range(4):
            x = self.tiles[0].x
            y = self.tiles[0].y
            x1 = x + self.shift[i][0]
            y1 = y + self.shift[i][1]
            x2 = x1 + self.size
            y2 = y1 + self.size
            c = self.canv.create_oval(x1, y1, x2, y2, fill=self.color[i])
            p = Player(self, i, self.color[i], self.shift[i][0], self.shift[i][1], c)
            self.players.append(p)

        ###########################################################################################

        self.buyPropertyBtn.config(state="disabled")
        self.buildHousesBtn.config(state="disabled")
        self.endTurnBtn.config(state="disabled")

        self.showAllAsets()
        self.window.mainloop()

        
        

        # Functions


    def showAllAsets(self):
        #Show money
        self.p1Money.set(self.players[0].getMoney())
        self.p2Money.set(self.players[1].getMoney())
        self.p3Money.set(self.players[2].getMoney())
        self.p4Money.set(self.players[3].getMoney())

        #Show properties
        self.pList1.delete(0,END)
        for pro in self.players[0].properties:
            self.pList1.insert(END, pro.name)

        self.pList2.delete(0,END)
        for pro in self.players[1].properties:
            self.pList2.insert(END, pro.name)

        self.pList3.delete(0,END)
        for pro in self.players[2].properties:
            self.pList3.insert(END, pro.name)

        self.pList4.delete(0,END)
        for pro in self.players[3].properties:
            self.pList4.insert(END, pro.name)

        
        #Show cards
        self.cList1.delete(0,END)
        for pro in self.players[0].cards:
            self.cList1.insert(END, pro.name)

        self.cList2.delete(0,END)
        for pro in self.players[1].cards:
            self.cList2.insert(END, pro.name)

        self.cList3.delete(0,END)
        for pro in self.players[2].cards:
            self.cList3.insert(END, pro.name)

        self.cList4.delete(0,END)
        for pro in self.players[3].cards:
            self.cList4.insert(END, pro.name)


        


    def move_plus(self, sum):
        self.players[self.turn].position += sum
        if self.players[self.turn].position > 39:
            self.players[self.turn].position %= 40
            self.players[self.turn].rec(200)

        x = self.tiles[self.players[self.turn].position].x
        y = self.tiles[self.players[self.turn].position].y
        x1 = x + self.shift[self.turn][0]
        y1 = y + self.shift[self.turn][1]
        x2 = x1 + self.size
        y2 = y1 + self.size
        self.canv.delete(self.players[self.turn].circle)
        c = self.canv.create_oval(x1, y1, x2, y2, fill=self.color[self.turn])
        self.players[self.turn].circle = c

    def Go_to_gail(self):
        self.players[self.turn].jail = 3
        self.move(10, plus=False)
        self.showMsg("Player " + str(self.turn+1) + " sent to jail")


    def move(self, dest, plus=True):
        if self.players[self.turn].position > dest and plus:
            self.players[self.turn].position = dest
            self.players[self.turn].rec(200)
        self.players[self.turn].position = dest

        x = self.tiles[self.players[self.turn].position].x
        y = self.tiles[self.players[self.turn].position].y
        x1 = x + self.shift[self.turn][0]
        y1 = y + self.shift[self.turn][1]
        x2 = x1 + self.size
        y2 = y1 + self.size
        self.canv.delete(self.players[self.turn].circle)
        c = self.canv.create_oval(x1, y1, x2, y2, fill=self.color[self.turn])
        self.players[self.turn].circle = c

    def draw(self, type):
        if type == 'chance':
            return random.choice(self.chance)
        else:
            return random.choice(self.community)




    def Roll_dice(self):
        print("Rolling Dice")
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        # dice1 = 1
        # dice2 = 3

        print("Dice 1: " + str(dice1))
        print("Dice 2: " + str(dice2))

        sum = dice1 + dice2

        if self.players[self.turn].jail == 0:
            self.move_plus(sum)

        currPlayer = self.players[self.turn]
        currTile = self.tiles[currPlayer.position]
        self.showMsg("Player " + str(self.turn+1) + " advanced to " + currTile.name)


        if dice1 == dice2:
            self.double = True
            self.totalDoubles += 1
            messagebox.showinfo(message="Your rolled double (Total Double: "+ str(self.totalDoubles) +")")

            if self.totalDoubles == 3:
                messagebox.showinfo(message="You have been sent to the jail")
                self.rollDiceBtn.config(state="disabled")
                self.buyPropertyBtn.config(state="disabled")
                self.buildHousesBtn.config(state="active")
                self.endTurnBtn.config(state="active")

                self.Go_to_jail()
                return

                #######################################################################

                # jail[10]

                #######################################################################

            else:
                self.rollDiceBtn.config(state="active")
                self.buyPropertyBtn.config(state="active")
                self.buildHousesBtn.config(state="active")
                self.endTurnBtn.config(state="disabled")

        else:
            self.double = False
            self.totalDoubles = 0
            self.endTurnBtn.config(state="active")
            self.rollDiceBtn.config(state="disabled")
            

        tile = self.tiles[self.players[self.turn].position]
        owned = False

        if tile.tile_type == "property":
            currPlayer = self.players[self.turn]
            currTile = self.tiles[currPlayer.position]

            for player in self.players:
                if player is self.players[self.turn]:
                    pass
                elif player.playing == False:
                    pass
                else:
                    if tile in player.properties:
                        amount = self.players[self.turn].pay(int(tile.rent[tile.houses]))
                        player.rec(amount)
                        owned = True
                        self.showMsg("Player " + str(self.turn+1) + " payed " + str(currTile.cost) + " Rent")

            if not owned:
                self.buyPropertyBtn.config(state="active")
                self.buildHousesBtn.config(state="disabled")
                self.endTurnBtn.config(state="active")

        elif tile.tile_type == "station":
            currPlayer = self.players[self.turn]
            currTile = self.tiles[currPlayer.position]
            for player in self.players:
                if player is self.players[self.turn]:
                    pass
                elif player.playing == False:
                    pass
                else:
                    if tile in player.properties:
                        count = len(player.properties)
                        amount = [25, 50, 100, 200]
                        self.amount = self.players[self.turn].pay(amount[count - 1])
                        player.rec(self.amount)
                        self.showMsg("Player " + str(self.turn+1) + " payed " + str(currTile.cost) + " to " + currTile.name)
                        owned = True

            if not owned:
                self.buyPropertyBtn.config(state="active")


        elif tile.tile_type == "utility":
            currPlayer = self.players[self.turn]
            currTile = self.tiles[currPlayer.position]

            for player in self.players:
                if player is self.players[self.turn]:
                    pass

                elif player.playing == False:
                    pass

                else:
                    if tile in player.properties:
                        sum = currTile.cost

                        countUtilities = 0
                        for pro in player.properties:
                            if pro.tile_type == 'utility':
                                countUtilities = countUtilities + 1

                        if countUtilities == 1:
                            amount = sum * 4
                        else:
                            amount = sum * 10


                        self.amount = self.players[self.turn].pay(amount)
                        player.rec(self.amount)
                        self.showMsg("Player " + str(self.turn+1) + " payed " + str(currTile.cost) + " to " + currTile.name)
                        owned = True

            if not owned:
                self.buyPropertyBtn.config(state="active")



        elif tile.tile_type == 'move':
            if currTile.position == 30:
                self.Go_to_gail()


        elif tile.tile_type == 'chance':
            chance = self.draw("chance")
            messagebox.showinfo(title= "Chance Card",message=chance.text)
            if chance.action == "move":
                self.move(int(chance.value), plus=False)
            elif chance.action == "move+":
                self.move(int(chance.value))
            elif chance.action == "back":
                self.move(-1 * int(chance.value), plus=True)
            elif chance.action == "pay":
                self.players[self.turn].pay(int(chance.value))
            elif chance.action == "receive":
                self.players[self.turn].rec(int(chance.value))
            elif chance.action == "jail card":
                self.players[self.turn].cards.append(chance)

            self.buyPropertyBtn.config(state="disabled")
            self.buildHousesBtn.config(state="normal")
            self.endTurnBtn.config(state="normal")



        elif tile.tile_type == 'jail':
            self.buyPropertyBtn.config(state="disabled")
            self.buildHousesBtn.config(state="normal")
            self.endTurnBtn.config(state="normal")

        elif tile.tile_type == 'pay':
            currPlayer = self.players[self.turn]
            currTile = self.tiles[currPlayer.position]
            
            currPlayer.pay(currTile.cost)
            self.showMsg("Player " + str(self.turn+1) + " payed " + str(currTile.cost) + " " + currTile.name)
            self.buyPropertyBtn.config(state="disabled")
            self.buildHousesBtn.config(state="normal")
            self.endTurnBtn.config(state="normal")

        elif tile.tile_type == 'community chest':
            chance = self.draw("community")
            messagebox.showinfo(title= "Chance Card",message=chance.text)
            if chance.action == "move":
                self.move(int(chance.value), plus=False)
            elif chance.action == "move+":
                self.move(int(chance.value))
            elif chance.action == "back":
                self.move(-1 * int(chance.value), plus=True)
            elif chance.action == "pay":
                self.players[self.turn].pay(int(chance.value))
            elif chance.action == "receive":
                self.players[self.turn].rec(int(chance.value))
            elif chance.action == "jail card":
                self.players[self.turn].cards.append(chance)

            self.buyPropertyBtn.config(state="disabled")
            self.buildHousesBtn.config(state="normal")
            self.endTurnBtn.config(state="normal")

        #show everything
        self.showAllAsets()




    def Buy_Properties(self) :
        currPlayer = self.players[self.turn]
        currTile = self.tiles[currPlayer.position]

        if currTile in currPlayer.properties:
            pass

        elif currPlayer.getMoney() >= currTile.cost:
            currPlayer.properties.append(currTile)
            self.amount = currPlayer.pay(currTile.cost)
            self.showAllAsets()
            self.buyPropertyBtn.config(state="disabled")
            self.buildHousesBtn.config(state="normal")
            self.statusLabel.configure(text= "Player " + str(self.turn+1) + " bought " + currTile.name + " for " + str(self.amount))


    def End_Turn(self):
        self.turn = (self.turn + 1) % len(self.players)

        self.turnLabel.configure(text= "Player " + str(self.turn + 1 ) + " turn")

        self.rollDiceBtn.config(state="active")
        self.buyPropertyBtn.config(state="disabled")
        self.buildHousesBtn.config(state="active")
        self.endTurnBtn.config(state="disabled")
        print(self.turn)


    


    def showMsg(self, msg):
        self.statusLabel.configure(text= msg)


    ####################################################################################################################


class Player:
    def __init__(self, game, i, color, shift_x, shift_y, circle):
        self.game = game
        self.i = i
        self.properties = []
        self.position = 0
        self.cards = []
        self.jail = 0
        self.__money = 1500
        self.jail_cards = 0
        self.playing = True
        self.color = []
        self.shift_x = shift_x
        self.shift_y = shift_y
        self.circle = circle
        self.color = color

    def pay(self, amount):
        print("Paying... ", amount)
        if amount > self.__money:
            amount = self.__money
            self.__money = -1
            self.playing = False
            self.properties = []
        else:
            self.__money -= amount
        return amount

    def rec(self, amount):
        self.__money += amount

    def getMoney(self):
        return self.__money



# def Go_to_gail(self):
# self.players[self.turn].jail = 3
# self.move(10,plus=False)


##############################################################################################
class Tiles():
    def __init__(self, row):
        self.position = row['position']
        self.tile_type = row['tile_type']
        self.cost = row['cost']

        try:
            self.rent = json.loads(row['rent'])
        except:
            pass
            

        self.color = row['color']
        self.name = row['name']
        self.house_price = row['house_price']
        self.x = row['x']
        self.y = row['y']
        self.houses = 0


#######################################################################################
class Cards():
    def __init__(self, row):
        self.text = row['text']
        self.action = row['action']
        self.value = row['value']


#########################################################################################
#from PIL import Image, ImageTk

root = Tk()
root.title('Monopoly')
root.geometry('1320x800')



game = Game(root)
money = 1000
bank = 50000
root.mainloop()
