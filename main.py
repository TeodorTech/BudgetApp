
class Food:
    ledger = list()
    def deposit(self):
       descriere = input("Deposit in Food")
       ammount = int(input("Ammount deposited"))
       tabel = [descriere,ammount]
       d.ledger.append(tabel)

    def withdrawl(self):
        self.description = input("For what you withdrawl?")
        self.withdraw = -int(input("withdraw ammount"))
        lista =[self.description,self.withdraw]
        d.ledger.append(lista)
        #print(d.ledger[1])


    def transfer(self):
        category = input("Transfer from Food to")
        if category == " Investments":
            depunere= input("ammount")
            lista2 = ["Transfer to",category]
            lista3 = [lista2[0]+lista2[1],-int(depunere)]
            d.ledger.append(lista3)
            translist = ["Transfer from Food",depunere]
            Id.ledger.append(translist)
        else:
            depunere = input("ammount")
            lista2 = ["Transfer to", category]
            lista3 = [lista2[0] + lista2[1], -int(depunere)]
            d.ledger.append(lista3)
            translist = ["Transfer from Food", depunere]
            Hd.ledger.append(translist)

    def get_balance(self):
        self.balance = d.ledger[1]-w.withdraw
        print("current balance=",self.balance)
    def check_funds(self):
        check = int(input("check ammount?"))
        if check < b.balance:
            print("You have money")
        else: print("esti sarac")


class Investments:
    ledger = list()

    def deposit(self):
        descriere = input("Deposit in investments")
        ammount = int(input("Ammount deposited"))
        tabel = [descriere, ammount]
        Id.ledger.append(tabel)

    def withdrawl(self):
        self.description = input("For what you withdrawl?")
        self.withdraw = -int(input("Ammount of withdraw"))
        lista = [self.description, self.withdraw]
        # d.ledger.append(self.description)
        # d.ledger.append(self.withdraw)
        # self.ledger = [self.description,self.withdraw]
        Id.ledger.append(lista)

    def transfer(self):
        category = input("Transfer form Investments to")
        if category ==" House":
            depunere = input(" deposit ammount")
            lista2 = ["Transfer to", category]
            lista3 = [lista2[0] + lista2[1], -int(depunere)]
            Id.ledger.append(lista3)
            translist = ["Transfer from Investments", depunere]
            Hd.ledger.append(translist)
        else:
            depunere = input("ammount")
            lista2 = ["Transfer to", category]
            lista3 = [lista2[0] + lista2[1], -int(depunere)]
            Id.ledger.append(lista3)
            translist = ["Transfer from Investments", depunere]
            d.ledger.append(translist)

class House:
    ledger = list()

    def deposit(self):
        descriere = input("Deposit in House")
        ammount = int(input("Ammount deposited"))
        tabel = [descriere, ammount]
        Hd.ledger.append(tabel)

    def withdrawl(self):
        self.description = input("For what you withdrawl?")
        self.withdraw = -int(input("ammount of withdraw"))
        lista = [self.description, self.withdraw]
        # d.ledger.append(self.description)
        # d.ledger.append(self.withdraw)
        # self.ledger = [self.description,self.withdraw]
        Hd.ledger.append(lista)

    def transfer(self):
        category = input("Transfer from House to")
        if category == "investments":
            depunere = input(" deposit ammount")
            lista2 = ["Transfer to", category]
            lista3 = [lista2[0] + lista2[1], -int(depunere)]
            Hd.ledger.append(lista3)
            translist = ["Transfer from House", depunere]
            Id.ledger.append(translist)
        else:
            depunere = input(" deposit ammount")
            lista2 = ["Transfer to", category]
            lista3 = [lista2[0] + lista2[1], -int(depunere)]
            Hd.ledger.append(lista3)
            translist = ["Transfer from House", depunere]
            d.ledger.append(translist)

x = "Food"

d= Food()
d.deposit()
Id = Investments()
Id.deposit()
Hd = House()
Hd.deposit()
w = Food()
w.withdrawl()
#w.withdrawl()
t = Food()
t.transfer()

print("*"*int(((30-int(len(x)))/2)),x,"*"*int((30-int(len(x)))/2))
for i in d.ledger:
    a = i[0]
    b = str(i[1])
    l = int(30 - len(a))
    print(a,b.rjust(l))

Id = Investments()
Id.deposit()
Iw = Investments()
Iw.withdrawl()
It = Investments()
It.transfer()
y = "Investments"
print("*"*int(((30-int(len(y)))/2)),y,"*"*int((30-int(len(y)))/2))
for i in Id.ledger:
    a = i[0]
    b = str(i[1])
    l = int(30 - len(a))
    print(a,b.rjust(l))

z = "House"
print("*"*int(((30-int(len(z)))/2)),z,"*"*int((30-int(len(z)))/2))
for i in Hd.ledger:
    a = i[0]
    b = str(i[1])
    l = int(30 - len(a))
    print(a,b.rjust(l))









