import inspect, os, csv
import pyodbc
import logging
from LoggerManager import NewLogger

# Source https://github.com/bAcheron/basic_etl/blob/master/DatabaseManager.py

class NewDatabaseManager:


    def __init__(self, server_name, database, logger_file_name=''):
        #self.conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server_name+';DATABASE='+database+'')
        self.conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server_name+';DATABASE='+database+';UID=sa;PWD=#abc123#')
        self.database = database
        #self.logger_file_name=logger_file_name
        #self.database_logger = NewLogger('DatabaseManager',self.logger_file_name)
        self.cursor = self.conn.cursor()
	
	
    def select_data(self,sql_string):
        logging.info('get_sql_data run on ' + self.database)	
        table_data = self.cursor.execute(sql_string)
        table_data =  self.cursor.fetchall()
        return table_data
	

    # ACESSANDO STORED PROCEDURE COM PYTHON
    # Em sql É assim:  EXEC stp_GetMultiCode 'Pessoa', id, 1
    def chama_id(self):
        cursor = self.conn.cursor()
        abc = cursor.execute("EXEC stp_GetMultiCode 'NaturezaLancamento', 'IdNaturezaLancamento', 1")
        for row in abc:
            return row[0]
            

    def cap_name(self, name):
        p = ['da','das', 'de', 'di', 'do','dos', 'du', 'para', 'com', 'a', 'e']
        items = []
        for item in name.split():
            if not item.lower() in p:
                item = item.capitalize()
            else:
                item = item.lower()
            items.append(item)
        return ' '.join(items)

    def insert_sql_data(self, sql_string, data):
        try:
            logging.info('insert_sql_data run on: ' + self.database)
            cursor = self.conn.cursor()
            cursor.execute(sql_string,data)
            cursor.commit()
            return 0
        except pyodbc.Error as ex:
            logging.error('insert_sql_data run on: ' + self.database + 'for query: '+str(ex))
            return 1


    def delete_sql_data(self, sql_string, data):
        try:
            logging.info('delete_sql_data run on: ' + self.database)
            cursor = self.conn.cursor()
            cursor.execute(sql_string, data)
            cursor.commit()
            return 0
        except pyodbc.Error as ex:
            logging.error('delete_sql_data run on: ' + self.database + 'for query: '+str(ex))
            return 1

    def delete_all_sql_data(self, sql_string):
        try:
            logging.info('delete_sql_data run on: ' + self.database)
            cursor = self.conn.cursor()
            cursor.execute(sql_string)
            cursor.commit()
            return 0
        except pyodbc.Error as ex:
            logging.error('delete_sql_data run on: ' + self.database + 'for query: '+str(ex))
            return 1


    def update_sql_data(self,sql_string,data):
        try:
            logging.info('update_sql_data run on: ' + self.database)
            cursor = self.conn.cursor()
            cursor.execute(sql_string,data)
            cursor.commit()
            return 0
        except pyodbc.Error as ex:
            logging.error('update_sql_data run on: ' + self.database + 'for query: '+str(ex))
            return 1
	

    def run_sql_data(SqlString):
        try:
            logging.info('run_sql_data run on ' + self.database)
            cursor = self.p_conn.cursor()
            cursor.execute(SqlString)
            cursor.commit()
        except pyodbc.Error as ex:
            logging.error('get_sql_data run on ' + self.database)
            return -1

