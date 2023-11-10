import mysql.connector
conexion=mysql.connector.connect(user= 'root', password='Apolo@74',
                                host='localhost',
                                database= 'prueba1',
                                port=3306)
print(conexion)