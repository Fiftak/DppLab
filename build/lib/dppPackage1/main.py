from Aplikacja.ListaZakupow import ListaZakupow
from Aplikacja.Uroczystosc import Uroczystosc
import os
from Aplikacja.Produkt import Produkt

if __name__ == "__main__":
    pl = ListaZakupow(Uroczystosc.Kolacja, 10, 15, 20)
    pl.generateList()
    pl.printAllProducts()
    script_dir = "../produkty.txt"  # <-- absolute dir the script is in

    pl.readProductsFromFile(script_dir)
    pl.printAllAviableProducts()