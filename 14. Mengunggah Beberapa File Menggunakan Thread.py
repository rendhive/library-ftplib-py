import threading
from ftplib import FTP

def upload_file(filename):
    ftp = FTP('ftp.dlptest.com')
    ftp.login(user='dlpuser', passwd='rNrKYTX9g7z3RgJRmxWuGHbeu')
    with open(filename, 'rb') as f:
        ftp.storbinary('STOR ' + filename, f)
    ftp.quit()
    print(f"File {filename} berhasil diunggah.")

# Mengunggah beberapa file secara asinkron
files_to_upload = ['upload1.txt', 'upload2.txt']
threads = []

for fn in files_to_upload:
    t = threading.Thread(target=upload_file, args=(fn,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
# Fungsi: Mengunggah beberapa file secara asinkron menggunakan threading.
# Kondisi: Ketika Anda ingin mengunggah banyak file tanpa menunggu satu per satu.
