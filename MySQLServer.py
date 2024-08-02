import mysql.connector
from mysql.connector import errorcode


def create_database():
    try:
        #Connect to MySQL server
        conn = mysql.connector.connect(
            host = "localhost",
            user = "Thato",
            password = "0205",
            database = "alx_book_store"
        )
        cursor = conn.cursor()

        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store DEFAULT CHARACTER SET 'utf8'")
            print("Database 'alx_book_store' created successfully!")        
        except mysql.connector.Error as err:
            print(f"Faild creating database: {err}")

        #close cursor and it connection
        cursor.closer()
        conn.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DECLINED_ERROR:
            print("Something went wrong with your username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            return err
    
if __name__ == "__main__":
    create_database()
        