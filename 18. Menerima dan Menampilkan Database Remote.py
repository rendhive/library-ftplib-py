import sqlite3
from ftplib import FTP

def fetch_db():
    ftp = FTP('ftp.dlptest.com')
    ftp.login(user='dlpuser', passwd='rNrKYTX9g7z3RgJRmxWuGHbeu')

    with open('remote.db', 'wb') as f:
        ftp.retrbinary('RETR my_database.db', f.write)

    conn = sqlite3.connect('remote.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM my_table')
    for row in cursor.fetchall():
        print(row)
    conn.close()
    ftp.quit()

fetch_db()
# Fungsi: Mengambil file database dari FTP dan menampilkannya.
# Kondisi: Ketika Anda ingin mengakses data yang ada di file database di server FTP.
