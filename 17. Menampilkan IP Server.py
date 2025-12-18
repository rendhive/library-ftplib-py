from ftplib import FTP

ftp = FTP('ftp.dlptest.com')
ftp.login(user='dlpuser', passwd='rNrKYTX9g7z3RgJRmxWuGHbeu')

print("IP address dari server:", ftp.sock.getpeername()[0])
ftp.quit()
# Fungsi: Menampilkan alamat IP server yang terhubung ke socket FTP.
# Kondisi: Ketika Anda perlu mengetahui detail koneksi saat ini.
