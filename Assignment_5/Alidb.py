import os
import json
import csv
class Connection:

    def __init__(self,address):
        self.address=address
        file=open(self.address,"w")
        file.close()

    def connect(self,query,mode="a"):
        with open(self.address,mode) as file:
            print(file.read())
            return query(file)

class Query:

    connection=None
    id=0
    def __init__(self,connection,columns):
        self.connection=connection
        self.id=self.todictionary(self.select().split('\n')[-1],columns)['id']

    def __query(self,method):
        return self.connection.connect(method,'r')
    
    def __execute(self,method):
        self.connection.connect(method)

    def tofileformat(dictionary):
        record=""
        for key in dictionary.keys():
            record+=dictionary[key]+","
        return record[:-1]+"\n"
   
    def todictionary(self,line,columns):
        values=line.split(',')
        dic={columns[i]: values[i] for i in range(len(columns))}
        return dic

    def searchonarray(self,arr,key,value):
        for item in arr:
            if(self.todictionary(item)[key]==value):
                return item

    def insert(self,dictionary):
        self.id+=1
        dictionary['id']=self.id
        self.__execute(lambda file: file.write(self.tofileformat(dictionary)));

    def delete(self,id):
        records=self.select().split('\n')
        records.remove( self.searchonarray(records,'id',id))
        os.remove(self.connection.address)
        self.__execute(lambda file: file.write(records))
        
    def update(self,id,dictionary):
        self.delete(id);
        self.insert(dictionary)

    def select(self,value=None,key=None):
        if key==None:
            return self.__query((lambda file:file.read()));
        records=self.select(value,None).split('\n')
        return self.searchonarray(records,key,value)