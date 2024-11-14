import qrcode
import sqlite3
import io
from smtplib import SMTP



with sqlite3.connect('my_database.db') as connection:
    customer_websearch = input("please enter a url you would like to add")
    customer_name = input("please enter your name")
    

    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS QRCodeinfo (
        id INTEGER PRIMARY KEY,
        name TEXT,
        link TEXT,
        img BLOB 
    );
    

    ''')
    # Binary large object data type.

    
    img = qrcode.make(customer_websearch)
    img_buffer=io.BytesIO() #define img_buffer as a BYTESIO object
    img.save(img_buffer,format="PNG")
    img_binary = img_buffer.getvalue() # retrieves all the contents of the img buffer as a byte object representing in a image data in binary format

    insert_query = '''
    INSERT INTO QRCodeinfo (name,link,img)
    VALUES (?,?,?);
    '''
    cursor.execute(insert_query,(customer_name,customer_websearch,img_binary))

connection.commit()




