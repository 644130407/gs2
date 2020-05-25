import hashlib


def my_md5(mystr):
    md5 = hashlib.md5()
    md5.update(mystr.encode())
    return md5.hexdigest()