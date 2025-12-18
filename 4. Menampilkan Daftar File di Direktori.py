from ftplib import FTP

ftp = FTP('ftp.dlptest.com')
ftp.login(user='dlpuser', passwd='rNrKYTX9g7z3RgJRmxWuGHbeu')

files = ftp.nlst()  # Mendapatkan daftar file di direktori saat ini
print("Daftar file:", files)
ftp.quit()
# Fungsi: Mengambil dan menampilkan daftar file di direktori server FTP.
# Kondisi: Ketika Anda ingin melihat konten direktori di server FTP.
