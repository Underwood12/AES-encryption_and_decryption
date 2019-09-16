from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

'''
    根据特定密钥进行AES 加解密
    若在本地运行，可以对检验代码加上MD5之类的防篡改检测
'''

#  账户
account = 'ssh123'
#  截止日期
date = '20191010'

class EncryptStr(object):
    def __init__(self, key):
        self.key = key.encode('utf-8')
        self.mode = AES.MODE_CBC

    def encrypt(self, text):
        text = text.encode()
        cryptor = AES.new(self.key, self.mode, self.key)
        length = 16
        count = len(text)
        if (count % length != 0):
            add = length - (count % length)
        else:
            add = 0
        text = text + ('\0' * add).encode()
        self.ciphertext = cryptor.encrypt(text)
        return b2a_hex(self.ciphertext).decode()

    # 解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        plain_text = cryptor.decrypt(a2b_hex(text))
        return plain_text.decode('utf-8').strip('\0')

if __name__ == '__main__':
    #  长度必须是16，密钥不同，所产生的的密文也不同
    pc = EncryptStr('keyskeyskeyskeys')  # 初始化密钥
    e = pc.encrypt(account + '+' + date)
    print('密文', e)
    d = pc.decrypt(e)
    print('明文', d)
