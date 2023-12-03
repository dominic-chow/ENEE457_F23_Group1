
# Reference here:
# https://mimic.mit.edu/docs/iv/modules/hosp/patients/

import AES

def encrypt(roundkeys, plaintext_tuple):
    encrypted_list = []
    for data in plaintext_tuple:
        encrypted = AES.encrypt(data.encode('ascii'), roundkeys)
        encrypted_list.append(encrypted)
    return tuple(encrypted_list)


def decrypt(roundkeys, encrypted_tuple):
    decrypted_list = []
    for data in encrypted_tuple:
        decrypted = AES.decrypt(data, roundkeys)
        decrypted_list.append(decrypted)
    return tuple(decrypted_list)

