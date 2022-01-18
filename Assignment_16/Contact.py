import sqlite3
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from PySide6.QtUiTools import  QUiLoader
from functools import partial
import qdarkstyle

#TODO :~Validate
class MainWindow(QMainWindow):
    def __init__(self):

        super().__init__()
        self.Result=[]
        loader = QUiLoader()
        self.ui = loader.load("Design.ui")
        self.ui.show()
        self.conn = sqlite3.connect("dbContact.db")
        self.my_cursor = self.conn.cursor()

        self.ui.tableview.horizontalHeader().setStretchLastSection(True)
        self.ui.tableview.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableview.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tableview.cellClicked.connect(self.updateUiCellClick)

        self.ui.deletebtn.clicked.connect(partial(self.delete))
        self.ui.updatebtn.clicked.connect(partial(self.update))
        self.ui.insertbtn.clicked.connect(partial(self.insert))
        self.ui.deselectbtn.clicked.connect(partial(self.reset))


        self.ui.deleteallbtn.clicked.connect(partial(self.deleteAll))
        self.ui.darkmodecb.clicked.connect(partial(self.darkmode))
        self.selectedcontact=None

        self.load_data()

    def darkmode(self):
        dark_stylesheet =  qdarkstyle.load_stylesheet()
        global app
        if self.ui.darkmodecb.isChecked():
            app.setStyleSheet(dark_stylesheet)
        else:
            app.setStyleSheet(None)


    def updateUiCellClick(self):

        self.ui.deletebtn.setEnabled(True)
        self.ui.updatebtn.setEnabled(True)
        self.ui.insertbtn.setEnabled(False)

        row=self.ui.tableview.currentRow()
        self.ui.namelb.setText(self.ui.tableview.item(row,0).text())
        self.ui.numberlb.setText(self.ui.tableview.item(row,1).text())
        self.selectedcontact={
            'name':self.ui.tableview.item(row,0).text(),
            'number':self.ui.tableview.item(row,1).text()
        }

    def load_data(self):

        self.my_cursor.execute("SELECT * FROM contacts")
        records = self.my_cursor.fetchall()
        columnNames = [column[0] for column in self.my_cursor.description]
        for record in records:
            self.Result.append( dict( zip( columnNames , record ) ) )
        self.render()

    def fresh_db(self):

        self.my_cursor.execute("DELETE FROM contacts;")
        self.conn.commit()
        
        for row in self.Result:
            self.my_cursor.execute(f"INSERT INTO contacts (name,number)VALUES ('{row['name']}','{row['number']}');")
            self.conn.commit()
        
        return True


    def update_table(self):
        
        self.ui.tableview.setColumnCount(2)  
        self.ui.tableview.setRowCount(len(self.Result))
        
        myListOfHeaderLabels = ['name' , 'number']
        self.ui.tableview.setHorizontalHeaderLabels(myListOfHeaderLabels)     


    def render(self):

        self.update_table()
        for i in range(len(self.Result)):

            self.ui.tableview.setItem(i,0, QTableWidgetItem(self.Result[i]['name']))  
            self.ui.tableview.setItem(i,1, QTableWidgetItem(self.Result[i]['number']))  
        self.reset()
        self.fresh_db()

    def deleteAll(self):
        self.Result= []
        self.render()

    def delete(self):

        self.Result.remove(self.selectedcontact)
        self.render()

    def insert(self):
        if self.validate():

            contact={
                'name':self.ui.namelb.text(),
                'number':self.ui.numberlb.text()
            }

            self.Result.append(contact)

            self.render()

    def validate(self):
        try:
            tmp=int (self.ui.numberlb.text())
            return True
        except:
            return False
        
    
    def reset(self):
        self.ui.deletebtn.setEnabled(False)
        self.ui.updatebtn.setEnabled(False)
        self.ui.insertbtn.setEnabled(True)

        self.ui.namelb.setText("")
        self.ui.numberlb.setText("")

    def update(self):
        if self.validate():
            contact={}
            contact['name']=self.ui.namelb.text()
            contact['number']=self.ui.numberlb.text()
            self.Result.remove(self.selectedcontact)
            self.Result.append(contact)
            self.selectedcontact=None
            
            self.render()


class MyApp(QApplication):
    def __init__(self):
        super().__init__()
        self.window=MainWindow()
    



app = MyApp()      
app.exec()

