from ftplib import FTP

ftp = FTP('ftp.dlptest.com')
ftp.login(user='dlpuser', passwd='rNrKYTX9g7z3RgJRmxWuGHbeu')

ftp.cwd('/parent_directory')  # Mengubah direktori
print("Sekarang berada di:", ftp.pwd())
# Fungsi: Mengubah direktori kerja di server FTP.
# Kondisi: Ketika Anda perlu menjelajahi folder lain di server FTP.
