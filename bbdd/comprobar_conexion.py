import mysql.connector

class ComprobadorMySQL:
    def comprobar_conexion(self, host, user, password, database, port):
        try:
            connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                port=port
            )
            if connection.is_connected():
                connection.close()
                return True
        except mysql.connector.Error:
            return False
        return False
