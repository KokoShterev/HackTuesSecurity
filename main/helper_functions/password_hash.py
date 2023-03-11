import string


def encrypt(plain_txt):
    all_letters = string.ascii_letters
    dict1 = {}
    for i in range(len(all_letters)):
        dict1[all_letters[i]] = all_letters[(i + 6) % len(all_letters)]
    cipher_txt = []
    for char in plain_txt:
        if char in all_letters:
            temp = dict1[char]
            cipher_txt.append(temp)
        else:
            temp = char
            cipher_txt.append(temp)
    cipher_txt = "".join(cipher_txt)
    return cipher_txt


def decrypt(cipher_txt):
    all_letters = string.ascii_letters
    dict2 = {}
    for i in range(len(all_letters)):
        dict2[all_letters[i]] = all_letters[(i - 6) % len(all_letters)]
    decrypt_txt = []
    for char in cipher_txt:
        if char in all_letters:
            temp = dict2[char]
            decrypt_txt.append(temp)
        else:
            temp = char
            decrypt_txt.append(temp)
    decrypt_txt = "".join(decrypt_txt)
    return decrypt_txt
