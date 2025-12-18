from ftplib import FTP

ftp = FTP('ftp.dlptest.com')
ftp.login(user='dlpuser', passwd='rNrKYTX9g7z3RgJRmxWuGHbeu')

ftp.mkd('new_directory')  # Membuat direktori baru di server
print("Direktori baru berhasil dibuat.")
ftp.quit()
# Fungsi: Membuat direktori baru di server FTP.
# Kondisi: Ketika Anda perlu menyusun file di server dengan folder.
