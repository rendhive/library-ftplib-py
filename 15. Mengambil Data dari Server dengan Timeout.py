from ftplib import FTP

ftp = FTP('ftp.dlptest.com', timeout=5)  # Mengatur timeout 5 detik
ftp.login(user='dlpuser', passwd='rNrKYTX9g7z3RgJRmxWuGHbeu')

try:
    files = ftp.nlst()  # Mengambil daftar file
    print("Daftar file:", files)
except Exception as e:
    print("Error:", e)

ftp.quit()
# Fungsi: Mengambil data dengan pengaturan timeout agar tidak menunggu terlalu lama.
# Kondisi: Ketika Anda ingin memastikan bahwa aplikasi tidak terjebak menunggu respons dari server.
