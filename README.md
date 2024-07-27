# Caesar Cipher Encoder/Decoder

## Deskripsi Umum

Proyek ini mengimplementasikan Caesar Cipher, sebuah teknik enkripsi sederhana yang digunakan dalam kriptografi. Caesar Cipher bekerja dengan menggeser setiap huruf dalam pesan sebanyak jumlah tertentu dalam alfabet.

## Cara Kerja Caesar Cipher

Caesar Cipher mengenkripsi pesan dengan menggeser setiap huruf dalam alfabet sejumlah posisi tertentu. Misalnya, dengan pergeseran 3:
- A menjadi D
- B menjadi E
- C menjadi F
dan seterusnya.

## Rumus

- Enkripsi: E(x) = (x + n) mod 26
- Dekripsi: D(x) = (x - n) mod 26

Dimana:
- x adalah posisi huruf dalam alfabet (A=0, B=1, ..., Z=25)
- n adalah jumlah pergeseran
- mod 26 memastikan hasil tetap dalam rentang alfabet

## Fitur

- Enkripsi pesan menggunakan Caesar Cipher
- Dekripsi pesan yang telah dienkripsi
- Brute force dekripsi untuk menemukan pesan asli tanpa mengetahui kunci

## Cara Penggunaan

### Enkripsi (encode.py)

1. Buka file `encode.py`
2. Ubah variabel `plaintext` dengan pesan yang ingin dienkripsi
3. Jalankan script dengan perintah: `python encode.py`
4. Hasil enkripsi akan ditampilkan bersama dengan semua kemungkinan dekripsi

### Dekripsi (decode.py)

1. Buka file `decode.py`
2. Ubah variabel `chipertext` dengan pesan terenkripsi yang ingin didekripsi
3. Jalankan script dengan perintah: `python decode.py`
4. Semua kemungkinan hasil dekripsi akan ditampilkan

## Struktur Kode

Kedua file (encode.py dan decode.py) menggunakan struktur yang sama:

1. Definisi alfabet
2. Fungsi `encode()` untuk enkripsi
3. Fungsi `decode()` untuk dekripsi
4. Bagian utama yang menjalankan enkripsi/dekripsi dan menampilkan hasil