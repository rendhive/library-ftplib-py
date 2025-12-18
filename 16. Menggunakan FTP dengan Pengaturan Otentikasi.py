from ftplib import FTP

ftp = FTP('ftp.dlptest.com')
ftp.login(user='your_username', passwd='your_password')  # Ganti sesuai dengan kredensial yang sesuai

print("Login berhasil.")
ftp.quit()
# Fungsi: Melakukan autentikasi dengan username dan password pada server FTP.
# Kondisi: Ketika Anda perlu mengakses server bersama yang memerlukan kredensial.
