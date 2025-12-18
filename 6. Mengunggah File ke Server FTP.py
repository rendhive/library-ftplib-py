from ftplib import FTP

ftp = FTP('ftp.dlptest.com')
ftp.login(user='dlpuser', passwd='rNrKYTX9g7z3RgJRmxWuGHbeu')

with open('upload_file.txt', 'rb') as f:
    ftp.storbinary('STOR upload_file.txt', f)

print("File berhasil diunggah.")
ftp.quit()
# Fungsi: Mengunggah file dari lokal ke server FTP.
# Kondisi: Ketika Anda perlu menyimpan file di server FTP.
