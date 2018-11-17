import hashlib

def md5encode(string):
    md5 = hashlib.md5()
    md5.update(string)
    return md5.hexdigest()

def sha1encode(string):
    sha1 = hashlib.sha1()
    sha1.update(string)
    return sha1.hexdigest()

def sha256encode(string):
    sha256 = hashlib.sha256()
    sha256.update(string)
    return sha256.hexdigest()

def sha384encode(string):
    sha384 = hashlib.sha384()
    sha384.update(string)
    return sha384.hexdigest()

def sha512encode(string):
    sha512 = hashlib.sha512()
    sha512.update(string)
    return sha512.hexdigest()

def sha_encode(sha, string):
    exec('sha = hashlib.sha' + str(sha) + '()')
    exec('sha.update(\'' + string + '\')')
    return sha.hexdigest()
