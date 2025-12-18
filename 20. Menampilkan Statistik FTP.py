from ftplib import FTP

ftp = FTP('ftp.dlptest.com')
ftp.login(user='dlpuser', passwd='rNrKYTX9g7z3RgJRmxWuGHbeu')

print("Statistics:")
print("Current Directory:", ftp.pwd())
print("Welcome Message:", ftp.getwelcome())
print("Files:", ftp.nlst())
ftp.quit()
# Fungsi: Menampilkan informasi statistik dasar tentang server FTP dan file.
# Kondisi: Ketika Anda perlu mendapatkan gambaran umum tentang server FTP yang ada.
