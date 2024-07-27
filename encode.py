alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(plaintext, shift):
  encoded_text = ''
  for letter in plaintext:
    if letter in alphabet:
      index = alphabet.index(letter)
      encoded_text += alphabet[(index + shift) % len(alphabet)]
    else:
      encoded_text += letter
  return encoded_text

def decode(chipertext, shift):
  plaintext = ''
  for letter in chipertext:
    if letter in alphabet:
      index = alphabet.index(letter)
      plaintext += alphabet[(index - shift) % len(alphabet)]
    else:
      plaintext += letter
  return plaintext

plaintext = "aku suka kamu"
chipertext = encode(plaintext, 3)
print(f"Ciphertext: {chipertext}") 

for shift in range(26):
  decoded_text = decode(chipertext, shift)
  print(f"Shift: {shift}, {decoded_text}")