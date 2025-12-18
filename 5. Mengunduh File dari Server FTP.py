from ftplib import FTP

ftp = FTP('ftp.dlptest.com')
ftp.login(user='dlpuser', passwd='rNrKYTX9g7z3RgJRmxWuGHbeu')

with open('downloaded_file.txt', 'wb') as f:
    ftp.retrbinary('RETR test.txt', f.write)

print("File berhasil diunduh.")
ftp.quit()
# Fungsi: Mengunduh file dari server FTP dan menyimpannya di lokal.
# Kondisi: Ketika Anda perlu mendapatkan file dari server FTP ke komputer Anda.
