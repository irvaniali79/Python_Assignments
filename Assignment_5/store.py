from Alidb import *
from validator import *

query=Query(Connection('datastore.csv'))


def setproduct():
    product={}

    product['name']=input('name: ')
    product['price']=Cinput.getpostive("enter price: ")
    product['entity']=Cinput.getpostive("enter entity: ")

    return product

def show(arr):
    for item in arr:
        print(item)
    return arr

cart=[]
total_cost=0
while True:

    print(" Welcome to my store: ")
    print(" 1.add ")
    print(" 2.edit ")
    print(" 3.delete ")
    print(" 4.show List ")
    print(" 5.search ")
    print(" 6.buy ")
    print(" 7.exit ")

    x = int (input("please choose from menu : \n"))
    if x == 1:
        query.insert(setproduct())
    elif x == 2:
        show(query.todictionary(query.select()))
        query.update(Cinput.getpostive("please choose id from list : \n"),setproduct())
    elif x == 3:
        query.delete(Cinput.getpostive("please choose id from list : \n"))
    elif x == 4:
        show(query.todictionary(query.select()))
    elif x == 5:
        arr=['search by:','1.id','2.price','3.entity','4.name']
        show(arr)
        x=Cinput.getconstrainedint(0,5,"please choose number from list : \n")
        value= Cinput.getpostive('enter your numeric value: ') if 0<x<4 else Cinput.getstr('enter name : ') 
            
        show(query.todictionary(query.select(value,arr[x][2:])))

    elif x == 6:
        products=show(query.todictionary(query.select()))
        x=Cinput.getconstrainedint(0,len(products)+1,"please choose id from list : \n")
        product=dict(products[x])
        product['entity']=Cinput.getconstrainedint(0,products['entity']+1,"enter your number that you have from this product: ")
        cart.append(products[x])
        show(cart)
        total_cost+=product['entity']*product['price']
        print('total price',total_cost)
    elif x == 7:
        exit(0)





    




