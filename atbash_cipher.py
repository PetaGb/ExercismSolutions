def encode(plain_text):
  plain =  "abcdefghijklmnopqrstuvwxyz"
  cipher = "zyxwvutsrqponmlkjihgfedcba"
  encoded = ""
  for t in plain_text.lower():
    if t in plain:
      encoded += cipher[plain.index(t)]
    elif t.isnumeric():
        encoded += t
  return ' '.join([encoded[i:i+5] for i in range(0, len(encoded), 5)])

def decode(ciphered_text):
  plain =  "abcdefghijklmnopqrstuvwxyz"
  cipher = "zyxwvutsrqponmlkjihgfedcba"
  encoded = ""
  for t in ciphered_text.lower():
    if t in plain:
      encoded += cipher[plain.index(t)]
    elif t.isnumeric():
        encoded += t  
  return encoded
