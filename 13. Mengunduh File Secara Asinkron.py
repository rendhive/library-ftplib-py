import threading
from ftplib import FTP

def download_file(filename):
    ftp = FTP('ftp.dlptest.com')
    ftp.login(user='dlpuser', passwd='rNrKYTX9g7z3RgJRmxWuGHbeu')
    with open(filename, 'wb') as f:
        ftp.retrbinary('RETR ' + filename, f.write)
    ftp.quit()
    print(f"File {filename} berhasil diunduh.")

# Mengunduh beberapa file secara asinkron
threads = []
for fn in ['test.txt', 'test1.txt']:
    t = threading.Thread(target=download_file, args=(fn,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
# Fungsi: Mengunduh file secara asinkron menggunakan threads.
# Kondisi: Ketika Anda ingin mengoptimalkan waktu dengan mengunduh beberapa file sekaligus.
