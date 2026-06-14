#cipher
'''
message: hellocoders
shift: 9
encrypted message:h-> q from below and so on qnuuxlxmnab
a b cdefghijklmnopqrstuvwxyz
0 1 23456789101112...
-> type yes to go again else no
-> yes
-> type encode to encrypt and decode to decrypt
decode
message: qnuuxlxmnab
shift: 9
decrypted message: hellocoders (subtracted shift number)
'''

letters_list = ['a','b','c','d','e','f','g','h'
,'i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def crypt_message(message, shift, encryption_type):
    result = ""
    for i in range(len(message)):
        # i = find index of h in letters_list
        index = letters_list.index(message[i])
        if encryption_type == "encode":
            shifted_index = (index + shift) % len(letters_list)
        elif encryption_type == "decode":
            shifted_index = (index - shift) % len(letters_list)
        else:
            raise ValueError("invalid encryption_type")

        result += letters_list[shifted_index]

    return result


message1 = input("message:")
shift1 = int(input("shift:"))
encrypted_message = crypt_message(message1,shift1,"encode")
decrypted_message = crypt_message(encrypted_message,shift1,"decode")

print(encrypted_message)
print(decrypted_message)



