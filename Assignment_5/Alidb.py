import os

class Connection:

    def __init__(self,address):
        self.address=address
        file=open(self.address,"a")
        file.close()

    def connect(self,query,mode="a"):
        with open(self.address,mode) as file:
            return query(file)

class Query:

    connection=None
    id=0
    def __init__(self,connection,columns):
        self.connection=connection
        self.columns=columns
        arr=self.todictionary(self.select(),columns)
        self.numoflines=len(arr) if arr[-1]!='' else 0
        self.id=int(arr[-1]['id'] if isinstance(arr,list) and len(arr)>1 else (arr['id']) if isinstance(arr,dict) else 0)
        
    def __query(self,method):
        return self.connection.connect(method,'r')
    
    def __execute(self,method):
        self.connection.connect(method)

    def tofileformat(self,dictionaries,columns=None):
        columns=self.columns if columns==None else columns
        if not isinstance(dictionaries,list):dictionaries=[dictionaries]
        record=""


        for dictionary in dictionaries:            
            for key in columns:
                record+=str(dictionary[key])+","
            record=record[:-1]+"\n"

        return record[:-1]
   
    def todictionary(self,line,columns=None):
        columns=self.columns if columns==None else columns
        arr=line.split('\n')
        if arr[0]=='' :return arr
        data=[]
        for item in arr:
            values=item.split(',')
            data.append({columns[i]: values[i] for i in range(len(columns))})

        return data if len(arr)>1 else data[0]

    def searchonarray(self,arr,key,value):
        for item in arr:
            if(self.todictionary(item)[key]==str(value)):
                return item

    def insert(self,dictionary):
        self.id+=1
        dictionary['id']=self.id
        self.numoflines+=1
        line="\n" if self.numoflines!=1 else ""
        self.__execute(lambda file: file.write(line+self.tofileformat(dictionary)));

    def delete(self,id):
        records=self.select().split("\n")
        records.remove( self.searchonarray(records,'id',id))
        self.numoflines-=1
        os.remove(self.connection.address)
        if(records==[]):
            self.__execute(lambda file: file.write(""))
        else :
            self.__execute(lambda file: file.write(self.tofileformat(self.todictionary("\n".join(record for record in records)))))
        
    def update(self,id,dictionary):
        self.delete(id);
        self.insert(dictionary)

    def select(self,value=None,key=None):
        if key==None:
            return self.__query((lambda file:file.read()));
        records=self.select(value,None).split('\n')
        return self.searchonarray(records,key,value)