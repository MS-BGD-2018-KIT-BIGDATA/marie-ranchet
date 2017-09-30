import requests
from bs4 import BeautifulSoup

urlDell = 'https://www.cdiscount.com/search/10/dell.html#_his_'
urlAcer = 'https://www.cdiscount.com/search/10/acer.html#_his_'

def getSoupFromURL(url, method='get', data={}):
    res = None
    if method == 'get':
        res = requests.get(url)
    elif method == 'post':
        res = requests.post(url, data=data)
    else:
        return None

    if res.status_code == 200:
        soup = BeautifulSoup(res.text, 'html.parser')
        return soup
    else:
        return None

def getMeanDiscountFromBrand(url):

    mylist = []
    soup = getSoupFromURL(url)

    if soup:
        # parcourir tous les produits de la page :
        products = soup.find_all(class_="prdtBloc")
        for p in products:

            # chercher les prix ancien/nouveau, pour chaque produit
            prices = p.find_all(class_="prdtBZPrice")

            for el in prices:

                # récupérer l'ancien prix
                oldPrice = el.find(class_="prdtPrSt")
                if (oldPrice != None) :
                    oldPrice=oldPrice.get_text()
                else:
                    oldPrice = ""

                # récupérer le nouveau prix
                newPrice = el.find(class_="prdtPrice")
                if (newPrice != None):
                    newPrice = newPrice.get_text()
                else:
                    newPrice = el.find(class_="price")
                    if newPrice != None:
                        newPrice = newPrice.get_text()

                # remplacer , par . et € par .
                oldPrice = oldPrice.replace(",",".")
                oldPrice = oldPrice.replace("€",".")
                newPrice = newPrice.replace("€",".")

                # traiter le cas ou pas de oldPrice
                if (oldPrice == None or oldPrice == ""):
                    oldPrice = newPrice
                mylist.append(-(float(newPrice)-float(oldPrice))/float(oldPrice) * 100)

        #renvoyer la moyenne des réductions
        return sum(mylist)/len(mylist)


#### MAIN
discountAcer = getMeanDiscountFromBrand(urlAcer)
discountDell = getMeanDiscountFromBrand(urlDell)

if (discountAcer > discountDell):
    print("Buy Acer ! Discount : {:.2f}% compared to {:.2f}% at Dell".format(discountAcer, discountDell))
else:
    print("Buy Dell ! Discount : {:.2f}% compared to {:.2f}% at Acer".format(discountDell, discountAcer))
