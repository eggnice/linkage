# !/usr/bin/python
# coding=utf-8
# ---edit by lambda---
# --email:freedom_whm@163.com

import hmac
from hashlib import sha1


def decrypt(salt, s):
    # decrypt a string(s)
    c = bytearray(str(s).encode('utf-8'))
    n = len(c)
    if n % 2 != 0:
        return ""
    n = n // 2
    b = bytearray(n)
    j = 0
    for i in range(0, n):
        c1 = c[j]
        c2 = c[j + 1]
        j = j + 2
        c1 = c1 - 46
        c2 = c2 - 46
        b2 = c2 * 19 + c1
        b1 = b2 ^ salt
        b[i] = b1
    return str(b.decode('utf-8'))


def shamac(key, url):
    sigbyte = hmac.new(key, url, sha1)
    return sigbyte.digest().encode('hex')


def enter(url):
    return shamac(decrypt(13, ':48473443392=0718472@2335444:48162=0>1:181:26471=3=2/313@2;40162'), url)
