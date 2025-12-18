from ftplib import FTP

ftp = FTP('ftp.dlptest.com')
ftp.login(user='dlpuser', passwd='rNrKYTX9g7z3RgJRmxWuGHbeu')

print("Berhasil login ke server FTP.")
# Fungsi: Melakukan otentikasi ke server FTP dengan username dan password.
# Kondisi: Ketika Anda ingin mengakses server FTP yang dilindungi oleh otentikasi.
