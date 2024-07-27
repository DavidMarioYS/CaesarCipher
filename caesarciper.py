import string

def caesar_cipher(text, shift, mode='encode'):
    # Membuat alfabet huruf kecil dan huruf besar
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    
    result = ""
    
    for char in text:
        if char.isalpha():
            # Menentukan alfabet yang akan digunakan (kecil atau besar)
            alphabet = lowercase if char.islower() else uppercase
            
            # Mencari indeks karakter dalam alfabet
            index = alphabet.index(char)
            
            if mode == 'encode':
                # Untuk enkripsi, geser ke kanan
                new_index = (index + shift) % 26
            else:
                # Untuk dekripsi, geser ke kiri
                new_index = (index - shift) % 26
            
            # Menambahkan karakter hasil ke string result
            result += alphabet[new_index]
        else:
            # Jika bukan huruf, tambahkan langsung tanpa perubahan
            result += char
    
    return result

def encode(plaintext, shift):
    return caesar_cipher(plaintext, shift, mode='encode')

def decode(ciphertext, shift):
    return caesar_cipher(ciphertext, shift, mode='decode')

# Contoh penggunaan
plaintext = "Hello World! 123"
shift = 3

# Enkripsi
encrypted = encode(plaintext, shift)
print(f"Encrypted: {encrypted}")

# Dekripsi
decrypted = decode(encrypted, shift)
print(f"Decrypted: {decrypted}")

# Mencoba semua kemungkinan shift untuk dekripsi
print("\nMencoba semua kemungkinan shift:")
for i in range(26):
    print(f"Shift {i}: {decode(encrypted, i)}")