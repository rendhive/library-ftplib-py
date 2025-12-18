from ftplib import FTP

ftp = FTP('ftp.dlptest.com')
ftp.login(user='dlpuser', passwd='rNrKYTX9g7z3RgJRmxWuGHbeu')

ftp.delete('upload_file.txt')  # Menghapus file yang diunggah
print("File berhasil dihapus.")
ftp.quit()
# Fungsi: Menghapus file di server FTP.
# Kondisi: Ketika Anda perlu menghapus file yang tidak lagi diperlukan.
