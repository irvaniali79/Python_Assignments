from Alidb import *
from validator import *

class Store:
    
    query=None
    cart=[]
    total_cost=0

    def setproduct():
        product={}

        product['name']=input('name: ')
        product['price']=Cinput.getpostive("enter price: ")
        product['entity']=Cinput.getpostive("enter entity: ")

        return product

    def show(arr):
        if not isinstance(arr,list):arr=[arr]
        for item in arr:
            print(item)
        return arr

    def __init__(self,columns,address):
        self.columns=columns
        self.query=Query(Connection(address),self.columns)

    def add(self):
        self.query.insert(self.setproduct())

    def edit(self):
        self.show(self.query.todictionary(self.query.select(),columns))
        self.query.update(Cinput.getpostive("please choose id from list : \n"),self.setproduct())

    def delete(self):
        self.show(self.query.todictionary(self.query.select(),columns))
        self.query.delete(Cinput.getpostive("please choose id from list : \n"))
    def show_list(self):
        self.show(self.query.todictionary(self.query.select(),columns))
    def search(self):

        arr=['search by:','1.id','2.price','3.entity','4.name']
        self.show(arr)
        x=Cinput.getconstrainedint(0,5,"please choose number from list : \n")
        value= Cinput.getpostive('enter your numeric value: ') if 0<x<4 else Cinput.getstr('enter name : ') 
            
        self.show(self.query.todictionary(self.query.select(value,arr[x][2:]),columns))
    


    def buy(self):
        products=self.show(self.query.todictionary(self.query.select(),columns))
        x=Cinput.getconstrainedint(0,len(products)+1,"please choose id from list : \n")
        product=dict(products[x])
        product['entity']=Cinput.getconstrainedint(0,products['entity']+1,"enter your number that you have from this product: ")
        self.cart.append(products[x])
        self.show(self.cart)
        self.total_cost+=product['entity']*product['price']
        print('total price',self.total_cost)

    def exit():
        exit(0)