from ftplib import FTP_TLS

ftp = FTP_TLS('ftp.dlptest.com')
ftp.login(user='dlpuser', passwd='rNrKYTX9g7z3RgJRmxWuGHbeu')
ftp.prot_p()  # Mengatur proteksi data untuk transfer

print("Berhasil terhubung ke FTPS.")
# Fungsi: Menghubungkan ke server FTPS untuk komunikasi aman.
# Kondisi: Ketika Anda perlu meningkatkan keamanan data selama transfer.
