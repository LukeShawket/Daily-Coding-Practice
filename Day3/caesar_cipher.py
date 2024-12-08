alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encode_text(_message, shift_amount):
    encoded_text = ""
    position = 0
    for l in _message:
        for a in alphabet:
            if a == l:
                position = alphabet.index(a)
                encoded_text += alphabet[position - shift]
    print(f"Your encoded text text is: {encoded_text}")

def decode_text(_message, shift_amount):
    decoded_text = ""
    position = 0
    for l in _message:
        for a in alphabet:
            if a == l:
                position = alphabet.index(a)
                final_pos = 0
                if position + shift > len(alphabet) - 1:
                    final_pos = (position + shift) - len(alphabet)
                    decoded_text += alphabet[final_pos]
                else:
                    decoded_text += alphabet[position + shift]

    print(f"Your decoded text is: {decoded_text}")


if direction == "encode":
    encode_text(_message=text, shift_amount=shift)
elif direction == "decode":
    decode_text(_message=text, shift_amount=shift)
else:
    print("Please type correct matching letters!")