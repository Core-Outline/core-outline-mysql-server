import pyodbc

conn_lims = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                           "Server=localhost\\SQLEXPRESS;"
                           "Database=Robodine;"
                           "uid=CoreOutline;pwd=Tobirama13")
