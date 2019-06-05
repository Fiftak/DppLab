from array import array
import numpy as np
from Aplikacja.Produkt import Produkt
from Aplikacja.Uroczystosc import Uroczystosc

def printFileName():
    print("PurchaseList")

class ListaZakupow():
    event=None,
    products = [],
    avaiableProducts=[],
    toddlers=0,
    kids=0,
    adults=0

    def __init__(self,event,toddlers,kids,adults):
        self.event=event
        self.toddlers=toddlers
        self.kids=kids
        self.adults=adults
        self.products= []
        self.avaiableProducts=[]


    def generateList(self):
        if self.event==Uroczystosc.Kolacja:
            self.products.append(Produkt("Ser", (0.1*self.toddlers+0.1*self.kids+0.6*self.adults+0.1),(0.1*self.toddlers+0.1*self.kids+0.2*self.adults+0.1)*7.15))
            self.products.append(Produkt("Wedlina", 0.1 * self.toddlers + 0.2 * self.kids + 0.3 * self.adults + 0.1,(0.1 * self.toddlers + 0.2 * self.kids + 0.3 * self.adults + 0.1) * 5.17));
            self.products.append(Produkt("Bulki", (int)(2 + self.toddlers + 0.5 * self.kids + 0.6 * self.adults),(int)(2 * self.toddlers + 0.5 * self.kids + 0.6 * self.adults + 0.7) * 0.99));
            self.products.append(Produkt("Parowki(4-sztuki)", (int)(1 + (self.toddlers + self.kids) * 0.2 + 0.3 * self.adults),(int)(1 + (self.toddlers + self.kids) * 0.2 + 0.3 * self.adults) * 2.87));
            self.products.append(Produkt("Sok grejfrutowy", (int)(1 + (self.toddlers + self.kids) * 0.3 + 0.15 * self.adults),(int)(1 + (self.toddlers + self.kids) * 0.3 + 0.15 * self.adults) * 4.87))
        elif self.event==Uroczystosc.Gril:
            self.products.append(Produkt("Ziemniaki", 0.2*self.toddlers+0.3*self.kids+0.4*self.adults+0.3,(0.2*self.toddlers+0.3*self.kids+0.4*self.adults+0.3)*1.79))
            self.products.append(Produkt("Ogorki",0.1*self.toddlers+0.2*self.kids+0.4*self.adults+0.15,(0.1*self.toddlers+0.2*self.kids+0.4*self.adults+0.15)*6.29))
            self.products.append(Produkt("Schab", (0.2 + self.toddlers * 0.1 + 0.15 * self.kids + 0.25 * self.adults),(0.2 + self.toddlers * 0.1 + 0.15 * self.kids + 0.25 * self.adults) * 15.23))
            self.products.append(Produkt("Cebula", (0.1 + self.toddlers * 0.15 + 0.18 * self.kids + 0.23 * self.adults), (0.1 + self.toddlers * 0.15 + 0.18 * self.kids + 0.23 * self.adults) * 3.23))
            self.products.append(Produkt("Smietana", (int)(1 + (self.toddlers + self.kids + self.adults) * 0.2),(int)(1 + (self.toddlers + self.kids + self.adults) * 0.2) * 4.05))
        elif self.event == Uroczystosc.Uroczysty_Obiad:
            self.products.append(Produkt("Paluszki", (int)(1 + 0.1 * self.toddlers + 0.12 * self.kids + 0.25 * self.adults),(int)(1 + 0.1 * self.toddlers + 0.12 * self.kids + 0.25 * self.adults) * 3.99));
            self.products.append(Produkt("Ciastka", 0.3 + 0.2 * self.kids + 0.2 * self.adults, (0.3 + 0.2 * self.kids + 0.2 * self.adults) * 3.45));
            self.products.append(Produkt("Owoce", (0.5 + 0.2 * self.toddlers + 0.35 * self.kids + 0.40 * self.adults),(0.5 + 0.2 * self.toddlers + 0.35 * self.kids + 0.40 * self.adults) * 4.99));
            self.products.append(Produkt("Cola", (int)(1 + self.kids * 0.4 + 0.3 * self.adults), (int)(1 + self.kids * 0.4 + 0.3 * self.adults) * 5.00));
            self.products.append(Produkt("Sok pomaranczowy", (int)(1 + self.toddlers * 0.3 + 0.2 * self.adults),(int)(1 + self.toddlers * 0.3 + 0.2 * self.adults * 6.12)))
        elif self.event == Uroczystosc.Wesele:
            self.products.append(Produkt("Paluszki", (int)(1 + 0.1 * self.toddlers + 0.12 * self.kids + 0.25 * self.adults),(int)(1 + 0.1 * self.toddlers + 0.12 * self.kids + 0.25 * self.adults) * 3.99))
            self.products.append(Produkt("Ciastka", 0.3 + 0.2 * self.kids + 0.2 * self.adults, (0.3 + 0.2 * self.kids + 0.2 * self.adults) * 3.45));
            self.products.append(Produkt("Owoce", (0.5 + 0.2 * self.toddlers + 0.35 * self.kids + 0.40 * self.adults),(0.5 + 0.2 * self.toddlers + 0.35 * self.kids + 0.40 * self.adults) * 4.99));
            self.products.append(Produkt("Cola", (int)(1 + self.kids * 0.4 + 0.3 * self.adults), (int)(1 + self.kids * 0.4 + 0.3 * self.adults) * 5.00));
            self.products.append(Produkt("Sok pomaranczowy", (int)(1 + self.toddlers * 0.3 + 0.2 * self.adults),(int)(1 + self.toddlers * 0.3 + 0.2 * self.adults * 6.12)));

    def addProductToCatalog(self,data):
        self.avaiableProducts.append(data)

    def printAllProducts(self):
        for product in self.products:
            product.printProduct()

    def printAllAviableProducts(self):
        print("Pro:")
        for product in self.avaiableProducts:
            product.printProduct()

    def readProductsFromFile(self,path):
        file = open("../produkty.txt",'r')
        #file.write("aaaaa1213131")
        i=0;
        name=None
        value=1
        weight=1
        for x in file:
            i = i + 1
            print(x)
            if(i %4==1):
                print(i)
                print("name "+x)
                name=x
            elif i%4==3:
                print(i)
                print("value " + x)
                value=x
        if (value!=1 and name!=None):
            produkt=Produkt(name,weight,value)
            self.avaiableProducts.append(produkt)
            value=1
            name=None
        file.close()
