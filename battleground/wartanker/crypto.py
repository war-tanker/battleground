import base64, string

def b64encode(string, encoding='UTF-8'):
    return base64.b64encode(bytes(string, encoding)).decode()

def b64decode(string):
    return base64.b64decode(string).decode()

def b32encode(string, encoding='UTF-8'):
    return base64.b32encode(bytes(string, encoding)).decode()

def b32decode(string):
    return base64.b32decode(string).decode()

def b16encode(string, encoding='UTF-8'):
    return base64.b16encode(bytes(string, encoding)).decode()

def b16decode(string):
    return base64.b16decode(string).decode()

class UnknownBaseError(Exception): 
    def __init__(self):
        super().__init__('Unknown base given')
 
def base_encode(base, string, encoding='UTF-8'):
    if base in (16, 32, 64):
        return eval('b' + str(base) + "encode('" + str(string) + "', '" + str(encoding) + "')")
    else: raise UnknownBaseError

def base_decode(string, base=''):
    if base in (16, 32, 64):
        return eval('b' + str(base) + "decode('" + str(string) + "')")
    else: 
        try: return b64decode(string)
        except:
            try: return b32decode(string)
            except:
                try: return b16decode(string)
                except: raise UnknownBaseError

def hex2str(hexdata, _split=''):
    if _split:
        return ''.join([chr(int(char, 16)) for char in hexdata.split(_split)])
    else: 
        return ''.join([chr(int(char, 16)) for char in [hexdata[i:i+2] for i in range(0, len(hexdata), 2)]])

def str2hex(string, _join=''):
    return _join.join([format(ord(char), '02X') for char in string])

def caesar_encrypt(string, key):
    ret = ''
    for i in string:
        if (i.isalpha()):
            ret += chr(((ord(i) - ord('A' if i.isupper() else 'a') + key) % 26) + ord('A' if i.isupper() else 'a'))
    return ret

def caesar_decrypt(string, key=''):
    R = range(26)
    if not key == '': R = range(key, key+1)
    ans = []
    for k in R:
        ret = ''
        for i in string:
            if (i.isalpha()):
                ret += chr(((ord(i) - ord('A' if i.isupper() else 'a') - k) % 26) + ord('A' if i.isupper() else 'a'))
        if key == '': ans.append(ret)
        else: return ret
    return ans
