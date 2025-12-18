from ftplib import FTP

ftp = FTP('ftp.dlptest.com')
ftp.login(user='dlpuser', passwd='rNrKYTX9g7z3RgJRmxWuGHbeu')

with open('updated_file.txt', 'rb') as f:
    ftp.storbinary('STOR old_file.txt', f)  # Mengupdate file yang sudah ada

print("File berhasil diperbarui.")
ftp.quit()
# Fungsi: Memperbarui file yang sudah ada di server dengan konten baru.
# Kondisi: Ketika Anda ingin mengganti file yang ada dengan versi yang diperbarui.
