from Alidb import *
from helper import *

class Store:
    
    query=None
    cart=[]
    total_cost=0

    def __init__(self,columns,address):
        self.columns=columns
        self.query=Query(Connection(address),self.columns)

    def setproduct(self):
        product={}

        product['name']=input('name: ')
        product['price']=Cinput.getpostive("enter price: ")
        product['entity']=Cinput.getpostive("enter entity: ")

        return product

    def show(self,arr,start=None):
        if not isinstance(arr,list):arr=[arr]
        for item in arr:
            if start!=None:print(str(start)+"_",end='')
            print(item)
            if start!=None:start+=1
        return arr

    def add(self):
        self.query.insert(self.setproduct())

    def edit(self):
        self.show(self.query.todictionary(self.query.select(),self.columns))
        self.query.update(Cinput.getpostive("please choose id from list : \n"),self.setproduct())

    def delete(self):
        self.show(self.query.todictionary(self.query.select(),self.columns))
        self.query.delete(Cinput.getpostive("please choose id from list : \n"))
    def show_list(self):
        self.show(self.query.todictionary(self.query.select(),self.columns))
    def search(self):

        arr=['search by:','1.id','2.price','3.entity','4.name']
        self.show(arr)
        x=Cinput.getconstrainedint(0,5,"please choose number from list : \n")
        value= Cinput.getpostive('enter your numeric value: ') if 0<x<4 else Cinput.getstr('enter name : ') 
            
        self.show(self.query.todictionary(self.query.select(value,arr[x][2:]),self.columns))
    


    def buy(self):
        products=self.show(self.query.todictionary(self.query.select(),self.columns),1)
        x=Cinput.getconstrainedint(0,len(products)+1,"please choose number of <row>  from list : \n")-1
        _product=dict(products[x])
        _product['entity']=str(Cinput.getconstrainedint(0,int(_product['entity'])+1,"enter your number that you have from this product: "))
        self.cart.append(products[x])
        self.show(self.cart)
        self.total_cost+=int(_product['entity'])*int(_product['price'])
        products[x]['entity']=str(int(products[x]['entity'])-int(_product['entity']))

        self.query.update(int(products[x]['id']),products[x])
        print('total price',self.total_cost)

    def exit():
        exit(0)