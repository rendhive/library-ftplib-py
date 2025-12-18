from ftplib import FTP

ftp = FTP('ftp.dlptest.com')
ftp.login(user='dlpuser', passwd='rNrKYTX9g7z3RgJRmxWuGHbeu')

print("Server:", ftp.getwelcome())
# Fungsi: Menampilkan informasi sambutan dari server FTP.
# Kondisi: Ketika Anda ingin melihat informasi dasar tentang server FTP.
