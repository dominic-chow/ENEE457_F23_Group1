import AES

ADMIN_USER_ENCRYPTED = b'V\x8d0U\x14\\\xa2\xf8\xb7\x950M\xd4\xc3\xefo'
ADMIN_PASS_ENCRYPTED = b'*\x14e\xbb\x81\xbe\xbc$\xf4\xabc\x80\x90re\x95'

def admin_login(user, pw):
    encrypted_user = AES.encrypt(user)
    encrypted_pw = AES.encrypt(pw)
    if encrypted_user == ADMIN_USER_ENCRYPTED and encrypted_pw == ADMIN_PASS_ENCRYPTED:
        print('Login Success')
        return True
    else:
        print('Incorrect login')
        return False