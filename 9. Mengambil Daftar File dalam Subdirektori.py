from ftplib import FTP

ftp = FTP('ftp.dlptest.com')
ftp.login(user='dlpuser', passwd='rNrKYTX9g7z3RgJRmxWuGHbeu')

ftp.cwd('new_directory')  # Masuk ke dalam direktori baru
files = ftp.nlst()
print("Daftar file dalam subdirektori:", files)
ftp.quit()
# Fungsi: Mengambil dan menampilkan daftar file dalam subdirektori.
# Kondisi: Ketika Anda ingin menjelajahi file dalam folder tertentu di server.
