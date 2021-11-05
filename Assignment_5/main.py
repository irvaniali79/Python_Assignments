from Store import Store
columns=['id','name','price','entity']

app = Store(columns,'datastore.csv')


def main(app):
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
            app.add()
        elif x == 2:
            app.edit()
        elif x == 3:
            app.delete()
        elif x == 4:
            app.show_list()
        elif x == 5:
            app.search()
        elif x == 6:
            app.buy()
        elif x == 7:
            app.exit()


if __name__=='__main__':
    main(app)