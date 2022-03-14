import sqlite3 as db

class DataBase():
    def connect(self):
        global cursor
        #self.database=DataBase()
        #sql=address_save
        self.dataBase = db.connect("Database.db")
        cursor= self.dataBase.cursor()
        cursor.execute("CREATE table if not EXISTS data(Local TEXT not null unique)")

    def adicionar(self,address_save):
        self.connect()
        sql1=f"INSERT into data values('{address_save}')"
        cursor.execute(sql1)
        self.dataBase.commit()

        select=f"SELECT * FROM data ;"
        cursor.execute(select)
            
            
        for element in cursor.fetchall():
            print(element)
                
            
                        
        self.dataBase.close()