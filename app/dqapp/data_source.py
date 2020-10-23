
import pyodbc



class DataSource:
    """Data source class."""

    def __init__(self,data_source_name,user_id,password,hostname,port,database_name):
        self.data_source_name=data_source_name
        self.user_id=user_id
        self.password=password
        self.hostname=hostname
        self.port=port
        self.database_name=database_name

    def getconnection(self):
        
        driver = 'DRIVER={MySQL ODBC 8.0 Ansi Driver}'
        connectstr = f'{driver};uid={self.user_id};Password={self.password};Server={self.hostname};Database={self.database_name};Port={self.port};'

        # MySQL
        if self.data_source_name == "mysql":
            connection = pyodbc.connect(connectstr)
            connection.setdecoding(pyodbc.SQL_CHAR, encoding='iso-8859-1')
            connection.setdecoding(pyodbc.SQL_WCHAR, encoding='iso-8859-1')
            connection.setencoding(encoding='iso-8859-1')
       

        else:
            message = f'Invalid data source  {self.data_source_name}'
            raise ValueError(message)

        return connection

    def checkconnection(self):
        connectstr=''
        print(self.data_source_name)
        if self.data_source_name == 'mysql':
            driver = 'DRIVER={MySQL ODBC 8.0 Ansi Driver}'
            connectstr = f'{driver};uid={self.user_id};Password={self.password};Server={self.hostname};Database={self.database_name};Port={self.port};'
            print(connectstr)

        try:
            cnxn = pyodbc.connect(connectstr)
        except pyodbc.Error as ex:
            print(ex)
            # return None
            return str(ex)

        if cnxn:
            cnxn.close()
            return str(cnxn)
        